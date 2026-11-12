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
