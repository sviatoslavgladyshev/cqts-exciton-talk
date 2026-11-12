"""Render the equations added for the results section (December 2026 revision).

Same recipe as the existing equations: standalone class, 10 pt Computer Modern, 960 dpi,
transparent background; display at about 0.22 of the pixel size.
Conventions follow BLG_multiband_Berry/LATTICE_METHOD_RU.md: symmetric pair coordinate
(electron at k+Q/2, valence state at k-Q/2), A = i<X|grad_Q X>, lambda = -arg eig(W) / (dQx dQy).

    python3 tools/make_equations.py          # needs latex + dvipng
Also writes latex/results-equations.tex with every source string.
"""
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets'

PRE = r"""\documentclass[10pt,border=4pt]{standalone}
\usepackage{amsmath,amssymb,bm,xcolor}
\definecolor{ink}{HTML}{202124}\definecolor{acc}{HTML}{0D40A6}\definecolor{ele}{HTML}{0D40A6}
\definecolor{hol}{HTML}{C5221F}\definecolor{exc}{HTML}{188038}\definecolor{mut}{HTML}{5F6368}\definecolor{pur}{HTML}{4E057E}
\newcommand{\kk}{\mathbf k}\newcommand{\QQ}{\mathbf Q}
\begin{document}\color{%s}$\displaystyle %s$\end{document}"""

EQ = {
    # electronic lattice Hamiltonian used in the calculation, basis (A1, B1, A2, B2)
    'eq-r-ham-accent': ('acc', r"""\renewcommand{\arraystretch}{1.25}H(\kk,U)=\begin{pmatrix}
U/2 & -\gamma_0 g & 0 & -\gamma_3 g^{*}\\
-\gamma_0 g^{*} & U/2 & \gamma_1 & 0\\
0 & \gamma_1 & -U/2 & -\gamma_0 g\\
-\gamma_3 g & 0 & -\gamma_0 g^{*} & -U/2\end{pmatrix}"""),
    'eq-r-g': ('ink', r"""g(\kk)=\sum_{j=1}^{3}e^{i\kk\cdot\bm\delta_j},\qquad g(\mathbf K+\mathbf p)\simeq-\tfrac{\sqrt3\,a}{2}\,(p_x-ip_y)"""),
    'eq-r-par': ('ink', r"""E_{\pm}(\mathbf p)\simeq\pm\sqrt{\tfrac{U^{2}}{4}+\Big(\tfrac{\hbar^{2}p^{2}}{2m^{*}}\Big)^{2}}\quad(\gamma_3=0,\ U\ll\gamma_1)"""),
    # exciton state in the symmetric pair coordinate
    'eq-r-x': ('ink', r"""|X_S(\QQ)\rangle=\sum_{\kk,c,v}A^{S}_{\kk cv}(\QQ)\;{\color{ele}c^{\dagger}_{c,\kk+\QQ/2}}\;{\color{hol}c_{v,\kk-\QQ/2}}\;|\mathrm{GS}\rangle"""),
    'eq-r-comp': ('ink', r"""\text{electron at }{\color{ele}\kk+\QQ/2},\quad\text{valence state }{\color{hol}\kk-\QQ/2},\quad\text{pair momentum }{\color{exc}\QQ}"""),
    # finite-Q BSE, Tamm-Dancoff, singlet
    'eq-r-bse': ('ink', r"""\sum_{j}\Big[\big(E_{c_i,\kk_i+\frac{\QQ}{2}}-E_{v_i,\kk_i-\frac{\QQ}{2}}\big)\delta_{ij}-K^{d}_{ij}(\QQ)+2K^{x}_{ij}(\QQ)\Big]A^{S}_{j}={\color{exc}E_S(\QQ)}\,A^{S}_{i}"""),
    'eq-r-idx': ('mut', r"""i\equiv(\kk,c,v):\ \ 2\ \text{valence}\times 2\ \text{conduction}=4\ \text{transitions per }\kk"""),
    # screening
    'eq-r-w': ('ink', r"""W(q)=\big[I-V(q)\,\Pi(q)\big]^{-1}V(q),\qquad V_{\ell\ell'}(q)=\frac{2\pi e^{2}}{\kappa q}\,e^{-q|z_\ell-z_{\ell'}|}\,e^{-r_o^{2}q^{2}/2}"""),
    'eq-r-pi': ('ink', r"""\Pi_{\ell\ell'}(\mathbf q)=2\sum_{\kk nm}w_{\kk}\,\frac{f_{n\kk}-f_{m,\kk+\mathbf q}}{E_{n\kk}-E_{m,\kk+\mathbf q}}\,L^{\ell}_{nm}(\kk,\mathbf q)\,L^{\ell'*}_{nm}(\kk,\mathbf q),\qquad L^{\ell}_{nm}=\sum_{a\in\ell}u^{*}_{n\kk a}\,u_{m,\kk+\mathbf q,a}"""),
    'eq-r-kd': ('ink', r"""K^{d}_{ij}=\sqrt{w_iw_j}\sum_{ab}D_a^{b}(\kk_i,\kk_j)\,u^{*}_{c_i a}u_{c_j a}\,u_{v_i b}u^{*}_{v_j b},\qquad D_a^{b}(\kk_i,\kk_j)=\sum_{\mathbf G}W_{\ell(a)\ell(b)}(|\kk_i-\kk_j+\mathbf G|)\,e^{i\mathbf G\cdot(\bm\tau_a-\bm\tau_b)}"""),
    # gauge-covariant overlap with Bloch factors
    'eq-r-m': ('ink', r"""M_{ST}(\QQ,\QQ')=\sum_{\kk}\sum_{cv,c'v'}A^{S*}_{\kk cv}(\QQ)\,A^{T}_{\kk c'v'}(\QQ')\;
\underbrace{{\color{ele}\langle u_{c,\kk+\QQ/2}|u_{c',\kk+\QQ'/2}\rangle}}_{\text{electron}}\;
\underbrace{{\color{hol}\langle u_{v',\kk-\QQ'/2}|u_{v,\kk-\QQ/2}\rangle}}_{\text{hole}}"""),
    'eq-r-svd': ('ink', r"""M=L\,\Sigma\,R^{\dagger}\ \Rightarrow\ \mathcal U=L R^{\dagger},\qquad \mathcal W=\mathcal U_{12}\,\mathcal U_{23}\,\mathcal U_{34}\,\mathcal U_{41}"""),
    'eq-r-lam-accent': ('acc', r"""\lambda_{\pm}(\mathcal F_{xy})\simeq-\frac{\arg\,\mathrm{eig}_{\pm}(\mathcal W)}{\delta Q_x\,\delta Q_y}"""),
    'eq-r-f': ('ink', r"""\mathcal A^{\mu}_{ST}=i\langle X_S|\partial_{Q_\mu}X_T\rangle,\qquad \mathcal F_{xy}=\partial_{x}\mathcal A^{y}-\partial_{y}\mathcal A^{x}-i\,[\mathcal A^{x},\mathcal A^{y}]"""),
    'eq-r-gauge': ('ink', r"""|X_S\rangle\to\sum_T|X_T\rangle\,V_{TS}(\QQ),\ \ V\in U(2)\quad\Rightarrow\quad \mathcal W\to V^{\dagger}\,\mathcal W\,V,\quad \mathcal F_{xy}\to V^{\dagger}\mathcal F_{xy}V"""),
    'eq-r-trace': ('ink', r"""\lambda_{+}+\lambda_{-}=\mathrm{tr}\,\mathcal F_{xy}\approx0"""),
    'eq-r-chernpair': ('ink', r"""\mathcal C_{\mathrm{doublet}}=\frac{1}{2\pi}\int_{\text{exciton BZ}}\mathrm{tr}\,\mathcal F_{xy}\,d^{2}Q\quad\text{(not computed)}"""),
}


def render(name, colour, body, workdir):
    tex = workdir / f'{name}.tex'
    tex.write_text(PRE % (colour, body))
    subprocess.run(['latex', '-interaction=nonstopmode', '-halt-on-error', tex.name], cwd=workdir, check=True,
                   stdout=subprocess.DEVNULL)
    subprocess.run(['dvipng', '-q', '-D', '960', '-bg', 'Transparent', '-T', 'tight', '-o', str(OUT / f'{name}.png'),
                    f'{name}.dvi'], cwd=workdir, check=True, stdout=subprocess.DEVNULL)


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as tmp:
        for name, (colour, body) in EQ.items():
            render(name, colour, body, Path(tmp))
            print('wrote', name)
    lines = ['% LaTeX source for equations added with the exciton Berry-curvature results.',
             '% Rendered by tools/make_equations.py: standalone 10pt, 960 dpi, transparent. Display at ~0.22 of pixel size.', '']
    for name, (colour, body) in EQ.items():
        lines += [f'% {name}.png ({colour})', '%   ' + body.replace('\n', '\n%   '), '']
    (ROOT / 'latex' / 'results-equations.tex').write_text('\n'.join(lines))
