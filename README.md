# Topological excitons in biased bilayer graphene

Research symposium talk by **Sviatoslav Gladyshev**, supervised by **Dr. Marwa Mannai**,
Center for Quantum and Topological Systems (CQTS), NYU Abu Dhabi.

A self-contained HTML slide deck with its own viewer: no build step, no framework, no internet needed once downloaded.

## View it

- **Online:** <https://sviatoslavgladyshev.github.io/cqts-exciton-talk/>
- **Locally:** run `python3 -m http.server` in this folder and open <http://localhost:8000>.
  You can open `index.html` directly too, but some browsers block the live illustration on slide 3 from `file://`.

## Controls

| Key | Action |
|---|---|
| → ↓ Space Enter PageDown | Next slide |
| ← ↑ Backspace PageUp | Previous slide |
| Home / End | First / last slide |
| 12 then Enter | Jump to slide 12 |
| **F** | Full screen |
| **G** | All slides, grouped by section (arrow keys and Enter work here) |
| **N** | Speaker notes |
| **P** | Presenter window: notes, next slide, timer and clock, kept in sync with the main window |
| **B** or **.** | Black screen; any key brings the slide back |
| **?** | Keyboard shortcuts |
| Esc | Close the grid, notes or shortcuts |

Click the right part of a slide to go forward and the left third to go back. On a phone, swipe.
Move the pointer to bring up the control bar, and hover over its timeline to preview any slide.
The address bar keeps the slide number (`#12`), so you can link to a single slide.

**Clicker:** presentation remotes work with no setup. Forward and back send PageDown and PageUp (or media-track keys),
the start button (F5 or Shift+F5) goes full screen instead of reloading, and the blank-screen button (`.` or B) goes black.
Holding a button moves one slide only. The browser window you are presenting from must have focus: click it once before you start.

**PDF:** use the browser's *Print → Save as PDF*. You get one slide per page at 1920 × 1080.

## Publishing

The site is served by GitHub Pages from branch `main`, folder `/ (root)`. Pushing to `main` updates it within about a minute.
Keep the hidden `.nojekyll` file.

## Structure

```
index.html              viewer + all 34 slides (each slide is one <section class="slide">)
embed-recreation.html   live illustration on slide 3 (canvas animation)
assets/                 LaTeX equations (eq-*.png), figures, animations (anim-*.gif), CQTS logo
thumbs/                 slide thumbnails for the grid and presenter view
fonts/                  Roboto (self-hosted)
PROMPT.md               prompt for asking an AI assistant to edit or extend this deck
```

## Credits

Exciton figures on slides 17, 19 and 21 are reproduced from M. O. Sauer & T. G. Pedersen, *Phys. Rev. B* (2022), arXiv:2110.14428.
The electronic-structure figures and animations are computed from the four-band continuum model (γ₀ = 3.0, γ₁ = 0.40, γ₃ = 0.30 eV).
Equations are typeset with LaTeX.
