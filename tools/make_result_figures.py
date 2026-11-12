"""Build the result figures for the talk from the saved numerical outputs.

Every plotted number is read from the files written by the lattice BSE code
(BLG_multiband_Berry/): nothing is interpolated, fitted or invented.

    python3 tools/make_result_figures.py [path/to/BLG_multiband_Berry]

Writes assets/res-*.png and assets/res-numbers.json (the values quoted on slides).
"""
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
DATA = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'BLG_multiband_Berry'
OUT = ROOT / 'assets'

INK, MUTED, GRID = '#202124', '#5F6368', '#DADCE0'
PURPLE, BLUE, RED, GREEN, ORANGE = '#4E057E', '#0D40A6', '#C5221F', '#188038', '#E37400'
# Diverging: blue (negative) <-> neutral gray <-> red (positive), as in the electron Berry-curvature animation.
DIVERGE = LinearSegmentedColormap.from_list('div', ['#0D40A6', '#5B83CF', '#F0EFEC', '#E0726B', '#C5221F'])

plt.rcParams.update({
    'font.family': 'Arial', 'font.size': 26, 'axes.edgecolor': GRID, 'axes.labelcolor': INK,
    'xtick.color': MUTED, 'ytick.color': MUTED, 'axes.linewidth': 1.2, 'xtick.major.size': 0,
    'ytick.major.size': 0, 'axes.spines.top': False, 'axes.spines.right': False,
    'savefig.dpi': 200, 'savefig.transparent': False, 'figure.facecolor': 'white',
})


def load(name):
    return json.loads((DATA / name).read_text())


def save(fig, name):
    fig.savefig(OUT / name, bbox_inches='tight', pad_inches=0.12, facecolor='white')
    plt.close(fig)
    print('wrote', OUT / name)


def tiles(ax, values, qaxis, vmax, cmap, fmt, label_all=False, highlight=None):
    """Draw a 5x5 grid of separated square tiles, one per computed Q point (no interpolation)."""
    q = qaxis * 1e3                     # 10^-3 1/A
    h = (q[1] - q[0]) * 0.46
    for i, qx in enumerate(q):
        for j, qy in enumerate(q):
            v = values[i, j]
            ax.add_patch(plt.Rectangle((qx - h, qy - h), 2 * h, 2 * h, color=cmap((v / vmax + 1) / 2) if vmax else cmap(v),
                                       lw=0, joinstyle='round'))
            if label_all or (i == 2 and j == 2):
                light = abs(v) / vmax > 0.55 if vmax else False
                ax.text(qx, qy, fmt(v), ha='center', va='center', fontsize=23,
                        color='white' if light else INK, fontweight='bold' if (i == 2 and j == 2) else 'normal')
    if highlight is not None:
        i, j = highlight
        ax.add_patch(plt.Rectangle((q[i] - h - .25, q[j] - h - .25), 2 * h + .5, 2 * h + .5, fill=False, ec=INK, lw=2.5))
    lim = q[-1] + h + 0.6
    ax.set(xlim=(-lim, lim), ylim=(-lim, lim), aspect='equal', xticks=q, yticks=q)
    ax.set_xticklabels([f'{v:g}' for v in q]); ax.set_yticklabels([f'{v:g}' for v in q])
    ax.set_xlabel(r'$Q_x$  (10$^{-3}$ Å$^{-1}$)'); ax.set_ylabel(r'$Q_y$  (10$^{-3}$ Å$^{-1}$)')
    for s in ax.spines.values():
        s.set_visible(False)


def curvature_map():
    m = np.load(DATA / 'lattice_local_map.npz', allow_pickle=False)
    qaxis, lam = m['Q'], m['curvature_eigenvalues']           # lam[ix, iy, 0] = lambda_-, [...,1] = lambda_+
    # Independent check: rebuild every Wilson loop from the stored raw 2x2 overlap matrices.
    step = float(m['step'])
    rebuilt = np.zeros_like(lam)
    for i in range(5):
        for j in range(5):
            loop = np.eye(2, dtype=complex)
            for mat in m['raw_overlap_matrices'][i, j]:
                left, _, right = np.linalg.svd(mat)
                loop = loop @ (left @ right)
            rebuilt[i, j] = np.sort(-np.angle(np.linalg.eigvals(loop)) / step ** 2)
    assert np.max(abs(rebuilt - lam)) < 1e-6, 'stored map does not match its raw overlaps'

    fig, axes = plt.subplots(1, 2, figsize=(14.2, 6.6), gridspec_kw=dict(wspace=0.32))
    for k, ax in enumerate(axes):
        tiles(ax, lam[:, :, k], qaxis, 800, DIVERGE, lambda v: f'{v:+.0f}', label_all=True)
    cax = fig.add_axes([0.93, 0.18, 0.016, 0.64])
    sm = plt.cm.ScalarMappable(cmap=DIVERGE, norm=plt.Normalize(-800, 800))
    cb = fig.colorbar(sm, cax=cax, ticks=[-800, -400, 0, 400, 800])
    cb.outline.set_visible(False); cb.ax.tick_params(colors=MUTED, labelsize=23)
    cb.set_label('Å$^2$', color=INK, rotation=0, labelpad=18)
    save(fig, 'res-curvature-map.png')
    return dict(map_qaxis=qaxis.tolist(), map_step=step, map_centre=lam[2, 2].tolist(),
                map_offcentre_abs_range=[float(abs(np.delete(lam[..., 1].ravel(), 12)).min()),
                                         float(abs(np.delete(lam[..., 1].ravel(), 12)).max())],
                map_rebuild_error=float(np.max(abs(rebuilt - lam))))


def links_map():
    """Single sorted state vs. two-state subspace: how well each is transported around each small loop."""
    m = np.load(DATA / 'lattice_local_map.npz', allow_pickle=False)
    qaxis = m['Q']
    single = m['abelian_links'][:, :, 0]
    pair = np.array([[min(np.linalg.svd(mat, compute_uv=False).min() for mat in m['raw_overlap_matrices'][i, j])
                      for j in range(5)] for i in range(5)])
    seq = LinearSegmentedColormap.from_list('seq', ['#F8F9FA', '#E6DAF2', '#9A6CC0', '#4E057E'])
    fig, axes = plt.subplots(1, 2, figsize=(14.2, 6.6), gridspec_kw=dict(wspace=0.32))
    for ax, vals, fmt in zip(axes, [single, pair], [lambda v: f'{v:.3f}', lambda v: f'{v:.4f}']):
        tiles(ax, vals, qaxis, None, seq, fmt, label_all=True)
        for t in ax.texts:
            t.set_color('white' if float(t.get_text()) > 0.6 else INK); t.set_fontsize(21 if fmt(0.5).count('0') < 3 else 17)
    save(fig, 'res-links.png')
    return dict(single_state_min_link_centre=float(single[2, 2]), single_state_min_link_offcentre=float(np.delete(single.ravel(), 12).min()),
                pair_min_singular=float(pair.min()),
                branch_abs_curvature_max_offcentre=float(max(abs(np.delete(m['abelian_curvature'][..., b].ravel(), 12)).max() for b in range(2))))


def levels():
    r = load('lattice_screen8_results.json')
    e = np.array(r['energies_Q0_eV']) * 1e3
    thr = r['threshold_Q0_eV'] * 1e3
    fig, ax = plt.subplots(figsize=(7.4, 8.2))
    ax.axhspan(thr, 100, color='#E8EAED', lw=0)
    ax.axhline(thr, color=MUTED, lw=2)
    ax.text(0.03, thr + 0.9, 'free electron–hole pairs\n(discrete-grid threshold)', color=MUTED, fontsize=20, va='bottom')
    for n, v in enumerate(e):
        doublet = n < 2
        ax.plot([0.10, 0.62], [v, v], color=GREEN if doublet else '#7FB58F', lw=5 if doublet else 3, solid_capstyle='round')
    ax.text(0.66, e[0], 'lowest doublet\n(two states)', color=INK, fontsize=20, va='center', fontweight='bold')
    ax.text(0.66, e[2:4].mean() + .5, 'next levels', color=MUTED, fontsize=20, va='center')
    # binding energy arrow
    ax.annotate('', xy=(0.05, e[0]), xytext=(0.05, thr), arrowprops=dict(arrowstyle='<->', color=PURPLE, lw=2.2))
    ax.text(0.075, (e[0] + thr) / 2 + 2, f'{thr - e[0]:.1f} meV', color=PURPLE, fontsize=22, va='center', fontweight='bold')
    ax.annotate('', xy=(0.36, e[0]), xytext=(0.36, e[2]), arrowprops=dict(arrowstyle='<->', color=BLUE, lw=2.2))
    ax.text(0.385, (e[0] + e[2]) / 2, f'{e[2] - e[1]:.2f} meV', color=BLUE, fontsize=22, va='center', fontweight='bold')
    ax.set(xlim=(0, 1.05), ylim=(66, 96), xticks=[], ylabel='Excitation energy at Q = 0  (meV)')
    ax.spines['bottom'].set_visible(False)
    ax.yaxis.grid(True, color='#F1F3F4', lw=1); ax.set_axisbelow(True)
    save(fig, 'res-levels.png')
    return dict(E1_meV=e[0], E2_meV=e[1], E3_meV=e[2], threshold_meV=thr, binding_meV=thr - e[0],
                splitting_eV=r['splitting_Q0_eV'], doublet_gap_meV=r['doublet_gap_eV'] * 1e3,
                energies_Q0_meV=e.tolist())


def dispersion():
    m = np.load(DATA / 'lattice_map_map.npz', allow_pickle=False)
    q, en = m['Q'] * 1e3, m['energies'][:, 2, :] * 1e3          # line Q_y = 0
    fig, ax = plt.subplots(figsize=(8.4, 6.4))
    colors = [GREEN, '#0F5C2A', '#9AA0A6', '#5F6368']
    styles = ['-', '--', '-', '--']
    for b in range(4):
        ax.plot(q, en[:, b], styles[b], color=colors[b], lw=2.4, marker='o', ms=8, mec='white', mew=1.5, label=f'level {b + 1}')
    ax.set(xlabel=r'$Q_x$  (10$^{-3}$ Å$^{-1}$),  $Q_y$ = 0', ylabel='Excitation energy (meV)', xticks=q)
    ax.yaxis.grid(True, color='#F1F3F4', lw=1); ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=19, ncol=2, loc='upper center', bbox_to_anchor=(0.5, 1.14))
    save(fig, 'res-dispersion.png')
    return dict(dispersion_Q=m['Q'].tolist(), dispersion_meV=en.tolist())


def convergence():
    runs = [load(n) for n in ['lattice_d5_results.json', 'lattice_d6_results.json', 'lattice_map_results.json',
                              'lattice_d7_results.json', 'lattice_screen8_results.json']]
    fine = load('lattice_fine_checks.json')
    fig, axes = plt.subplots(1, 2, figsize=(14.2, 5.6), gridspec_kw=dict(wspace=0.38, width_ratios=[1.25, 1]))
    ax = axes[0]
    # one point per BSE grid at the finest RPA level that was run with it
    best = {}
    for r in runs:
        best[r['points']] = r
    pts = sorted(best)
    vals = [abs(best[p]['curvature_eigenvalues_A2'][0]) for p in pts]
    ax.plot(pts, vals, '-', color=PURPLE, lw=2.4, marker='o', ms=11, mec='white', mew=2)
    for p, v in zip(pts, vals):
        ax.text(p * 1.07, v + 2.0, f'{v:.1f}', ha='left', va='bottom', color=INK, fontsize=25)
    ax.set(xscale='log', xticks=pts, xlabel='BSE electronic k points', ylabel=r'$|\lambda_\pm|$  (Å$^2$)', ylim=(725, 785), xlim=(380, 2900))
    ax.set_xticklabels([str(p) for p in pts]); ax.minorticks_off()
    ax.yaxis.grid(True, color='#F1F3F4', lw=1); ax.set_axisbelow(True)
    ax = axes[1]
    dq = [0.0015, 0.00075, 0.000375]
    # the small-loop checks were run with RPA level 7, so compare with the RPA-7 run at the same BSE grid
    d7 = load('lattice_d7_results.json')
    assert d7['points'] == 1980 and d7['parameters']['screen_depth'] == 7
    dv = [abs(d7['curvature_eigenvalues_A2'][0]), abs(fine['half_step']['curvature_A2'][0]), abs(fine['quarter_step']['curvature_A2'][0])]
    x = [d * 1e4 for d in dq]
    ax.plot(x, dv, '-', color=BLUE, lw=2.4, marker='o', ms=11, mec='white', mew=2)
    for xx, v in zip(x, dv):
        ax.text(xx + 0.5, v - 0.12, f'{v:.2f}', ha='right', va='top', color=INK, fontsize=25)
    ax.set(xlabel=r'Loop side $\delta Q$  (10$^{-4}$ Å$^{-1}$)', ylabel=r'$|\lambda_\pm|$  (Å$^2$)', xticks=x, xlim=(18.5, 2.5), ylim=(733, 737))
    ax.set_xticklabels(['15', '7.5', '3.75'])
    ax.yaxis.grid(True, color='#F1F3F4', lw=1); ax.set_axisbelow(True)
    save(fig, 'res-convergence.png')
    return dict(grid=[dict(points=r['points'], rpa_level=r['parameters']['screen_depth'], E1_meV=r['energies_Q0_eV'][0] * 1e3,
                           lam_abs=abs(r['curvature_eigenvalues_A2'][0])) for r in runs],
                contour=[dict(dQ=a, lam_abs=b) for a, b in zip(dq, dv)],
                valley_polarization_quarter=fine['quarter_step']['valley_polarization'])


if __name__ == '__main__':
    numbers = {}
    for f in (curvature_map, links_map, levels, dispersion, convergence):
        numbers.update(f())
    numbers['validation'] = load('lattice_validation.json')
    numbers['local_map_checks'] = load('lattice_local_map_checks.json')
    (OUT / 'res-numbers.json').write_text(json.dumps(numbers, indent=1, default=float))
    print('wrote', OUT / 'res-numbers.json')
