# Speaker notes — 20-minute talk

Generated from the `<aside>` notes in `index.html` (the same text appears in the presenter view, the **N** panel and the phone remote).
The notes are deliberately fuller than a script (about 4,300 words for the main talk): on the results slides the first paragraph is the plain spoken version, and the rest explains the mathematics and the physics for questions.
Timing cues in brackets add up to 20:00 (slide 2 has no cue in its preserved notes and takes 0:40): introduction 1:00 · motivation 3:00 · bilayer graphene 4:00 · excitons 4:00 · results 6:45 · Ateno 0:30 · conclusion 0:45.

### 1. A Tale of Two Valleys: The Hidden Geometry of Excitons  

[0:20] Title.
The title borrows from Dickens, A Tale of Two Cities: here the two valleys are K and K′, and the hidden geometry is the Berry curvature of the excitons, which, as we will see, comes out opposite in the two valleys.
The question of this talk is in blue: can we have topological excitons in biased bilayer graphene? By that I mean topology or quantum geometry of the exciton states themselves, as functions of the exciton's own centre-of-mass momentum Q, not the well-known topology of the electron bands.
Since the last version of this talk I have carried out the calculation: a finite-momentum Bethe–Salpeter calculation in a four-orbital lattice model, followed by a non-Abelian Berry-curvature calculation for the lowest exciton states. So today the second half of the talk presents actual model results.
Throughout I will keep four things apart: established electronic topology, published exciton physics, my own numerical model results, and what is still open. The work is supervised by Dr. Marwa Mannai at CQTS, NYU Abu Dhabi.

### 2. Why excitons?  

An exciton is an electron and a hole bound together, so it carries energy but no net charge. That makes it hard to steer with an ordinary voltage. Our hypothesis is that the geometry of the exciton band gives another handle on its motion, and that hypothesis is untested here.

### 3. Excitons are already being routed and switched.  

[1:30] Why should anyone care whether excitons have band geometry? Because excitons are already being used to carry and switch signals.
Left: the University of Michigan optoexcitonic switch. These are bare excitons: neutral electron–hole pairs that are guided and gated in a nanoengineered structure at room temperature. It is a working prototype. It is not topological and not bilayer graphene.
Right: the integrated polariton transistor from IBM Research Zurich and collaborators. This is a different particle: an exciton-polariton, an exciton strongly mixed with a cavity photon. The device switches in picoseconds with gain, on a silicon-photonics platform. Again a working prototype, but polaritonic, not topological.
Message: excitons carry energy and information without net charge. That makes them attractive for low-loss optoelectronics, but also hard to steer with a voltage. Band geometry is one candidate handle. None of these devices demonstrates topological exciton transport in biased bilayer graphene.

### 4. Topology and geometry are entering exciton physics.  

[1:30] Three more examples, now closer to topology and geometry. The pills say what each one is: development project, experiment or theory; and which particle: polaritons or bare excitons.
PolArt is a European research project building neuromorphic hardware from polariton microcavities. It is in development, not a product.
The perovskite experiment of Jin et al. shows topological valley kink states of exciton-polaritons at room temperature, with a gap of about 9 meV. This is an experiment, but with polaritons, in a patterned photonic lattice, not with bare excitons in bilayer graphene.
Thompson et al. is a theory prediction for bare excitons: the quantum geometry of the exciton band can enhance diffusion. It is not an experiment and not protected edge transport.
Together: geometry and topology are becoming useful words for exciton and polariton transport. But none of these is a demonstration of topological exciton transport in biased AB bilayer graphene. That gap is what motivates our calculation: first find out whether the exciton states there have geometry at all.

### 5. Four orbitals and one gate-controlled bias.  

[1:15] The electronic starting point. AB bilayer graphene has four carbon sites per unit cell: A1 and B1 in the top layer, A2 and B2 in the bottom layer. B1 sits directly above A2, and that pair forms the strong vertical dimer bond γ1 = 0.4 eV. γ0 = 3 eV is the usual in-plane hopping, and γ3 = 0.3 eV is the skew hop between the two non-dimer sites, which causes trigonal warping.
A perpendicular electric field is represented by a layer potential: +U/2 on the top layer and −U/2 on the bottom layer. That is the only place the gate enters the model.
The matrix is written with the lattice structure factor g(k), the sum over the three nearest-neighbour vectors. This form is valid across the whole Brillouin zone, which the exciton calculation needs because the screening and exchange sums run over the entire zone, including both valleys K and K′. Near K, g is approximately −(√3a/2)(px − i py), and the matrix reduces exactly to the continuum Hamiltonian used in my earlier analytic work. The code checks this numerically to 10⁻¹¹ eV. The full continuum derivations are in Appendix A.
This is the established tight-binding model of McCann and Koshino; the parameter values are standard, not fitted to a device.

### 6. A band gap you can dial.  

[1:15] The bands. Without bias the two low-energy bands touch at K and K′ and are approximately parabolic, with effective mass m* ≈ γ1/2v², because the dimer orbitals are pushed away to ±γ1. γ3 adds trigonal warping very close to the touching point (Appendix A).
Switching on U opens a gap. The formula on the slide is the leading-order two-band result: E ≈ ±√(U²/4 + (ħ²p²/2m*)²). The full four-band result has a slight Mexican-hat shape, so the band edge sits on a small ring rather than exactly at K; the animation, from the four-band model, shows this as U sweeps up to 300 meV and back.
Published DFT gives gaps up to about 300 meV at strong fields (Sauer and Pedersen). For the exciton calculation I fix U = 100 meV. In the discretized model the lowest electron–hole pair energy at Q = 0 is about 93 meV, which will be the continuum threshold in the results.
Key point for later: the conduction and valence states near K and K′ are what the exciton is built from, so their energies and their wavefunctions both matter.

### 7. Electron Berry curvature and valley Chern numbers flip with the bias.  

[1:30] Electronic topology, which is established physics; I re-derived it as my starting point.
The Berry curvature Ω(k) of the conduction band acts like a magnetic field in momentum space. The animation shows it in both valleys as U sweeps from +100 to −100 meV: it is concentrated near the band edge, it has three lobes because of trigonal warping, it is opposite in K and K′ by time reversal, and it flips sign when the bias reverses.
Integrating it over one valley gives the valley Chern number. For the conduction band, C(K) = −sgn U and C(K′) = +sgn U (two-band model, Appendix A, which also shows that trigonal warping does not change the result). So the total Chern number is zero — there is no quantum anomalous Hall effect — but the valley difference is ±2 and reverses with the gate. This is the origin of valley Hall physics and of topological kink states at domain walls in bilayer graphene.
Important for what follows: these are properties of single electrons. They do not tell us the Berry curvature of an exciton as a function of its own momentum Q. That has to be computed separately, and that is what I did.

### 8. The story, in one picture.  

[0:45] This is my existing animation, unchanged: a cartoon, not a calculation.
Light creates an electron in the conduction band and leaves a hole in the valence band. Coulomb attraction binds them into an exciton, a neutral composite that moves as one object.
The picture draws the electron in the top layer and the hole in the bottom layer for clarity. In the real calculation each exciton state is a superposition of many electron–hole configurations, including both layers and both valleys.
The sideways bend at the end is the question we want to answer: does the exciton band have Berry curvature that could deflect it? The next slides set up how to compute that.

### 9. A composite boson with its own momentum Q.  

[0:45] What kind of particle is an exciton? Two fermions bound together. At low density, when the pairs do not overlap, they behave approximately as bosons; at high density the fermionic constituents matter again.
A bare exciton is just the electron–hole pair; that is what this talk is about. An exciton-polariton additionally mixes in a cavity photon, so its dispersion, mass and lifetime are different. The device examples earlier were mostly polaritons.
The crucial new variable is Q, the centre-of-mass momentum of the pair. In my calculation I use the symmetric convention: the electron sits at k + Q/2 and the valence state is at k − Q/2, so the pair carries total momentum Q while k labels the relative motion. Each exciton state is a band E_S(Q), and exciton topology means Berry curvature and Chern numbers in Q, not in the electron momentum k.
Bosonic statistics alone gives none of condensation, topological order or protected transport.

### 10. From electron–hole pairs to exciton bands.  

[1:30] The method that turns electron bands into exciton bands.
First line: an exciton state at centre-of-mass momentum Q is a superposition of electron–hole pairs. c† creates an electron in conduction band c at k + Q/2; c removes an electron from valence band v at k − Q/2, which leaves the hole. The coefficients A are the exciton envelope in the space of pairs. In my calculation there are two conduction and two valence bands, so four transitions at every k, and k runs over the whole Brillouin zone, so both valleys are in the same matrix.
Second line: the Bethe–Salpeter equation in the Tamm–Dancoff approximation. The diagonal is the pair energy E_c(k+Q/2) − E_v(k−Q/2). K^d is the direct term: the screened Coulomb attraction between electron and hole, which binds them. K^x is the exchange term: the electron–hole pair annihilating and re-creating, which is repulsive; the factor 2 is for spin singlets. Exchange can transfer the pair between valleys, so it couples K and K′ excitons.
Output: exciton energies E_S(Q) — the exciton bands — and the weights A. A point to keep in mind: the coefficients A are defined relative to a choice of phase for each electronic Bloch state, so the geometry cannot be obtained from A alone. It needs A together with the Bloch states. I will come back to this in the results.
The structure is the standard one (see ABINIT and Sauer–Pedersen); the specific kernels are in Appendix C.

### 11. Bright, dark, and a field-driven crossing.  

[1:00] Bright and dark excitons; this is published work by Sauer and Pedersen (PRB 105, 115416), a DFT-based Bethe–Salpeter calculation for biased bilayer graphene.
Bright excitons couple to normally incident light; dark ones do not. In the rotationally symmetric picture the band pseudospin contributes angular momentum ∓2 in K and K′, so a 1s exciton has total angular momentum ±2 and is dark, while light needs ±1; trigonal warping relaxes this weakly (Appendix B).
Their figure shows the absorption spectrum at fields from 60 to 300 mV/Å. At low field the lowest exciton is mostly dark; near 240 mV/Å a bright state crosses below it. The crossing position is nearly the same for suspended and hBN-encapsulated samples. This is their result, not mine.
My own model gives one consistent data point, shown in the box: at U = 100 meV the lowest exciton doublet has only about 0.14 of the dipole strength of the brightest of the six lowest states, on a coarse 456-point check grid. I did not sweep the field, so I make no claim about where a crossing occurs in my model. Note also that their field in mV/Å and my U are not directly interchangeable because of screening.

### 12. Electron valley Chern numbers are established.  

[0:15] Here is the pivot. Electron valley Chern numbers in biased bilayer graphene are established physics. The research question is whether the excitons — the bound, neutral composites — have topology or quantum geometry of their own, in their own momentum Q.
The rest of the talk is my calculation. Six slides: the model, the exciton energies, the curvature result, why it has to be done in a non-Abelian way, the numerical checks, and what it does and does not tell us about topological excitons.

### 13. What was computed.  

[1:15] This is the calculation I carried out. Read the top row left to right.
1. Electronic Hamiltonian: the four-orbital lattice model from the previous section, over the whole Brillouin zone, not just a patch around K.
2. Diagonalize it at every k: energies and Bloch eigenvectors for two valence and two conduction bands, in both valleys. The k grid is non-uniform: it covers the full zone and is much denser around K and K′, because the low-energy valleys are narrow. A coarse uniform grid does not resolve them and gives wrong exciton energies.
3. Build and solve the finite-Q BSE. Four interband transitions per k point. The direct attraction is screened by a static RPA polarization computed from the same electronic states, resolved by layer, so the intra- and interlayer interactions are screened differently. Exchange is included for spin singlets, with 19 reciprocal-lattice vectors (37 checked). The largest problem has 7920 coupled pair states and is solved with a block Davidson method; it was checked against dense diagonalization on a smaller grid.
4. Take the two lowest exciton states. They form a nearly degenerate doublet, well separated from the rest.
5. Compute gauge-covariant overlaps between exciton states at neighbouring Q, multiply them around small squares in Q: Wilson loops.
6. Their eigenphases give the eigenvalues of the 2×2 non-Abelian Berry curvature.
Parameters on the right: standard hoppings; U = +100 meV as the working point; κ = 4.5 a uniform dielectric environment; 3.35 Å layer spacing; 0.6 Å Gaussian orbital radius as a short-distance form factor. These are assumptions of the model, not measured properties of a fabricated device. U is set directly; gates and anisotropic hBN are not modelled.

### 14. Excitons are bound, and come in pairs.  

[1:00] Left: the energy ladder at Q = 0. Right: how the energy changes when the whole exciton moves.
Say it simply: the lowest exciton sits at 70 meV; you need 23 meV more to tear it apart into a free electron and hole; and the lowest level is really two states with the same energy, one from each valley. The next states are 9 meV higher, so this pair is well isolated. On the right, the pair rises as Q grows, like a particle with mass, and the two partners split slightly away from Q = 0 because exchange couples the valleys. The right panel is the 864-point grid, so it starts at 70.8 rather than 70.0.
Details if asked. First result: the exciton energies at Q = 0, from the most refined run — 1980 k points in the BSE, screening computed on 5712 k points.
The lowest exciton lies at 70.016 meV. The lowest free electron–hole pair energy on the same discrete grid is 92.790 meV. So, relative to that threshold, the exciton is bound by 22.77 meV. I quote the threshold of the discretized model deliberately: it is the consistent reference for a binding energy within this calculation. Practically: about 70 meV for the excitation and about 23 meV of binding.
The two lowest states are almost exactly degenerate: their splitting at Q = 0 is 1.3 × 10⁻⁹ eV, a nano-electron-volt, which is numerically zero for our purposes. Physically they are the K-like and K′-like excitons, related by time reversal, mixed by exchange.
The next exciton level is 9.3 meV higher at Q = 0. Including the corners of the standard Wilson loop around Q = 0 (side 1.5 × 10⁻³ Å⁻¹) the minimum separation is 9.25 meV, and over the whole local map it never drops below 9.0 meV. This gap is what makes the doublet a well-defined two-dimensional subspace — the precondition for the curvature calculation.
These are numerical results of the model on the previous slide, with its assumed parameters; they are not measurements and not GW-corrected.

### 15. The lowest excitons curve in opposite ways in the two valleys.  

[1:30] The central result. Plain version first.
Berry curvature measures how the quantum state of the exciton twists as its momentum changes. Here the twist is large, about 730 square ångström, and it has opposite signs in the two valleys: K-valley excitons blue, K′-valley excitons red. Each tile is one point I computed; the strongest twist is at Q = 0, the centre tile, and it stays the same sign across the patch.
Because the two lowest excitons have exactly the same energy, I treat them together as a pair. That gives two curvature values, λ₋ and λ₊, which is what the map titles say.
Technical version, if asked.
For the lowest two-state exciton subspace I compute the 2×2 non-Abelian Berry curvature matrix F_xy(Q). Its two eigenvalues at Q = 0 are approximately −7.3 × 10² Å² and +7.3 × 10² Å². The most refined number — 1980 k points and the smallest Wilson loop, side 3.75 × 10⁻⁴ Å⁻¹ — is ∓733.85 Å². I quote it as 7.3 × 10² because the numerical uncertainty is far larger than the last decimals.
For scale: Berry curvature has units of area; √734 Å² ≈ 27 Å, which is a length of the order of an exciton size in this system. It is large compared with typical electron Berry curvatures near the band edge of strongly gapped materials, but I would not compare magnitudes across definitions without care.
Valley structure: each eigenvalue comes with an eigenvector inside the doublet. Measuring how much of that eigenvector sits in valley K versus K′ gives valley polarizations +0.999912 and −0.999912. So λ₋ belongs to an essentially pure K exciton and λ₊ to an essentially pure K′ exciton. That is what "opposite valley-associated excitonic geometry" means: K-like and K′-like excitons have opposite Berry curvature, as time reversal requires, and the calculation resolves this even though exchange mixes the valleys in the energy eigenstates.
The map: 5 × 5 points with |Qx| and |Qy| up to 0.008 Å⁻¹ — under 0.7 percent of the distance from Γ to K even at the corners. It uses the 864-point grid, hence 741 at the centre rather than 734. The curvature is largest at Q = 0 and falls to 300–480 Å² at the other points; the sampling is too coarse to resolve the profile between points, so I show discrete tiles, not a smooth surface.
Two cautions, written on the slide. These are eigenvalues of a matrix for a two-dimensional subspace, not the curvatures of exciton band 1 and band 2. And this is a local calculation around Γ, not over the whole exciton Brillouin zone.

### 16. Follow the pair, not the individual states.  

[1:15] Why the calculation has to be non-Abelian. This is one of the main messages.
The two lowest excitons are degenerate to 10⁻⁹ eV at Q = 0. Near a degeneracy, the individual energy eigenvectors are not smooth functions of Q: a tiny change of Q can rotate the lowest state into the second one. Sorting states by energy therefore does not follow a single physical branch. The cartoon shows this: the green disc is the two-dimensional subspace, which moves smoothly; the dark arrow, the sorted lowest state, points in very different directions at nearby Q.
The numbers confirm it. Around the smallest loop at Q = 0, the overlap of the sorted lowest state with itself drops to 0.012 — it is almost orthogonal to its neighbour — so its ordinary (Abelian) Berry phase is meaningless there. For the pair as a whole, the smallest singular value of the overlap matrix is at least 0.9996 everywhere on the map: the subspace is transported perfectly well.
So I treat the doublet as one object. The overlap matrix M_ST(Q,Q′) at the top is the correct gauge-covariant overlap between exciton states: the BSE weights A of the two states, times the overlap of the electron Bloch states at k+Q/2 and k+Q′/2, times the overlap of the valence Bloch states at k−Q′/2 and k−Q/2, summed over all band pairs. The raw coefficients A alone are not enough: each A is defined relative to an arbitrary phase of each Bloch state, and those phases only cancel when the Bloch overlaps are included. Differentiating A directly would give a gauge-dependent, wrong answer.
From each M take the closest unitary matrix via the SVD, multiply around a small square: that is the Wilson loop W. With the convention A = i⟨X|∇_Q X⟩, the eigenphases of W divided by the loop area give the eigenvalues of the curvature matrix F_xy. A U(2) rotation inside the doublet changes W and F only by conjugation, so the eigenvalues are basis-independent; this was tested with random U(2) rotations.
Contrast at the bottom: the doublet has eigenvalues of ±7.3 × 10² Å², while the individual exchange-mixed energy branches, away from the central degeneracy, have curvature below 4 × 10⁻⁷ Å² at all tested points — compatible with zero. A natural reading, which I offer as interpretation: exchange makes the energy eigenstates nearly equal mixtures of K and K′, whose opposite curvatures cancel. The geometry lives in the valley-resolved combinations, not in the energy branches. A single-branch number from an earlier one-valley model cannot simply be assigned to either mixed branch.

### 17. Stable under refinement and gauge changes.  

[0:45] How much should we trust 7.3 × 10² Å²?
Panel (a): refining the electronic k grid of the BSE at a fixed loop side of 1.5 × 10⁻³ Å⁻¹. 456 points give 771.3 Å², 864 give 741.5, 1980 give 735.9. The change is 30 Å² for the first refinement and 5.5 Å² for the second, so the scale 7.3–7.4 × 10² Å² is stable, but the value is not converged to the last digit. The exciton energy over the same refinement goes from 71.0 to 70.0 meV.
Panel (b): at 1980 points, halving the loop side twice: 735.9, 734.9, 733.8 Å². A finite Wilson loop measures the average curvature flux through the square; the curvature is peaked at Q = 0, so smaller loops approach the local value at the centre from above. That is why the most refined local estimate, 733.85 Å², is slightly below the fixed-loop numbers.
Right column, the checks. The result is gauge-invariant as it must be: assigning random phases to all electronic Bloch states changes the curvature by 6 × 10⁻¹⁰ Å²; random U(2) rotations of the exciton doublet change the eigenvalues by about 10⁻⁹ Å². Refining the screening grid from level 7 to 8 changes |λ| by 0.002 Å² and the energy by 0.003 meV. Doubling the reciprocal-lattice sum in the exchange changes |λ| by 0.0006 Å². The doublet remains at least 9.0 meV below the third state over the whole map, so the two-state subspace is well defined everywhere it was used. The iterative eigensolver reproduces dense diagonalization on a test grid.
What I do not claim: full convergence of the k grid, and above all that the number survives once the physical approximations — static screening, no GW, Tamm–Dancoff, model orbitals — are removed. Numerical convergence within a model is not agreement with experiment.

### 18. Topological excitons? What this does and does not show.  

[0:45] Back to the question: can we have topological excitons in biased bilayer graphene?
What the model shows. One: the lowest exciton doublet has substantial, nontrivial Berry curvature, with eigenvalues of about ±7.3 × 10² Å² near Q = 0. Two: the curvature eigenvectors are almost purely K or K′, so this is valley-contrasting geometry of the excitons — the exciton analogue of the electron valley structure, but now computed for the bound composite in its own momentum. Three: reversing the bias swaps the valley assignment of the two signs; this was tested once, on a coarser grid.
What it does not show. Four: the trace of the curvature matrix, λ₊ + λ₋, is zero to 6 × 10⁻⁹ Å² over the map. The total Chern number of the doublet is the integral of that trace, so nothing here suggests a net Chern number; opposite eigenvalues are what time reversal leads one to expect. Five: the curvature was computed only in a small square patch around Γ. A global invariant — say a valley-resolved exciton Chern number — would need the curvature over the whole exciton Brillouin zone, with the doublet isolated everywhere, or a Wilson-loop spectrum on closed paths. That has not been done. Six: no edge-state calculation and no transport calculation or measurement exist.
So my answer is the boxed sentence. We have computed substantial, valley-contrasting non-Abelian exciton Berry curvature in a model of biased bilayer graphene. Whether this becomes a nontrivial global excitonic topological phase, or a measurable anomalous transport signature — for example a valley-selective sideways drift when the valleys are populated unequally — remains open.
Footer: the main approximations. No GW, no dynamic screening, no spin–orbit coupling or triplets, no phonons or disorder, no full ab initio dielectric matrix, no calibrated device. I do not claim a topological exciton insulator.

### 19. Ateno AX.  

[0:30] Thirty seconds on Ateno, which I co-founded, before I close. We are building a dedicated chip for on-device 3D mapping based on Gaussian splatting, for warehouses, mines and tunnels, construction and inspection drones. The FPGA prototype renders a 1080p frame of 173,161 Gaussians; per-frame time went from 1.02 s to 262 ms in ten days. Early stage: no silicon yet, tape-out with design partners is next. The common thread with the physics: understand the structure, then put the computation where it is needed.

### 20. Can we have topological excitons in biased bilayer graphene?  

[0:45] To conclude, back to the question on the cover.
Established: the electrons of biased bilayer graphene have valley Chern numbers that reverse with the bias.
Published: the excitons are strongly bound, field-tunable, and bright and dark states cross at strong field (Sauer and Pedersen).
Computed here: in a four-orbital, two-valley, finite-Q Bethe–Salpeter model with RPA screening and exchange, the lowest exciton doublet carries valley-locked non-Abelian Berry curvature of about ±7.3 × 10² Å² near Q = 0, robust to gauge changes and to grid refinement within the model.
Open: whether that local geometry adds up to a global exciton invariant, whether there are exciton edge states, and whether it produces a measurable transport signature.
So: we can say that excitons in this model have substantial valley-contrasting geometry; we cannot yet say they are topological in the strong sense.
Thank you to Dr. Marwa Mannai and to CQTS. I am happy to take questions; derivations, convergence tables and checks are in the appendix.

### 21. Sources.  

Every entry links to its source. Electronic figures come from my own continuum and lattice models with McCann–Koshino parameters; the exciton figures on the published-physics slides are reproduced from Sauer and Pedersen with attribution. All exciton Berry-curvature numbers and plots are from my own lattice Bethe–Salpeter calculation, generated directly from its saved output files.

---

## Appendix (backup, for questions)

### 22. Appendix.  

Stop here in the main talk. These slides are for questions. Click a section title to jump straight to it. Section C holds every number behind the results slides.

### 23. Four bands, then two, with threefold warping.  

We start from the standard four-band model of bilayer graphene and reduce it to two low-energy bands. Skew hopping warps the band edge into a threefold pattern, which matters because excitons are built from these states. This is my own analytic working calculation, and the seven-step derivation is in the appendix.

### 24. The four-band Hamiltonian.  

Basis A1, B1, A2, B2 near valley K. Intralayer Dirac hopping alpha0 pi on the off-diagonal blocks, the dimer coupling gamma1 between B1 and A2, the skew hopping alpha3 between the non-dimer sites, and plus or minus U over 2 on the diagonal. K-prime follows by time reversal. Every result in the next slides is derived from this matrix.

### 25. Eliminating the dimer sites.  

The dimer sites B1 and A2 are pushed to plus or minus gamma1 by the strong interlayer bond. Eliminating them with a Schur complement and expanding to leading order in E over gamma1 gives an effective two-band Hamiltonian on the non-dimer sites A1 and B2. The only second-order path is A1 to B1, across the dimer bond, then A2 to B2, which produces the quadratic term minus alpha0 squared over gamma1 times pi-dagger squared; the skew hop gives the linear alpha3 pi term directly.

### 26. Spectrum and threefold symmetry.  

Writing pi = k e^(i theta), h has two terms with different winding. Their interference gives the cos 3 theta term in |h| squared, which is the analytic origin of trigonal warping. The exact four-band secular equation is quadratic in E squared, and its constant term contains the same cos 3 theta piece, minus 2 gamma1 alpha3 alpha0 squared k cubed cos 3 theta. Because cos 3(theta + 2 pi/3) = cos 3 theta, the spectrum is invariant under 2 pi/3 rotations only: C infinity is reduced to C3. With gamma3 = 0 the angle drops out of the determinant altogether.

### 27. Where the bands touch.  

At zero bias, a band touching requires h = 0. Factoring out k e^(-2i theta) leaves alpha3 e^(3i theta) = beta k. Since k is real and positive, e^(3i theta) = 1, so theta = 0, 2 pi/3, 4 pi/3, at radius k_s = alpha3/beta = 2 gamma1 gamma3 over root 3 a gamma0 squared, about 6.26 times 10^-3 inverse angstrom. Together with k = 0 this gives one central and three satellite Dirac points, plotted on the right.

### 28. Winding numbers, computed.  

Definition: the winding number counts how many times the pseudospin vector d rotates as k goes once around a contour. Without gamma3, d = minus beta k squared (cos 2 theta, sin 2 theta); the numerator of the winding integrand is 2 beta squared k^4 and the denominator beta squared k^4, so w = +2 exactly. With gamma3, near k = 0 the linear term dominates, d is approximately alpha3 (kx, -ky), which rotates clockwise: w = -1. Expanding around the satellite at (k_s, 0), the constant terms cancel because beta k_s = alpha3, and the Jacobian is diag(-alpha3, -3 alpha3) with positive determinant, so w = +1. C3 maps the satellites onto each other preserving orientation. Total: -1 + 3 = +2.

### 29. Watch the pseudospin wind.  

Animation of the winding numbers derived on the previous slide. Left: k goes once around K. Middle: for the quadratic touching (gamma3 = 0), d = -beta k^2 (cos 2 theta, sin 2 theta) turns twice in the same direction: w = +2. Right: near the central Dirac point with gamma3, d is approximately alpha3 (kx, -ky), which turns once the other way: w = -1. The counters show the accumulated winding.

### 30. Berry curvature in closed form.  

For a two-band Hamiltonian d dot sigma, the Berry curvature is minus-plus one half d dot the cross product of its momentum derivatives over |d| cubed. With d = (alpha3 kx - beta(kx^2 - ky^2), -alpha3 ky - 2 beta kx ky, u) the cross product has only a z component, 4 beta^2 k^2 - alpha3^2, and the triple product is u times that. Hence the closed form. Two corollaries: the curvature is odd in U, so reversing the bias reverses the valley Hall response while the energies are even; and the curvature changes sign on the ring k = alpha3 / 2 beta, which is where the lobes in the Berry-curvature animation come from.

### 31. Valley Chern number, integrated.  

Integrate the curvature over the plane at gamma3 = 0, where it is independent of theta. The angular integral gives 2 pi; the radial integral is minus-plus 2 u beta squared times integral of k cubed over (u^2 + beta^2 k^4)^(3/2). Substituting t = beta k^2 turns it into minus-plus u times integral of t over (u^2 + t^2)^(3/2), whose antiderivative is minus 1 over root(u^2 + t^2). Evaluated from 0 to infinity this gives minus-plus u over |u|, so C = minus-plus sgn U. K-prime has the opposite sign by time reversal, so the net charge Chern number vanishes; what survives is a valley Chern number.

### 32. Why γ₃ cannot change it.  

Two independent arguments that trigonal warping leaves the valley Chern number unchanged. First, topological: for nonzero bias the gap 2 root(u^2 + |h|^2) is at least |U| everywhere, so turning on gamma3 is an adiabatic deformation, and the Chern number is fixed by the asymptotic winding, w infinity = 2, giving minus-plus sgn u. Second, local: each massive Dirac point contributes minus-plus w_D over 2 times sgn u. The central point (w = -1) gives plus-minus one half, the three satellites (w = +1) give minus-plus three halves; the sum is minus-plus sgn U, the same answer. These are two-band results; the four-band values remain predictions to be checked with a converged four-band integration.

### 33. The exciton, as an equation.  

Note on conventions: this slide follows the Sauer–Pedersen notation with the electron at k + Q and the hole at k. My own calculation uses the symmetric choice, electron at k + Q/2 and valence state at k − Q/2 (Appendix C). The two labelings are related by a shift of k; the geometry calculation must use one convention consistently, and mine is the symmetric one. The exciton at centre-of-mass momentum Q is a superposition of electron-hole transitions with Bethe-Salpeter coefficients A. The BSE is an eigenvalue problem: band energy differences plus a kernel with a screened direct attraction and a repulsive exchange part. In a bilayer the direct kernel splits into intralayer and interlayer pieces; the interlayer one is softened by the vertical separation 2d of about 3.48 angstroms. The optical matrix element P is a coherent sum of single-transition matrix elements weighted by A, so contributions can cancel (dark) or add (bright). The exciton energy is the gap minus the binding energy.

### 34. Why the ground exciton is dark.  

In the rotationally symmetric continuum picture, the exciton carries total angular momentum m = m_pseudo + m_env, with m_pseudo = -2 in K and +2 in K-prime. Normal-incidence light needs m = plus or minus 1. A 1s envelope has m_env = 0, so m = plus or minus 2: forbidden, dark. A 2p envelope with m_env = plus or minus 1 gives m = plus or minus 1: bright. Trigonal warping reduces C infinity to C3, where angular momentum is only defined modulo 3, and -2 is congruent to +1 mod 3, so the coupling is allowed by symmetry but small, set by the warping strength. That is why the ground state is mostly, not completely, dark. The emission rate goes as |P| squared times sin squared phi, the classical dipole pattern.

### 35. Interlayer, anti-aligned excitons.  

At low field the anti-aligned interlayer configuration dominates: hole bottom, electron top, dipole opposite to the field, because of the bias-induced charge redistribution. As the field grows, intralayer weight increases, the electron-hole overlap and so |P| grow: this links to the dark-to-bright switch. The field controls the layer composition, hence the dipole, of the composite.

### 36. Light-like excitons from exchange.  

Exchange couples the K and K-prime excitons. Its matrix element is proportional to 1/Q times (Q dot p_K star)(Q dot p_K-prime), where p is the interband momentum matrix element at the valley. The numerator is quadratic in Q and the prefactor removes one power, so the coupling is linear in Q, and the splitting 2|<K|v_x|K-prime>| is linear in Q. One combination becomes light-like, E0 + alpha|Q|, with P parallel to Q; the other is particle-like, E0 + hbar^2 Q^2 / 2M, with P perpendicular to Q. For the dark exciton p is approximately zero, so the same formula predicts almost no splitting, which is what the DFT-BSE calculation finds.

### 37. Light cone, lifetime, temperature.  

Radiative decay must conserve energy and in-plane momentum, so only excitons with Q below omega over c can emit directly: the light cone. With hbar omega = 0.2 eV and hbar c = 1973 eV angstrom this is about 10^-4 inverse angstrom, a hundred times smaller than the inter-minivalley scale, so the trigonal anisotropy barely matters for emission. The observable rate is a Boltzmann average over exciton bands and momenta; the lifetime is its inverse. With a dark ground state, tau first drops as bright states are populated above the onset temperature (E3 - E1)/4 k_B, then rises again as excitons spread outside the light cone. The emission angle follows from sin theta = cQ/omega.

### 38. Why τ(T) drops, then rises.  

Schematic with illustrative parameters, not the paper data. Left: dark and bright exciton bands with their thermal populations; the yellow strip is the light cone, exaggerated for visibility. Right: the resulting radiative lifetime. At low T almost everything sits in the dark state, so tau is long. As T rises the bright band is populated and tau drops. At higher T excitons spread to large Q, outside the light cone, and tau rises again. This reproduces qualitatively the non-monotonic tau(T) found by Sauer and Pedersen.

### 39. Minivalleys imprint on the exciton band.  

This is the exciton energy plotted against its own momentum Q. The threefold pattern of the electrons shows up in the exciton band at higher field. But this is only energy, so it says nothing yet about exciton Berry curvature, which is the quantity we want.

### 40. Interaction model used in the calculation.  

Backup: the interaction model. The polarization Π is computed from the same four-band electronic states as the BSE, at T = 0 for the neutral insulator, resolved into the two layers, with a factor 2 for spin; both valleys are already in the full-zone k sum. V is the bare layer-resolved Coulomb interaction in a uniform dielectric κ = 4.5, with the Gaussian orbital form factor exp(−r_o²q²/2), r_o = 0.6 Å, which sets the short-distance behaviour; it is a model form factor, not an ab initio pz orbital. W = (1 − VΠ)⁻¹V.
Approximations: Π is averaged over six directions of q and interpolated on 110 logarithmic points, so it keeps the dependence on |q| and the layer matrix but not the full angular dependence; the full dielectric matrix in G, G′ is not computed; W is static. No adjustable screening wavevector from my earlier models is used.
Direct kernel: D sums W over reciprocal vectors with the orbital phase factors exp(iG·(τa − τb)), with orbital positions τ = (0, δ1, δ1, 2δ1). Exchange uses transition densities u*_c u_v, the unscreened V and momentum Q + G with 19 vectors G (37 checked); at Q = G = 0 the divergent term cancels by orthogonality of c and v while a finite interlayer term survives.

### 41. Every run behind the results.  

Backup: the full convergence record. All rows are from the JSON output files. The trend with BSE grid is monotonic: 771 → 741 → 736 Å², with the energy settling near 70.0 meV; the screening grid matters far less than the BSE grid (the two 1980 rows differ by 0.002 Å² and 0.003 meV). The loop-size series shows the finite-loop average approaching the local value. The min-link column is the smallest singular value of the doublet overlap on the loop: always above 0.997, so the subspace is well transported. The 192-point grid is a cautionary example: a coarse uniform grid misses the narrow valleys and gives an unphysical answer (128 meV, 35 Å²), which is why the production grids are dense near K and K′. I did not extrapolate to infinite k-point density, and I do not claim full convergence.

### 42. Checks of gauge invariance and numerics.  

Backup: the individual checks, all from the output files. Re-solving the BSE after random phases on every electronic eigenvector changes the energies only at machine precision, and the curvature by 6 × 10⁻¹⁰ Å²; random U(2) rotations of the exciton pair change the curvature eigenvalues by ~10⁻⁹ Å². The Hamiltonian satisfies H(k+G) = D†(G) H(k) D(G) with the orbital phase matrix to 6 × 10⁻¹⁵ eV, and reduces to my continuum Hamiltonian near K to 10⁻¹¹ eV. I independently rebuilt every Wilson loop of the map from the stored raw 2×2 overlap matrices: agreement to 6 × 10⁻¹⁰ Å².
One important caveat: invariance under phases and U(2) rotations does not mean independence of every convention. Exciton Berry curvature depends on which point of the pair is used as the coordinate — electron, hole or centre — and on the orbital embedding. I use the symmetric centre and the embedding τ = (0, δ1, δ1, 2δ1) throughout; results with other conventions would differ by well-understood terms (see Exciton Berryology).

### 43. Reversing U swaps the valleys, not the pair of values.  

Optional results slide: bias reversal. On the 456-point check grid at loop side 1.5 × 10⁻³ Å⁻¹, U = +100 meV gives λ₋ = −771.27 Å² with a K-polarized eigenvector and λ₊ = +771.27 Å² K′-polarized. At U = −100 meV the values are identical but the valley assignment is swapped: now the negative eigenvalue is K′-like. So the bias reverses the valley-associated sign — just as it reverses the electron valley Chern numbers — while the unordered pair {−λ, +λ} stays the same. This is one reverse-bias test, not a field sweep; I do not draw any curve of λ versus U.
Second check on the same grid: switching exchange off changes |λ| from 771.3 to 764.8 Å², under 1%, and makes the valley polarization even purer (0.999998). So the curvature belongs to the valley-resolved excitons formed by the direct attraction; exchange's main role is to mix K and K′ in the energy eigenstates, which is exactly why the single-branch curvature comes out near zero.

### 44. The subspace is smooth where its states are not.  

Backup for results slide 4. Left map: for each small loop, the smallest overlap between the energy-sorted lowest state at neighbouring corners. It is 0.98–0.998 away from the centre, but 0.012 for the loop around Q = 0: there the sorted state jumps, so its Abelian Berry phase is undefined. Right map: the smallest singular value of the 2×2 overlap matrix of the doublet, which is at least 0.99956 everywhere: the two-dimensional subspace is transported smoothly.
Right panel: the lowest four exciton levels along Qx on the 864-point grid. Levels 1 and 2 are split by exchange by only 0.05–0.17 meV on the local map, while the third level is about 9 meV higher. The doublet therefore must be treated as a unit near Γ.
Away from the centre, where single-branch links are healthy, the Abelian curvature of each branch is below 3.5 × 10⁻⁷ Å² — compatible with zero on this grid — in sharp contrast to the ±300–480 Å² eigenvalues of the doublet at the same points.

### 45. What would turn local geometry into a topological claim.  

These are the next steps, in rough priority order, and the questions I would like to discuss.
Global topology first: the present curvature is local. To speak of a topological exciton phase we need the curvature, or Wilson-loop spectra, over the whole exciton Brillouin zone, and we need to know where the doublet stays isolated from higher states; a valley-resolved Chern number only makes sense if the valley decomposition stays well defined.
Bias: repeat at several U values, and connect U to an applied field with a realistic screening model; that also lets us connect to the published dark–bright crossing.
Physics and numerics: the listed approximations, each of which could change magnitudes.
Observable: in a time-reversal-symmetric system the two valleys cancel in any Hall-like response, so an anomalous drift needs valley imbalance, for example from circularly polarized excitation; we should estimate its size. Edge states require a ribbon or domain-wall calculation.

### 46. Two different Berry curvatures, one composite.  

Concept slide from the proposal, updated. Panel a is the curvature of one electron band over electron momentum k. Panel b is the exciton as a bound composite. Panel c is now computed: the eigenvalues of the 2×2 non-Abelian curvature of the lowest exciton doublet over the pair momentum Q (results slide 3). The key point survives: exciton geometry is a separate quantity and had to be calculated, not read off from electron valley Chern numbers.

### 47. Exciton Berry curvature, defined.  

Superseded. This was the proposal before the calculation: an Abelian, single-band exciton curvature with the electron at k + Q and the hole at k, to be evaluated with Fukui–Hatsugai–Suzuki plaquettes. The calculation showed that the lowest exciton states form a nearly degenerate doublet, so a single-band Abelian curvature is not well defined near Q = 0. The actual calculation uses the symmetric pair coordinate and non-Abelian Wilson loops for the doublet (results slides 1 and 4, Appendix C). Kept for the record.

### 48. Three levels, three kinds of evidence.  

These three claims are often blurred, and each needs different evidence. Ordinary diffusion needs no geometry at all. Sideways drift needs exciton Berry curvature, and edge transport needs a true topological invariant plus modes that survive disorder. None of them has been shown for this project.

### 49. What nonzero exciton curvature would do.  

An exciton is neutral, but if it has an out-of-plane dipole then a spatial gradient of the perpendicular field pushes it in-plane. If an isolated exciton branch has nonzero Berry curvature, that push could produce a sideways velocity, like a Hall effect without charge. This is our proposal, the two valleys would cancel unless populated unequally, and the animation is a schematic rather than a result.

### 50. Closest scientific precedents.  

These four papers are the closest work to ours, and none of them is the calculation we propose. One covers the same material but studies polaritons, and another finds exciton Berry curvature on a different graphene platform. The other two are theories of enhanced diffusion and of collective polariton response, which helps define what would be new here.

### 51. Three questions, kept separate.  

Conceptual guardrail: Berry curvature, enhanced diffusion, anomalous Hall-like motion and protected edge states are not interchangeable claims.

### 52. From electron bands to exciton motion.  

Central research-direction slide, proposed and unverified. Start from the electronic eigenstates, solve the electron-hole problem in the biased four-band basis at finite Q, evaluate the exciton Berry curvature, and ask whether a force produces an anomalous velocity. The pseudospin winding characterises the electrons; it does not by itself determine the exciton Chern number, and an electron valley Chern number does not set it.

### 53. From working calculations to a transport claim.  

Step one is a set of analytic working calculations in Appendix A, not independently validated. Step two formulates the exciton problem at finite Q. Step three computes Omega_X with the plaquette method, the diffusion tensor, the anomalous response and finite-edge spectra, benchmarked against limiting cases. Step four compares with bias-tunable optical or spatial signatures.
