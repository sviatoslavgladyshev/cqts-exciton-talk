# From exciton geometry to applications: context and next steps

Sviatoslav Gladyshev · for discussion with Dr. Marwa Mannai · CQTS, NYU Abu Dhabi · November 2026
Companion to the talk *A Tale of Two Valleys: The Hidden Geometry of Excitons* (slides 3–5 and 20) and to `RESULTS_SUMMARY.md`.

## What we have
A four-orbital lattice model of AB bilayer graphene at U = 100 meV, with a finite-Q Bethe–Salpeter calculation (both valleys, four transitions per k, static layer-resolved RPA screening, singlet exchange) and gauge-covariant non-Abelian Wilson loops.

The results:
- The lowest exciton is at 70.0 meV, bound by 22.8 meV below the discrete-grid threshold.
- The lowest doublet is degenerate to about 10⁻⁹ eV.
- The curvature eigenvalues of the doublet are λ± ≈ ±7.3 × 10² Å² near Q = 0, and their eigenvectors are K- and K′-polarized.
- The trace of the curvature vanishes locally.
- The individual exchange-mixed branches have curvature compatible with zero at the off-centre points tested.

What we have not shown: a global exciton invariant, edge states, or any transport or optical response. The applications below are research directions only.

## How the experiments connect to this work

| Work | Kind | Material | What it shows | Connection to us | What it is not |
|---|---|---|---|---|---|
| Shang et al., *Nat. Mater.* (2026); briefing by Zúñiga-Pérez & Malpuech | Experiment | WS₂ monolayer on SiN/SiO₂ waveguide cavities | Spin-polarized polariton currents over 92 ± 1 µm at room temperature. Non-resonant pumping, circular polarization above 75 %, and an eight-domain optical-spin-Hall texture. Dark (out-of-plane) excitons feed coherent quasi-TE + quasi-TM modes. | Excitons can carry spin/valley information over long distances, and dark excitons can matter in a device. This is the strongest motivation for asking how an exciton's internal geometry affects its motion. | The texture comes from photonic TE–TM splitting (spin–orbit coupling of light). It is not exciton Berry curvature, and the material is not bilayer graphene. |
| Shi et al., *Nat. Mater.* 24, 56 (2025) | Experiment | FAPbBr₃ perovskite microcavity | Room-temperature optical spin Hall transport over 60 µm, a polariton NOT gate and a spin-polarized beam splitter. | A demonstrated spin-dependent logic function built from exciton-polaritons. | Photonic spin–orbit coupling, not excitonic geometry. |
| Jin et al., *Nat. Commun.* 15, 10563 (2024) | Experiment | Patterned perovskite valley-Hall lattice | Valley-polarized topological kink states (gap ≈ 9 meV) whose K and K′ states counter-propagate at room temperature. | Valley-dependent routing is technologically attractive, and our K/K′ curvature has the same valley-contrasting sign structure. | The topology belongs to an engineered photonic lattice, not to excitons in BLG. |
| Helmrich et al., *Nature* 654, 361 (2026) | Experiment | Dual-gated AB bilayer graphene in a THz bow-tie cavity | The gap is tuned through a cavity at about 2.3 THz, with ultrastrong coupling g/ω_c ≈ 40 %. A cavity-induced, exciton-like bound state is pulled out of the electron–hole continuum. | Bilayer graphene has already been integrated with a cavity, and its gap is gate-tunable in situ. | It is not our exciton. The binding is photon-mediated, at meV-scale gaps and 5–50 K, and no Coulomb-bound excitons were resolved. Our lowest exciton (70 meV ≈ 17 THz, λ ≈ 17.7 µm) is in a different spectral range. |
| Duarte et al., *Phys. Rev. B* 111, 075411 (2025) | Theory | Biased BLG in an optical microcavity | Exciton-polariton dispersions, Hopfield coefficients and Rabi splittings, all tunable by the bias, with strong coupling for realistic exciton lifetimes. Their Fig. 4 uses V_g = 100 meV, the same bias as our model. | This is the most direct device architecture for our material. It can be redone with our excitonic eigenstates in place of a fitted Elliott model. | It is a prediction, with no exciton geometry. |
| Tassan et al., *Light Sci. Appl.* 15, 65 (2026) | Experiment | π-conjugated polymer in silicon-photonics grating cavities | Room-temperature polariton transistor with a 2 × 2 µm² footprint, picosecond switching and amplification up to 60×. | Polariton nonlinearities can be integrated on a chip. | It uses polaritons, not bare excitons, and is not topological. |
| Jiang et al., *ACS Nano* 19, 32123 (2025) | Experiment | 2D monolayer with nanoengineered exciton–photon coupling | Fast, guided, directed exciton drift, and an optoexcitonic switch under ambient conditions. | Neutral excitons can be transported and gated in a device. | It is not topological, and not graphene. |
| Thompson et al., *Nat. Commun.* 16, 11448 (2025) | Theory | Organic polyacene chains | Topological excitons are larger and more dispersive, which enhances diffusion up to about 4×. The quantum metric can be probed with non-uniform fields. | A conceptual bridge from exciton quantum geometry to transport. | It has not been observed, and it is not bilayer graphene. |

## Future computational steps

### Direction A: valley-dependent exciton transport
1. **Valley polarization at every map point.** Store it alongside `lattice_local_map.npz`; at present the valley assignment is documented only at Q = 0.
2. **Larger Q region, same method.** Compute F_xy (the 2 × 2 matrix) and the doublet energies E₁,₂(Q) out to where the doublet stops being isolated. Find where exchange splits the two states.
3. **Non-Abelian wavepacket dynamics.** Use the semiclassical equations for a degenerate (or nearly degenerate) doublet, with Q̇ = F/ħ, a group velocity from E(Q), and an anomalous term from the matrix-valued curvature. The packet's internal state is evolved by the Berry connection plus the exchange splitting. The output would be the sideways displacement per unit force and travel distance, given as a model estimate.
4. **A realistic force on a neutral exciton.** Candidates are an in-plane gradient of the gate field (Stark shift through the polarizability), strain, or a patterned dielectric environment. Each needs its own coupling and an estimate of the achievable gradient.
5. **Intervalley coherence and relaxation.** Exchange already mixes K and K′. Phonon and disorder scattering need to be added, and the drift must outrun these times for the effect to survive.
6. **Global question.** Compute the Wilson-loop spectrum on closed paths and a valley-resolved invariant over the exciton Brillouin zone, to decide whether any of this is topological rather than local geometry.

### Direction B: electrically tunable BLG exciton-polaritons
1. **Optical transition dipoles** of the lowest states on the refined grid (at present they exist only on the 456-point check grid), resolved by polarization and valley.
2. **Light–matter coupling g** for a specified cavity (planar mirror or photonic crystal) at the mid-infrared exciton energy, then the Rabi splitting compared with the exciton and cavity linewidths.
3. **Detuning and Hopfield mixing** as functions of U, done by sweeping U in the BSE. This also gives λ(U), which is needed anyway.
4. **Losses.** Radiative and non-radiative exciton linewidths, plus cavity Q. Compare the results with the strong-coupling criterion used by Duarte et al.
5. **Polarization response.** Ask whether the polaritons inherit any valley-contrasting geometry, weighted by their excitonic Hopfield fraction, and whether this appears in circular-polarization-resolved spectra.

### Common prerequisites
- **λ(U) sweep**, linked to the published dark–bright crossing.
- **Sensitivity studies** for κ, r₀, the RPA angular sampling and the gate geometry.
- **Repeats on the 1980-point grid** for the bias-reversal and exchange-off checks.
- **Beyond the current approximations:** GW, dynamic screening, triplets and spin–orbit coupling, before comparing with experiment.

## Proposed wording for the application claim
"Room-temperature polariton experiments already route spin and valley information over tens of microns, and bilayer graphene has been coupled ultrastrongly to a cavity. Our calculation shows that the lowest excitons of biased bilayer graphene carry substantial valley-contrasting non-Abelian Berry curvature. Whether this geometry can be used to steer excitons or polaritons is an open question that we propose to study."
