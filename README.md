# Prompt Atlas

A searchable library of 125 complete, ready-to-use AI prompts across 25 categories. Each prompt has a role, goal, inputs, instructions, constraints, and output format.

- `index.html` is the interactive library (static, no build needed to serve).
- `p/<id>/` and `c/<category>/` are generated static pages, one per prompt and per category, for search engines. `sitemap.xml` lists them.
- `prompts.json` holds every prompt as data.
- `src/` holds the prompt sources, `template.html`, `pages.py` and `build.py`. Run `cd src && python3 build.py` to rebuild after editing anything.

## Monetization settings

`src/config.json` controls the newsletter form, support button, GitHub Sponsors link, Pro Pack checkout link and price, and GoatCounter analytics. An empty value hides that feature. `src/pro_previews.json` holds the public teaser titles for the Pro Pack (the paid prompts themselves are not in this repo). Edit, rebuild, commit, push.

Live at https://sai-code-glitch.github.io/Promptatlas/
