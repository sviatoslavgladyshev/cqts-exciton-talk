# Prompt for editing this deck with an AI assistant

Copy everything below the line into Claude (or another assistant) and attach `index.html`. Attach the other files it mentions only if the change touches them. Replace the last line with what you want.

---

You are editing a self-contained HTML slide deck hosted on GitHub Pages. It is a research symposium talk:
"Topological excitons in biased bilayer graphene" by Sviatoslav Gladyshev, supervised by Dr. Marwa Mannai,
Center for Quantum and Topological Systems (CQTS), NYU Abu Dhabi. The audience is academic, so physics must be correct
and anything not yet computed must stay labelled "proposed" or "schematic".

**How the deck is built**
- `index.html` holds the viewer (CSS + one inline `<script>`) and every slide.
- Each slide is `<section class="slide" id="…" data-transition="push|fade|magic" style="…">` on a fixed 1920 × 1080 canvas,
  with all styling inline in px. The viewer scales the canvas to the window. Do not use `vw`, `vh`, `rem` or external CSS inside slides.
- Speaker notes are the plain-text `<aside>` at the end of each section (hidden on screen; shown by the N key and the presenter window).
- Elements with `data-build-in="rise|pop|fade <order> auto"` animate in one after another when the slide opens.
- `data-transition` on a section says how that slide *leaves*: `push` slides sideways, `fade` cross-fades, `magic` is a quick cross-fade
  used between proof steps that share a header.
- Equations are LaTeX-rendered PNGs in `assets/eq-*.png` (accent versions: `eq-*-accent.png`). To add an equation, typeset it with
  LaTeX (standalone class, Computer Modern, ink colour #202124, accent colour #0D40A6), render a PNG with a transparent background
  at about 960 dpi, and size it so 1 em is about 55 px on the 1920 × 1080 canvas. Never write maths as plain text with
  underscores (for example `Omega_X`); use a LaTeX image, or words.
- Animations are GIFs in `assets/anim-*.gif`. The live illustration on slide 3 is `embed-recreation.html`, loaded into an iframe.
- `thumbs/<slide-id>.jpg` (480 × 270) are used by the grid and presenter view. Regenerate one when you change a slide.

**Design rules**
- Brand colours from the CQTS logo: purple `#4E057E` (eyebrows, titles' accent, buttons) and blue `#0D40A6`
  (results, links). Text `#202124`, secondary text `#5F6368`, light panel `#F8F9FA`, result card `#F1EAF7`.
- Physics colours stay fixed: electrons blue, holes red, excitons green.
- Font: Roboto (self-hosted in `fonts/`). Sizes on the 1920 × 1080 canvas: 96–120 px titles on the cover,
  64–72 px slide titles, 44 px subheads, 28–32 px body, 24 px minimum for captions.
- Keep the CQTS logo bottom right and the slide number to its left, as on the existing slides.
- One idea per slide; keep equations as numbered step cards, as on the existing proof slides.

**What I want you to do:**
[describe the change here, e.g. "add a slide after slide 13 that derives …", "translate all slide text to Russian",
"make slide 3's animation slower"]

Return the complete updated `index.html` (or only the sections you changed, clearly marked), plus any new asset files and the
LaTeX source for any new equation.
