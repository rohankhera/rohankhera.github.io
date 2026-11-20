# rohankhera.com

Personal website of Rohan Khera, MD, MS: one static page served by GitHub Pages at [rohankhera.com](https://rohankhera.com).

## Updating it

All the words are in `index.html`. Each section starts with a comment explaining how to add a row. For example, a new paper is one block copied and changed:

```html
<li>
  <time>2027</time>
  <div class="what"><a href="https://doi.org/...">Title of the paper</a> <span class="where">Journal</span></div>
</li>
```

Edit the file on GitHub, commit to `main`, and the site updates within a couple of minutes. The yearly checklist is in `CLAUDE.md`.

Styling is in `assets/site.css` and does not need touching for content changes.
