# Exciton Berry curvature in biased AB bilayer graphene: results summary

For the talk *A Tale of Two Valleys: The Hidden Geometry of Excitons*.

Sviatoslav Gladyshev · for review by Dr. Marwa Mannai · CQTS, NYU Abu Dhabi · November 2026

**Question.** Can we have topological excitons in biased bilayer graphene? That is, do the exciton states carry Berry curvature or topology as functions of their own centre-of-mass momentum Q, separately from the known valley Chern numbers of the electrons?

## Model (assumed parameters, not a specific device)

- Four-orbital tight-binding model (A₁, B₁, A₂, B₂) over the whole Brillouin zone, with γ₀ = 3.0, γ₁ = 0.40, γ₃ = 0.30 eV, a = 2.46 Å and layer potentials ±U/2 with U = +0.100 eV.
- Finite-Q Bethe–Salpeter equation in the Tamm–Dancoff approximation for spin singlets. It includes both valleys, two valence and two conduction bands (four transitions per k), direct attraction, and exchange with 19 G vectors (37 checked).
- Static, layer-resolved RPA screening computed from the same electronic states, in a dielectric κ = 4.5, with layer spacing 3.35 Å and a Gaussian orbital form factor r₀ = 0.6 Å.
- Pair coordinate: electron at k + Q/2, valence state at k − Q/2 (symmetric centre). Orbital embedding τ = (0, δ₁, δ₁, 2δ₁).
- Geometry: gauge-covariant exciton overlaps that include the conduction and valence Bloch overlaps. These enter non-Abelian Wilson loops for the lowest two-state subspace, giving λ(𝓕ₓᵧ) ≈ −arg eig(𝒲)/δQ², with 𝒜 = i⟨X|∇X⟩, the gradient taken in Q.

## Results (numerical model, Q = 0 unless stated)

| Quantity | Value | Run |
|---|---|---|
| Lowest exciton excitation | 70.0 meV (70.016) | 1980 BSE k, RPA 5712 k |
| Discrete-grid e–h threshold | 92.8 meV (92.790) | same |
| Binding energy relative to that threshold | 22.8 meV | same |
| Splitting of the lowest doublet | 1.3 × 10⁻⁹ eV | same |
| Gap from the doublet to the third state | 9.32 meV at Q = 0; 9.25 meV including the δQ = 1.5 × 10⁻³ Å⁻¹ loop corners; ≥ 9.03 meV over the local map | same; map on 864 k |
| Curvature eigenvalues of the doublet | λ± ≈ ±7.3 × 10² Å²; ∓733.85 Å² at δQ = 3.75 × 10⁻⁴ Å⁻¹ | 1980 k, RPA 7 |
| Valley polarization of the eigenvectors | +0.99991 (λ₋, K) and −0.99991 (λ₊, K′) | same |
| Trace λ₊ + λ₋ on the local map | ≤ 5.8 × 10⁻⁹ Å² | 864 k |
| Single exchange-mixed branches, off-centre | \|Ω\| ≤ 3.5 × 10⁻⁷ Å² (compatible with zero) | 864 k map |
| Bias reversal U → −U | same pair {−771.3, +771.3} Å²; valley assignment swapped | 456 k only |
| Exchange switched off | ±764.8 Å² (vs ±771.3), polarization 0.999998 | 456 k only |

Convergence of |λ| at δQ = 1.5 × 10⁻³ Å⁻¹: 771.3 (456 k) → 741.5 (864 k) → 735.9 (1980 k). Shrinking the loop at 1980 k gives 735.9 → 734.9 → 733.8 Å².
Gauge checks: random electronic phases change λ by 6 × 10⁻¹⁰ Å²; random U(2) rotations by about 10⁻⁹ Å². The Wilson loops rebuilt independently from the stored overlap matrices agree to 6 × 10⁻¹⁰ Å².

## Interpretation

- **Shown, in this model.** The lowest exciton doublet has substantial, valley-locked non-Abelian Berry curvature near Γ: the K-like and K′-like combinations carry opposite curvature, and the bias reverses which valley carries which sign. The individual energy eigenstates are nearly equal K/K′ mixtures because of exchange, and their curvature is near zero. The geometry lives in the doublet, not in a single branch.
- **Not shown.** A net Chern number: the trace vanishes locally, so the eigenvalues are opposite as time reversal suggests. A global exciton invariant: only |Qₓ|, |Q_y| ≤ 0.008 Å⁻¹ was computed (under 0.7 % of Γ–K even at the corners). Exciton edge states and topological or anomalous transport.
- **Proposed wording.** “Our calculations reveal substantial, valley-contrasting non-Abelian excitonic Berry curvature in a model of biased bilayer graphene. Whether this leads to a nontrivial global excitonic topological phase or measurable anomalous transport remains an open question.”

## Caveats to check

1. **Approximations.** No GW, no dynamic screening, no BSE coupling beyond Tamm–Dancoff, no triplets or spin–orbit coupling, no phonons or disorder, no full G,G′ dielectric matrix (RPA averaged over 6 directions), no calibrated device environment. Convergence within the model is not agreement with experiment.
2. **The k grid is not converged to the last digit.** |λ| still moved by 5.5 Å² between 864 and 1980 points, and no extrapolation was made.
3. **The discrete threshold is not monotonic in the grid** (93.20 → 93.51 → 92.79 meV for 456/864/1980 k). So the binding energy carries a grid uncertainty of order 0.5 meV, and it is defined relative to the grid minimum, not the true band minimum of the model.
4. **The map is coarse.** It covers 5 × 5 points on the 864-point grid: 741 Å² at the centre and 312–483 Å² elsewhere. The profile between points is not resolved, and a finite loop averages the flux.
5. **Convention dependence.** Phase and U(2) invariance were verified. Dependence on the pair coordinate (centre vs electron vs hole) and on the orbital embedding was not tested.

## Missing datasets, scripts and validation steps

- **Valley polarization at each map point.** It is not stored in `lattice_local_map.npz`, so the valley assignment is documented only at Q = 0.
- **Refined-grid repeats.** The bias reversal, exchange-off comparison, electronic-phase test and optical dipole strengths exist only on the 456-point grid; none was repeated on the 1980-point grid.
- **Field dependence.** There is no λ(U) sweep, so no field dependence and no link to the published dark–bright crossing.
- **Full exciton Brillouin zone.** There is no Q map over the full exciton BZ, no Wilson-loop spectrum on closed paths, and no valley-resolved invariant.
- **Sensitivity studies.** None for κ, the orbital radius r₀, the RPA angular sampling or the gate geometry.
- **Large-plaquette map.** `lattice_map_map.npz` contains a 4 × 4 map with very large single-branch values (about 10⁵ Å² where links are about 10⁻⁸). It is not described in the reports and is not used in the talk, except for its exciton energies along Q_x.
- **Notebook not reviewed.** `lattice_research.ipynb` was not reviewed for the talk. The figures were regenerated from the `.npz` and `.json` outputs with `tools/make_result_figures.py`.

## Questions for discussion

1. Which closed-path or full-zone calculation would be the convincing test of a global exciton invariant?
2. Should the next run sweep U, or improve the screening and quasiparticle levels first?
3. Which observable fits a time-reversal-symmetric system: valley-selective drift under valley-polarized excitation, or edge or domain-wall spectra?
