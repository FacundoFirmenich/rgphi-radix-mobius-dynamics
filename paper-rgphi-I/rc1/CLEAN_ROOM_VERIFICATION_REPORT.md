# RGΦ I RC1 — internal clean-room simulation

A fresh directory was populated from RC1 source while excluding generated PDF, AUX, BBL, BLG, LOG, OUT and TOC files. Then:

```bash
make verify
make pdf
```

Results:

- canonical article/CSV/JSON/supplement labelling: PASS;
- 37-row nonsquare certificate: PASS;
- Python replay of 1,001 bases: PASS;
- independent C++ replay: PASS;
- content-cocycle and spectral certificate: PASS;
- article compilation: PASS;
- supplement compilation: PASS;
- article pages: 16;
- supplement pages: 4;
- extracted text equality: PASS.

This remains an internal simulation, not the binding external clean-room gate.
