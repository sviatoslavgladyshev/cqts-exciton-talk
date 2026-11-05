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
| **P** | Switch between Viewer and Presenter (also the switch in the toolbar) |
| **D** | Settings: choose a display, reset the displays, turn automatic full screen on or off |
| **R** | Phone or tablet remote: scan the QR code |
| **B** or **.** | Black screen; any key brings the slide back |
| **?** | Keyboard shortcuts |
| Esc | Close the grid, notes or shortcuts |

Click the right part of a slide to go forward and the left third to go back. On a phone, swipe.
Move the pointer to bring up the toolbar, and hover over its timeline to preview any slide. In Presenter, click the timer to pause it; notes size is in Settings.
The address bar keeps the slide number (`#12`), so you can link to a single slide.

**Presenting with a projector or second monitor:** set it to *Extended* in System Settings → Displays (not mirrored), open the site in
Chrome or Edge, and press **P** or choose *Presenter* in the toolbar. The first time, click *Find second display* and allow access to your displays.

- **Presenter:** this window stays where it is and shows your notes, timer and next slide. The slides open in a new window on the other display, with no toolbar; your first click, key or clicker press fills it without changing slide. Browsers need that one press; turn it off under *Settings* to keep the slides in a window. With one screen, the window simply switches layout.
- **Viewer:** just the slides. Switch back with **P** or *Viewer*, which also ends the show on the projector.
- **D** or the *Settings* button changes which display gets the slides at any time, even mid-talk. *Reset displays* closes the slides window and detects the screens again, with no need to reload the page.

Safari and Firefox cannot move windows between displays: choose Presenter, drag the slides window onto the projector, then click it and press **F**.

**Phone, tablet or Apple Watch:** press **R** and scan the QR code. Connected remotes appear in that sheet, in Settings and at the top of the presenter screen. The phone gets Next, Back, Black screen, the current slide and your notes,
on Wi-Fi or mobile data with no app. The Apple Watch uses two iPhone Shortcuts; the steps and addresses are under *Apple Watch* on the phone page.
The site is static, so commands pass through the public relay [ntfy.sh](https://ntfy.sh) on a private random channel. The remote stays off until you open it,
and only commands such as `next` are sent. Keep the QR code private, since anyone with it can change slides; *New code* cancels the old one.
The relay allows 250 messages a day per network, so keep a keyboard or clicker as a backup.

**Clicker:** presentation remotes work with no setup. The clicker has its own indicator on the presenter screen, separate from remotes, which turns to *Clicker detected* at the first press of a clicker-style key (PageDown, PageUp, F5 or a media key). Clickers that send arrow keys look the same as a keyboard, so they work but cannot be detected. Press **D** to test yours. Forward and back send PageDown and PageUp (or media-track keys),
the start button (F5 or Shift+F5) goes full screen instead of reloading, and the blank-screen button (`.` or B) goes black.
Holding a button moves one slide only. In Presenter mode the clicker works without any extra click. In other modes, click the browser window once so it has focus.

**PDF:** use the browser's *Print → Save as PDF*. You get one slide per page at 1920 × 1080.

## Publishing

The site is served by GitHub Pages from branch `main`, folder `/ (root)`. Pushing to `main` updates it within about a minute.
Keep the hidden `.nojekyll` file.

## Structure

```
index.html              viewer + all 34 slides (each slide is one <section class="slide">)
embed-recreation.html   live illustration on slide 3 (canvas animation)
remote.html             phone and tablet remote
assets/                 LaTeX equations (eq-*.png), figures, animations (anim-*.gif), CQTS logo
thumbs/                 slide thumbnails for the grid and presenter view
fonts/                  Roboto (self-hosted)
PROMPT.md               prompt for asking an AI assistant to edit or extend this deck
```

## Credits

Exciton figures on slides 17, 19 and 21 are reproduced from M. O. Sauer & T. G. Pedersen, *Phys. Rev. B* (2022), arXiv:2110.14428.
The electronic-structure figures and animations are computed from the four-band continuum model (γ₀ = 3.0, γ₁ = 0.40, γ₃ = 0.30 eV).
Equations are typeset with LaTeX.
