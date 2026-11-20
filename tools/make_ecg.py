"""Generate assets/ecg.svg — the repeating rhythm-strip tile used in the header.

A synthetic lead II in sinus rhythm (sum-of-Gaussians P-QRS-T model), drawn at
standard paper scale: 25 mm/s, 10 mm/mV, with 1 mm = 4 px. The tile holds four
beats with slightly different R-R intervals so the repeat is not obvious.

Run from the repo root:  python3 tools/make_ecg.py
"""
import math

PX_PER_MM = 4
PX_PER_S = 25 * PX_PER_MM        # 100 px per second
PX_PER_MV = 10 * PX_PER_MM       # 40 px per millivolt
HEIGHT = 30 * PX_PER_MM          # 120 px, six large squares
BASELINE = 20 * PX_PER_MM        # 80 px from the top

RR = [0.94, 0.97, 0.93, 0.90]    # seconds; ~64 bpm with mild sinus arrhythmia
PERIOD = sum(RR)
FIRST_R = 0.33

# (offset from R peak in s, amplitude in mV, sigma before peak, sigma after peak)
WAVES = [
    (-0.170, 0.13, 0.022, 0.022),   # P
    (-0.030, -0.07, 0.008, 0.008),  # Q
    (0.000, 1.05, 0.0095, 0.0095),  # R
    (0.030, -0.17, 0.009, 0.009),   # S
    (0.265, 0.30, 0.058, 0.036),    # T (slower upstroke than downstroke)
]


def r_times():
    t, out = FIRST_R, []
    for rr in RR:
        out.append(t)
        t += rr
    # neighbours on either side so the tile wraps cleanly
    return [out[-1] - PERIOD] + out + [out[0] + PERIOD]


def mv(t, rs):
    v = 0.0
    for r in rs:
        for off, amp, s_before, s_after in WAVES:
            d = t - (r + off)
            s = s_before if d < 0 else s_after
            if abs(d) < 5 * s:
                v += amp * math.exp(-0.5 * (d / s) ** 2)
    return v


def simplify(pts, tol):
    """Ramer-Douglas-Peucker."""
    if len(pts) < 3:
        return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    norm = math.hypot(dx, dy) or 1.0
    worst, idx = 0.0, 0
    for i in range(1, len(pts) - 1):
        d = abs(dy * (pts[i][0] - x1) - dx * (pts[i][1] - y1)) / norm
        if d > worst:
            worst, idx = d, i
    if worst <= tol:
        return [pts[0], pts[-1]]
    return simplify(pts[: idx + 1], tol)[:-1] + simplify(pts[idx:], tol)


def main():
    rs = r_times()
    width = round(PERIOD * PX_PER_S)
    n = width * 8
    pts = []
    for i in range(n + 1):
        x = i * width / n
        y = BASELINE - mv(x / PX_PER_S, rs) * PX_PER_MV
        pts.append((x, y))
    pts[0] = (0.0, float(BASELINE))
    pts[-1] = (float(width), float(BASELINE))
    pts = simplify(pts, 0.08)

    def f(v):
        return f"{v:.2f}".rstrip("0").rstrip(".")

    d = "M" + " ".join(f"{f(x)} {f(y)}" for x, y in pts)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{HEIGHT}" '
        f'viewBox="0 0 {width} {HEIGHT}">'
        f'<path d="{d}" fill="none" stroke="#000" stroke-width="1.3" '
        f'stroke-linejoin="round" stroke-linecap="round"/></svg>\n'
    )
    with open("assets/ecg.svg", "w") as fh:
        fh.write(svg)
    print(f"assets/ecg.svg: {width}x{HEIGHT}px, {len(pts)} points, {len(svg)} bytes")


if __name__ == "__main__":
    main()
