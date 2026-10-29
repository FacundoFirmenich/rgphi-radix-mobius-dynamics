#!/usr/bin/env python3
"""Small deterministic layout fixes after Paper I finalization generation."""
from pathlib import Path

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

TEX.write_text(text, encoding="utf-8")
print("PASS_PAPER_I_FINALIZATION_POSTFIX")
