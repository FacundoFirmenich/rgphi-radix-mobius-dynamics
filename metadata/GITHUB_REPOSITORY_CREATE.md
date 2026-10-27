# One required GitHub administration step

The connected GitHub integration can write to existing repositories but does
not expose repository creation. Create an empty public repository with:

- Owner: `FacundoFirmenich`
- Name: `rgphi-radix-mobius-dynamics`
- Visibility: Public
- Description: `Exact rational radix-Mobius dynamics, robust nonnested extremal targets, and finite modular traps.`
- Initialize with README: **No**
- Add .gitignore: **No**
- Add license: **No**

After creation, push the prepared `main` branch and tags with
`tools/publish_to_github.sh` or authorize the connected assistant to populate it.
