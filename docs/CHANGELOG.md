# Changelog — second revision (November 2026)

## Slides
- **13 · What was computed:** the pipeline boxes pop in one by one and each arrow draws itself after its box; a dot then keeps travelling along every arrow while the slide is showing.
- **14 · Exciton energies:** redesigned as one large energy ladder drawn to scale (continuum, next states, the lowest pair), with the binding energy (22.8 meV) and the gap (9.3 meV) on animated brackets, and a card with the exciton bands E(Qₓ) drawn in from the 864-point data. Replaces the static level PNG and the list of numbers.
- **15 · Exciton Berry curvature:** the two maps are now 5 × 5 tiles built in the slide from `lattice_local_map.npz`, popping in from the centre outwards; plain-language text (opposite signs in the two valleys, near Q = 0 only, computed as a pair). Map titles still read “Non-Abelian curvature eigenvalue λ₋ / λ₊”. Notes start with a plain spoken version; the technical text follows for questions.
- **19 · Ateno AX:** moved from the end of the backup into the main talk, just before the conclusion (0:30). New dark design with the chip render, a Gaussian-splat video and map pictures from the Ateno website (`assets/ateno/`). The appendix loses section E.
- Timing: results validation and conclusion 0:45 each, so the main talk still adds up to 20:00. Slides from 19 on are renumbered; main talk 1–20, sources 21, backup 22–53.
- Build-in engine: new `wipe` (draws in from the left) and `drop` effects, fractional order numbers; videos restart when their slide is entered.

## Presenting
- **Projector reconnect:** in Presenter mode, when a display is unplugged and plugged back in, the slides window is moved back onto it automatically; if the browser refuses, the next key or clicker press does it. New *Send slides to display* button in the presenter header and key **S**.
- **Phone remote reliability:** commands now go over two public MQTT brokers at once, with ntfy.sh only as a fallback (its 250-messages-a-day limit per network was the main cause of the remote dropping out). Every command is acknowledged by the computer with the current slide; unanswered commands are resent once through ntfy. Dead links after the phone sleeps or changes network are detected and reopened.
- **Drawing:** *Draw · Point* on the phone opens a full-screen pad, turned sideways on an upright phone (about 3× the area of the preview), with laser, pen in four colours, Undo and Clear. Ink appears on the projector and the presenter view and stays on its slide; **E** clears it from the keyboard.

## Checks
- Every slide rendered at 1920 × 1080 with no overflow and no console errors; interaction tests pass (navigation, grid, notes, presenter, links, animation, remote).
- Remote tested end to end on the real relays: with MQTT, and with MQTT blocked on the phone (ntfy fallback); both move the deck in under 1.2 s and keep two phones in step. Pen strokes, Undo and Clear arrived in 4 of 4 runs.

---

# Changelog — results revision (November 2026)

The talk no longer proposes an exciton Berry-curvature calculation; it presents the completed lattice finite-Q BSE calculation from `BLG_multiband_Berry/`.
Deck: 53 slides. Main talk 1–19 (20 minutes), references 20, backup 21–53.

## Main talk, new order

| # | Slide | Status | Time |
|---|---|---|---|
| 1 | Title (`cover`) | Rewritten subtitle: the research question | 0:20 |
| 2 | Why excitons? (`why-excitons`) | **Preserved byte for byte** | 0:40 |
| 3 | Excitons are already being routed and switched (`devices-1`) | Moved from 17; new title; prototype and particle-type pills | 1:30 |
| 4 | Topology and geometry are entering exciton physics (`devices-2`) | Rewritten: PolArt, valley polaritons, Thompson et al. as three cards | 1:30 |
| 5 | Four orbitals and one gate-controlled bias (`bbg-hamiltonian`) | **New**: lattice H(k,U) used in the calculation, AB-stacking diagram | 1:15 |
| 6 | A band gap you can dial (`platform`) | Rewritten text: parabolic bands, gap, U = 100 meV; animation kept | 1:15 |
| 7 | Electron Berry curvature and valley Chern numbers flip with the bias (`berry`) | Animation kept; valley-Chern panel and sign table added | 1:30 |
| 8 | The story, in one picture (`recreation`) | **Preserved** (animation and slide unchanged); moved from 3 | 0:45 |
| 9 | A composite boson with its own momentum Q (`composite`) | Q row added (symmetric pair coordinate) | 0:45 |
| 10 | From electron–hole pairs to exciton bands (`bse-main`) | Rewritten with the calculation's equations (k ± Q/2, four transitions, 2K^x) | 1:30 |
| 11 | Bright, dark, and a field-driven crossing (`dark-bright`) | Published figure kept; separate "This work" box added | 1:00 |
| 12 | Can we have topological excitons…? (`question`) | Rewritten divider | 0:15 |
| 13 | Results 1 · What was computed (`res-model`) | **New**: pipeline diagram and parameters | 1:15 |
| 14 | Results 2 · Exciton energies (`res-energies`) | **New**: level diagram from data | 1:00 |
| 15 | Results 3 · Exciton Berry curvature (`res-curvature`) | **New**: λ₋/λ₊ local map from `lattice_local_map.npz` | 1:30 |
| 16 | Results 4 · Why a non-Abelian calculation (`res-nonabelian`) | **New**: M_ST, Wilson loop, single branch vs doublet | 1:15 |
| 17 | Results 5 · Numerical checks (`res-validation`) | **New**: convergence plots and gauge checks | 1:00 |
| 18 | Results 6 · What this does and does not show (`res-meaning`) | **New**: claims and non-claims, conclusion sentence, limitations | 0:45 |
| 19 | Conclusion (`takeaway`) | Rewritten: four-way status, thank you | 1:00 |
| 20 | Sources (`references`) | Added Yu et al. (Wilson loops) and Exciton Berryology | — |

## Backup (21–53)

- **21 Appendix index**: rewritten with sections A–E.
- **A · Electronic derivations (22–31)**: `electron-start` moved here from the main talk; the 9 derivation slides unchanged.
- **B · Exciton mathematics (32–38)**: unchanged, apart from a convention note in the BSE notes (Sauer–Pedersen use k + Q, k; the calculation uses k ± Q/2). `inheritance` (minivalley exciton band) moved here from the main talk.
- **C · Results: methods and checks (39–44)**, all new: interaction model (Π, W, K^d); full convergence tables; validation checks; bias reversal and exchange-off comparison (the optional results slide); single states vs doublet with overlap maps and dispersion; next steps and questions.
- **D · Earlier proposal and context (45–52)**: `three-geometries` (panel c now shows the computed map), `exciton-berry` (labelled *Earlier proposal · superseded*: Abelian, single-band, k + Q convention), `hierarchy`, `drift` (still a proposal), `precedents`, `three-questions`, `bridge`, `roadmap` (labelled as pre-calculation).
- **E · Ateno (53)**: unchanged.

## Removed

- `status` (“What is known, derived and proposed”): it said no exciton curvature had been computed. Its four-way status now lives on slides 18–19.
- `open-questions` (pre-calculation questions for Dr. Mannai): replaced by the new backup slide `bk-next`.
- Thumbnails `status.jpg`, `open-questions.jpg` and the already orphaned `literature.jpg`.

## Added files

- `assets/res-curvature-map.png`, `res-levels.png`, `res-convergence.png`, `res-links.png`, `res-dispersion.png`, `res-numbers.json`: built only from the calculation outputs by `tools/make_result_figures.py`. That script also rebuilds every Wilson loop of the map from the stored raw overlap matrices and stops if they disagree.
- `assets/eq-r-*.png`: 16 new equations, built by `tools/make_equations.py`; their sources are in `latex/results-equations.tex`.
- `docs/SPEAKER_NOTES.md`, `docs/RESULTS_SUMMARY.md`, this file.

## Viewer

- Speaker notes keep paragraph breaks (`white-space: pre-line`) in the notes panel, the presenter view and `remote.html`. No other viewer code changed.
- All 53 thumbnails were regenerated.

## Checks run

- Every slide rendered headless at 1920 × 1080: no element overflows the slide, and there are no console or network errors.
- Keyboard navigation, number jump, the grid (12 chapters), notes, presenter mode, internal links (all `data-go` targets exist), the build-in animations, the exciton animation iframe, all images and the remote page were tested.
