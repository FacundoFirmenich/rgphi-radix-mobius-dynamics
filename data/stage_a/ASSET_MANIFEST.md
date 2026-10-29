# Stage A and Stage B2 asset manifest

| Asset | Bytes | SHA-256 | Role |
|---|---:|---|---|
| `RGPHI_GLOBAL_TRAP_CUT_088_STAGE_A_BUNDLE.zip` | 185993 | `a07640fb6b86b14dc52e19095d927505efc36a737acd9023fa677a26f3d3b7ee` | full verified Stage A evidence bundle |
| `D2500_safe_states.csv` | 100057 | `d5f1be28b795ddeb0d71ce39142384634404e257ab5f2a6af39b576421959d6f` | complete D=2,500 safe-state list |
| `D10000_safe_states.csv` | 348114 | `276431f5e8330bef10f6e1cf656bca7c7b24821af060a8c8aedfad38fb24e27b` | complete D=10,000 safe-state list |
| `RGPHI_FRONTIER185_CHECKPOINT/cur/b0000.bin...b0127.bin` | 19700805368 | manifest `dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7` | exact Stage B2 input; payload absent from repository |

The first three assets are suitable for GitHub Release/Zenodo. The checkpoint
payload requires external storage with byte-for-byte validation before use.
