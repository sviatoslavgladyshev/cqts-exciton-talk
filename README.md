# A Tale of Two Valleys: The Hidden Geometry of Excitons

Can we have topological excitons in biased bilayer graphene?

Research symposium talk by **Sviatoslav Gladyshev**, supervised by **Dr. Marwa Mannai**,
Center for Quantum and Topological Systems (CQTS), NYU Abu Dhabi.

A self-contained HTML slide deck with its own viewer: no build step, no framework, no internet needed once downloaded.

The main talk is slides 1 to 22, for 20 minutes, and slide 23 lists the sources. It opens with exciton and polariton devices that exist today (slides 3–5, including the WS₂ spin-current experiment of Shang et al. 2026 and bilayer graphene in a terahertz cavity), presents completed calculations of exciton Berry curvature in a lattice finite-momentum Bethe–Salpeter model (13–19), proposes two application directions (20), then one slide on Ateno (21) and the conclusion (22).
Slides 24 to 57 are backup slides: A electronic derivations, B exciton mathematics, C results methods and checks, D the earlier proposal and device slides. Slide 24 links to each part.
Speaker notes for every slide, with timings, are also in `docs/SPEAKER_NOTES.md`.

## View it

- **Online:** <https://sviatoslavgladyshev.github.io/cqts-exciton-talk/>
- **Locally:** run `python3 -m http.server` in this folder and open <http://localhost:8000>.
  You can open `index.html` directly too, but some browsers block the live illustration on slide 9 from `file://`.

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
| **P** | Switch between Viewer and Presenter (also the switch in the toolbar) |
| **D** | Settings: choose a display, reset the displays, turn automatic full screen on or off |
| **R** | Phone or tablet remote: scan the QR code |
| **S** | Presenter: send the slides back to the projector (after it was unplugged) |
| **E** | Erase the drawing on this slide |
| **B** or **.** | Black screen; any key brings the slide back |
| **?** | Keyboard shortcuts |
| Esc | Close the grid, notes or shortcuts |

Click the right part of a slide to go forward and the left third to go back. On a phone, swipe.
Move the pointer to bring up the toolbar, and hover over its timeline to preview any slide. In Presenter, click the timer to pause it; notes size is in Settings.
The address bar keeps the slide number (`#12`), so you can link to a single slide.
You can refresh at any time: the mode, slide, timer, notes size and a running slides window all carry on. A new tab keeps the mode, but starts its own timer.

**Presenting with a projector or second monitor:** set it to *Extended* in System Settings → Displays (not mirrored), open the site in
Chrome or Edge, and press **P** or choose *Presenter* in the toolbar. The first time, click *Find second display* and allow access to your displays.

- **Presenter:** this window stays where it is and shows your notes, timer and next slide. The slides open in a new window on the other display, with no toolbar; your first click, key or clicker press fills it without changing slide. Browsers need that one press; turn it off under *Settings* to keep the slides in a window. With one screen, the window simply switches layout.
- **Viewer:** just the slides. Switch back with **P** or *Viewer*, which also ends the show on the projector.
- **Projector unplugged and plugged back in:** the slides go back to it by themselves; if the browser does not allow that, the next key or clicker press does it. *Send slides to display* in the presenter header, or **S**, does the same by hand. No need to leave Presenter.
- **D** or the *Settings* button changes which display gets the slides at any time, even mid-talk. *Reset displays* closes the slides window and detects the screens again, with no need to reload the page.

Safari and Firefox cannot move windows between displays: choose Presenter, drag the slides window onto the projector, then click it and press **F**.

**Phone, tablet or Apple Watch:** press **R** and scan the QR code. Connected remotes appear in that sheet, in Settings and at the top of the presenter screen. The phone gets Next, Back, Black screen, a laser pointer (drag on the slide preview), the current slide and your notes, and *Draw · Point*: a full-screen pad (turned on its side on an upright phone, about three times the area) with laser, pen in four colours, Undo and Clear. Drawings appear on the projector and stay on their slide until cleared,
on Wi-Fi or mobile data with no app. The Apple Watch uses two iPhone Shortcuts; the steps and addresses are under *Apple Watch* on the phone page.
The site is static, so phone and computer talk through public relays on a private random channel: first public MQTT brokers (HiveMQ and EMQX, both at once, no daily limit), and [ntfy.sh](https://ntfy.sh) as the fallback and for the Apple Watch. The remote stays off until you open it,
and only commands, pointer positions and pen strokes are sent. The computer answers every command with the slide now showing; a command with no answer in 1.5 s is sent again through the other relay, and the phone shows *Reconnecting…* if the computer stops answering. Links that went quiet (a phone that slept, a network change) are reopened automatically. Keep the QR code private, since anyone with it can change slides; *New code* cancels the old one.
ntfy.sh allows 250 messages a day per network, but it is now only the fallback; keep a keyboard or clicker as a backup anyway.

**Clicker:** presentation remotes work with no setup. The clicker has its own indicator on the presenter screen, separate from remotes, which turns to *Clicker detected* at the first press of a clicker-style key (PageDown, PageUp, F5 or a media key). Clickers that send arrow keys are recognised by their very brief presses. If yours is not, use *Detect* in Settings: pick it from Chrome's USB list, or press forward on it when asked. Forward and back send PageDown and PageUp (or media-track keys),
the start button (F5 or Shift+F5) goes full screen instead of reloading, and the blank-screen button (`.` or B) goes black.
Holding a button moves one slide only. In Presenter mode the clicker works without any extra click. In other modes, click the browser window once so it has focus.

**PDF:** use the browser's *Print → Save as PDF*. You get one slide per page at 1920 × 1080.

## Publishing

The site is served by GitHub Pages from branch `main`, folder `/ (root)`. Pushing to `main` updates it within about a minute.
Keep the hidden `.nojekyll` file.

## Structure

```
index.html              viewer + all 57 slides: 22 in the talk, references, 34 backup (each slide is one <section class="slide">)
embed-recreation.html   live illustration on slide 9 (canvas animation)
remote.html             phone and tablet remote
assets/                 LaTeX equations (eq-*.png), figures, animations (anim-*.gif), CQTS logo
thumbs/                 slide thumbnails for the grid and presenter view
fonts/                  Roboto (self-hosted)
latex/                  LaTeX source of added equations (results-equations.tex for the results section)
tools/                  make_result_figures.py (plots from the calculation outputs), make_equations.py (renders eq-r-*.png)
docs/                   talk script, speaker notes, changelog, results summary for review, applications context and next steps
PROMPT.md               prompt for asking an AI assistant to edit or extend this deck
```

## Credits

Exciton figures (dark-bright, anti-aligned and exciton-band slides) are reproduced from M. O. Sauer & T. G. Pedersen, *Phys. Rev. B* 105, 115416 (2022), arXiv:2110.14428.
The electronic-structure figures and animations come from the author's continuum models (γ₀ = 3.0, γ₁ = 0.40, γ₃ = 0.30 eV) and are working calculations, not independently validated.
The exciton Berry-curvature figures (`assets/res-*.png`) are generated by `tools/make_result_figures.py` directly from the output files of the author's lattice BSE calculation (`BLG_multiband_Berry/`, kept outside version control): `python3 tools/make_result_figures.py path/to/BLG_multiband_Berry`.
Figures from other work on the application slides: polarization maps from the *Nature Materials* research briefing on Shang et al. (2026), © 2026 the authors, not openly licensed (`assets/ext-shang-*`);
terahertz spectra from Helmrich et al., *Nature* 654, 361 (2026), arXiv version, CC BY 4.0 (`assets/ext-helmrich-*`); polariton dispersion from Duarte et al., *Phys. Rev. B* 111, 075411 (2025), arXiv:2502.06640, CC BY 4.0 (`assets/ext-duarte-fig4.png`).
Equations are typeset with LaTeX.
