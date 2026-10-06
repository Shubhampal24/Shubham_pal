# Shubham Pal | Portfolio

Static portfolio (HTML/CSS/JS, no dependencies), built by a tiny Python script and hosted on Vercel.

## Structure
- `src/index.html`: the whole page (content, styles, scripts)
- `assets/`: `avatar.jpg`, `Shubham_Pal_Resume.pdf` (replace the PDF to update the download button)
- `build_portfolio.py`: copies `src/` + `assets/` into `public/`
- `vercel.json`: Vercel runs `python build_portfolio.py --build` and serves `public/`

## Run locally
    python build_portfolio.py        # builds and opens http://localhost:3000

## Deploy
Push to GitHub. Vercel rebuilds automatically (config already in `vercel.json`).

## Edit content
Everything is plain HTML in `src/index.html`. Search for the section ids: `home`, `about`, `skills`, `journey`, `projects`, `education`, `contact`.
