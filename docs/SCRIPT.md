# Talk script — A Tale of Two Valleys: The Hidden Geometry of Excitons

CQTS Research Symposium, NYU Abu Dhabi · 20 minutes · slides 1–22

This is the spoken version: about 2,300 words, which is 20 minutes at roughly 115 words a minute, a calm pace that leaves room to pause on the figures and animations. The clock on each slide is where you should be when it ends. Builds on the slides play by themselves, so there are no clicks to time. *Italics* are stage directions, not text to read. The fuller notes in `SPEAKER_NOTES.md` carry the technical detail for questions.

If you are running late, cut the lines marked **[cut if late]**; together they save about 1:30.

---

## 1 · Title — *0:20*

Good afternoon. My talk is called *A Tale of Two Valleys*. The two valleys are K and K-prime in bilayer graphene, and the hidden geometry is the Berry curvature of the excitons that live there. As we will see, it comes out opposite in the two valleys. The question in blue is the one I have been working on with Dr. Marwa Mannai: can we have topological excitons in biased bilayer graphene?

## 2 · Why excitons? — *1:00*

An exciton is an electron and a hole bound together by their Coulomb attraction. It is bound, so it behaves as one particle. It is neutral, so it carries energy without carrying charge, which also means an ordinary voltage cannot simply push it around. So here is the hypothesis behind this work: if the exciton has its own band geometry, that geometry could be another handle on how it moves. I want to be clear from the start that this hypothesis is not yet tested.

## 3 · Excitons and polaritons already carry information — *2:00*

Before any mathematics: this is not science fiction. Excitons, and their light-dressed cousins the polaritons, already move and process information in the lab. Here are four experiments, all at room temperature.

*Left to right.* A switch from Michigan, where excitons in a WSe₂ monolayer are pushed along a guide and gated on and off. An integrated polariton transistor, two by two microns, switching in picoseconds with up to sixty-fold gain. Polariton spin logic in a perovskite cavity, where spin travels sixty microns and the authors build a NOT gate. And valley routing, where states from the two valleys travel in opposite directions along an interface.

Look at the tags. Three of the four are polaritons, not bare excitons. None is bilayer graphene. And none uses the Berry curvature of the excitons themselves. That is the gap I am working in.

## 4 · Spin information travels 92 µm — *3:15*

This is the paper Dr. Mannai pointed me to, published in Nature Materials this month by Shang and colleagues.

The headline is that spin-polarized polaritons travel ninety-two microns at room temperature, with an ordinary off-resonant laser. That is one to two orders of magnitude further than electron spins go.

How does it work? *Point to the steps.* One: bright excitons in a WS₂ monolayer mix with light trapped in a waveguide and form polaritons that live long and move fast. Two, the surprise: WS₂ also has dark excitons, with dipoles pointing out of the plane. An ordinary laser fills them, and they act as a built-in, linearly polarized source. Three: the two kinds of guided light modes, TE and TM, travel differently. That rotates linear polarization into circular, which is the optical spin Hall effect. *Point to the maps.* In a square cavity it makes these eight spin domains, and in a bigger cavity spin reaches right across a hundred microns.

*Orange box.* An honest caveat: this is spin–orbit coupling of light, in WS₂. It is not the exciton geometry I will show you. The link is motivation: excitons can carry spin and valley information a long way, and dark states matter.

## 5 · Bilayer graphene already works inside a cavity — *4:00*

So why bilayer graphene? Because a gate can tune it, and because it has already been put in a cavity.

*Left.* This year in Nature, a group at ETH Zürich placed gated bilayer graphene under a terahertz resonator and reached ultrastrong coupling, about forty percent. An exciton-like state is pulled out of the continuum by the cavity itself. It is not our exciton: that binding is mediated by photons, at tiny gaps and five kelvin.

*Right.* On the theory side, Duarte and colleagues predict exciton-polaritons in biased bilayer graphene whose branches and Rabi splitting are tuned by the bias. Their plot happens to use a hundred milli-electron-volts, the same bias as mine.

So the platform exists and the bias can tune it. What nobody had computed is the geometry of the exciton states themselves.

## 6 · Four orbitals and one gate-controlled bias — *5:10*

To get there we need the electrons first. AB bilayer graphene has four carbon sites per unit cell, two in each layer. One pair sits directly on top of each other and forms a strong vertical bond, gamma-one, about 0.4 electron-volts. Gamma-zero is the usual in-plane hopping, and gamma-three is a weaker skew hop that warps the bands.

The gate enters in one place only: a potential of plus U over two on the top layer and minus U over two on the bottom.

I use this model over the whole Brillouin zone, not just near K. The exciton calculation needs that, because screening and exchange involve both valleys. Near K it reduces exactly to the familiar continuum model. These are the standard parameters of McCann and Koshino, not fitted to a device.

## 7 · A band gap you can dial — *6:15*

Without bias, the two low-energy bands touch at K and K-prime and are roughly parabolic. Switch on U and a gap opens, and its size is set by the gate. *Point to the animation.* As U grows, the band edge moves onto a small ring, the Mexican-hat shape.

Published calculations give gaps up to about three hundred milli-electron-volts at strong fields. For the exciton calculation I fix U at a hundred.

Keep one thing in mind for later: the exciton is built from these conduction and valence states, so their energies and their wavefunctions both matter.

## 8 · Electron Berry curvature flips with the bias — *7:45*

Now the electronic topology. This part is established physics, which I re-derived as my starting point.

Berry curvature acts like a magnetic field in momentum space. *Point to the animation.* It sits near the band edge, it has three lobes because of the warping, it is opposite in K and K-prime, and it flips sign when the bias reverses.

Integrate it over one valley and you get a valley Chern number: minus or plus one, depending on the sign of U. The two valleys cancel, so there is no net Chern number, but the valley difference reverses with the gate. That is the origin of valley Hall physics in this material.

**[cut if late]** It is also why topological kink states form at domain walls in bilayer graphene.

The key point: all of this is about single electrons. It does not tell us the Berry curvature of an exciton as a function of its own momentum. That has to be computed separately.

## 9 · The story, in one picture — *8:30*

This is a cartoon, not a calculation. Light creates an electron in the conduction band and leaves a hole behind. Coulomb attraction binds them into an exciton, which moves as one neutral object.

*As the exciton bends.* The sideways bend at the end is the whole question: does the exciton band have a Berry curvature that could deflect it?

## 10 · A composite boson with its own momentum Q — *9:00*

A bare exciton is the electron–hole pair; a polariton adds a cavity photon. Today is about bare excitons. The key variable is Q, the momentum of the whole pair. Exciton topology means Berry curvature in Q, not in the electron's momentum.

## 11 · From electron–hole pairs to exciton bands — *10:20*

This equation turns electron bands into exciton bands. *Top line.* An exciton at momentum Q is a superposition of electron–hole pairs: the electron at k plus Q over two, the hole at k minus Q over two. In my calculation there are four such transitions at every k, over the whole zone, so both valleys sit in the same matrix.

*Second line.* This is the Bethe–Salpeter equation. The diagonal is the energy of a free pair. The direct term is the screened Coulomb attraction that binds them. The exchange term is repulsive, and it can move the pair from one valley to the other, so it couples K and K-prime excitons.

Out come the exciton bands, E of Q, and the weights A. One warning for later: the weights alone are not enough to get the geometry. You also need the electron wavefunctions underneath them.

## 12 · Bright, dark, and a field-driven crossing — *11:30*

One more piece of published physics. Bright excitons couple to light; dark ones do not. In bilayer graphene the lowest exciton is mostly dark because of an angular-momentum selection rule. Sauer and Pedersen showed that near 240 millivolts per ångström a bright state crosses below it.

My own model agrees qualitatively: at my bias, the lowest pair carries only about fourteen percent of the brightest state's dipole strength. I did not sweep the field, so I claim no crossing.

And a link back to the WS₂ experiment: there too, the dark states turned out to matter. The reason is different, but the lesson is the same.

## 13 · The question — *11:45*

So, the electron valley Chern numbers are established. The question is whether the excitons have geometry of their own. The next six slides are my calculation.

## 14 · What was computed — *12:45*

*Top row, left to right.* I take the four-orbital model over the whole zone. I diagonalize it on a grid that is much denser around the two valleys, because a coarse grid gets the excitons wrong. I build and solve the Bethe–Salpeter equation at finite Q, with screening computed from the same electrons and resolved by layer, and with exchange. The largest problem has almost eight thousand coupled pair states. Then I take the two lowest excitons, compute their overlaps between neighbouring Q points, and multiply them around small loops. These are Wilson loops, and they give the Berry curvature.

*Right.* These are model parameters, not a measured device: U of a hundred milli-electron-volts and a uniform dielectric environment.

## 15 · Excitons are bound, and come in pairs — *13:45*

First result: the energies. *Left.* The lowest exciton sits at seventy milli-electron-volts. You need about twenty-three more to tear it apart into a free electron and hole. And the lowest level is really two states with the same energy, split by only a nano-electron-volt, one from each valley. The next states are nine milli-electron-volts higher, so this pair is well isolated, which is exactly what we need to define its geometry.

*Right.* When the exciton moves, its energy rises like a particle with mass, and the two partners split slightly because exchange couples the valleys.

## 16 · Opposite curvature in the two valleys — *15:15*

This is the central result.

Berry curvature measures how the exciton's quantum state twists as its momentum changes. Here the twist is large, about seven hundred and thirty square ångström. *Point to the two maps.* It has opposite signs in the two valleys: blue for K-valley excitons, red for K-prime. Each tile is one point I computed. The strongest twist is at the centre, and the sign holds across the whole patch.

Because the two lowest excitons have the same energy, I treat them as a pair. That gives two curvature values, lambda-minus and lambda-plus. Each comes with a state that is ninety-nine point nine nine percent K or K-prime. So the K-like exciton and the K-prime-like exciton curve in opposite directions, as time reversal requires, and the calculation resolves it cleanly.

Two cautions. These are values for a pair of states, not for two separate bands. And this is a small patch around Q equals zero, not the whole exciton Brillouin zone.

## 17 · Follow the pair, not the individual states — *16:15*

Why a pair? Because the two states are degenerate, the individual energy eigenstates jump around as Q changes. *Point to the arrow.* A tiny step in Q can rotate the lowest state almost entirely into the other one. Its ordinary Berry phase is meaningless. The pair as a whole, the green disc, moves perfectly smoothly.

So I follow the pair, with overlaps that include the electron wavefunctions so that arbitrary phases cancel. And here is the striking contrast: the individual energy branches have curvature compatible with zero. Exchange mixes K and K-prime equally, and their opposite curvatures cancel. The geometry lives in the valley-resolved pair, not in the energy branches.

## 18 · Stable under refinement and gauge changes — *16:45*

Can we trust the number? Refining the grid moves it from 771 to 741 to 736, so the scale is stable, though not converged to the last digit. Random gauge changes move it by less than a billionth of a square ångström.

**[cut if late]** What I do not claim is that it survives once the physical approximations are removed.

## 19 · What this does and does not show — *17:30*

Back to the question. What the model shows: the lowest exciton pair has large Berry curvature, of opposite sign in the two valleys, and reversing the bias swaps them.

What it does not show: the total curvature of the pair is zero, so there is no net Chern number. The calculation is local, so there is no global invariant yet. And there is no transport calculation or measurement. So my answer is the boxed sentence: substantial, valley-contrasting exciton geometry; topology in the strong sense remains open.

## 20 · Can exciton geometry steer information? — *18:45*

Which brings me back to the devices. Could this geometry ever be used? These are directions, not results.

*Left.* Direction A: a force on a band with Berry curvature produces a sideways drift. Our valleys have opposite curvature, so K and K-prime excitons would drift to opposite sides. To predict it, I would need the dynamics of the pair, a realistic force on a neutral exciton, and how fast the valleys mix.

*Right.* Direction B: put these excitons in a cavity, like Duarte's proposal, to make bias-tunable polaritons. That needs the optical dipoles, the coupling, the detuning and the losses.

*Bottom.* Spin and valley information already travel tens of microns in other materials, and bilayer graphene already works in cavities. Intrinsic exciton geometry in bilayer graphene is the missing piece.

## 21 · Ateno — *19:05*

Twenty seconds on Ateno, which I co-founded. We are building a chip for on-device 3D mapping, so that robots can map places where GPS fails: tunnels, mines, warehouses. Our FPGA prototype got 3.9 times faster in ten days. Silicon is next.

## 22 · Conclusion — *20:00*

To conclude, back to the question on the cover.

Established: electron valley Chern numbers that reverse with the bias. Published by others: bright and dark excitons in bilayer graphene, room-temperature polariton spin and valley transport, and bilayer graphene in a cavity. Computed here: valley-contrasting exciton Berry curvature of about seven hundred and thirty square ångström near Q equals zero. Open: a global invariant, a measurable response, and whether it can steer excitons in a device.

So, can we have topological excitons in biased bilayer graphene? We have found the hidden geometry. Whether it becomes topology is the next chapter of the tale.

Thank you to Dr. Mannai and to CQTS. I am happy to take questions.

---

## Likely questions, short answers

- **"Is it topological, then?"** Not shown. The two curvatures cancel, so there is no net Chern number. A valley-resolved invariant would need the whole exciton Brillouin zone, and that is the next calculation.
- **"Isn't that just the electron Berry curvature?"** No. It is computed for the bound pair as a function of its own momentum Q, from gauge-covariant overlaps of the full exciton states. The electron result does not determine it.
- **"Why not one band at a time?"** The two lowest states are degenerate to 10⁻⁹ eV. The individual branches jump around in Q and have near-zero curvature. Only the pair is smooth (slide 17).
- **"How sure is 7.3 × 10² Å²?"** The scale is stable within the model: 771 → 741 → 736 Å² as the grid is refined, and it is gauge-invariant to 10⁻⁹. It is not converged to the last digit, and it rests on static screening, no GW and Tamm–Dancoff (backup C).
- **"Does the WS₂ result use your mechanism?"** No. It comes from TE–TM splitting of light modes. It motivates the application side only.
- **"Could you measure it?"** Possibly, as a valley-selective sideways drift with valley-polarized excitation, but intervalley mixing by exchange would compete. That is direction A, and it is not yet computed.
