#!/usr/bin/env python3
"""Small deterministic layout and exactness fixes after Paper I generation."""
from pathlib import Path

# This script is intentionally idempotent and safe to rerun after governance edits.
ROOT = Path(__file__).resolve().parents[2]
TEX = ROOT / "paper" / "main.tex"

text = TEX.read_text(encoding="utf-8")

text = text.replace(
    "\\begin{tikzpicture}[\n  box/.style={draw, rounded corners, align=center, inner sep=4pt,\n              font=\\small, text width=.29\\textwidth},\n  wide/.style={box, text width=.66\\textwidth},",
    "\\begin{tikzpicture}[scale=.82, transform shape,\n  box/.style={draw, rounded corners, align=center, inner sep=4pt,\n              font=\\small, text width=.25\\textwidth},\n  wide/.style={box, text width=.58\\textwidth},",
)
text = text.replace(
    "below left=5mm and 5mm of layers",
    "below left=5mm and 2mm of layers",
)
text = text.replace(
    "below right=5mm and 5mm of layers",
    "below right=5mm and 2mm of layers",
)
text = text.replace(
    "The public research repository is available at \\url{https://github.com/FacundoFirmenich/rgphi-radix-mobius-dynamics}.",
    "The public research repository is available as the \\href{https://github.com/FacundoFirmenich/rgphi-radix-mobius-dynamics}{RG$\\Phi$ project repository}.",
)

old_corollary = r"""\begin{corollary}[Current height is not a Bellman value]
The scalar $q(x)$ cannot order states by future portal value.  At the relevant checkpoints, future-winning latent states have heights approximately $4.68$, $2.55$, and $2.14$, while the target-optimal competitors have heights $129$, $1203$, and above $11{,}000$.
\end{corollary}"""
new_corollary = r"""\begin{corollary}[Current height is not a Bellman value]
The scalar $q(x)$ cannot order states by future portal value.  The following exact same-time comparisons reverse the ordering induced by present height:
\begin{center}
\small
\begin{tabular}{ccllc}
\toprule
checkpoint & target-optimal state & $q$ & latent winning state ($q$) & remaining costs\\
\midrule
$45$  & $128/129$     & $129$   & $103/131\ (131/28)$        & $42>40$\\
$85$  & $1202/1203$   & $1203$  & $956/1573\ (1573/617)$     & $54>35$\\
$120$ & $11156/11157$ & $11157$ & $11803/22160\ (22160/10357)$ & $48>42$\\
\bottomrule
\end{tabular}
\end{center}
Thus states of much smaller current height can have strictly smaller exact cost to the next portal.
\end{corollary}"""
text = text.replace(old_corollary, new_corollary)

TEX.write_text(text, encoding="utf-8")
print("PASS_PAPER_I_FINALIZATION_POSTFIX")
