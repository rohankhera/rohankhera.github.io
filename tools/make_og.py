"""Render og-image.jpg (1200x630 share card) and the touch icon from tools/og.html.

Needs Playwright and Pillow. Run from the repo root:  python3 tools/make_og.py
"""
import io
import subprocess
import sys
import time

from PIL import Image
from playwright.sync_api import sync_playwright

PORT = "8766"
server = subprocess.Popen(
    [sys.executable, "-m", "http.server", PORT, "--bind", "127.0.0.1"],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
)
time.sleep(1)
try:
    with sync_playwright() as p:
        browser = p.chromium.launch()

        page = browser.new_page(viewport={"width": 1200, "height": 630}, color_scheme="light")
        page.goto(f"http://127.0.0.1:{PORT}/tools/og.html", wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        png = page.screenshot()
        Image.open(io.BytesIO(png)).convert("RGB").save(
            "og-image.jpg", quality=88, optimize=True, progressive=True)

        icon = browser.new_page(viewport={"width": 180, "height": 180})
        icon.set_content(
            '<body style="margin:0;background:#15181e">'
            f'<img src="http://127.0.0.1:{PORT}/assets/favicon.svg" width="180" height="180"></body>')
        icon.wait_for_load_state("networkidle")
        icon.screenshot(path="assets/apple-touch-icon.png")

        browser.close()
finally:
    server.terminate()
print("wrote og-image.jpg and assets/apple-touch-icon.png")
