# TermuxForge starter (safe demo package)

This starter creates a tiny `forge-hello` command so you can test the APT packaging flow.

## Important
- This is a starter kit, not a live APT repository.
- Upload these files to your public `TermuxForge` GitHub repository.
- A GitHub repository alone is not an APT repository: the `.deb`, `Packages` index, and repository metadata must be published.
- This first demo uses an unsigned local/static repository setup only as a build/test starting point. Do not tell users to bypass APT signature checks. Before public use, add proper repository signing and verify the signing key fingerprint through a trusted channel.

## Files
- `package/` — source layout for the harmless demo command.
- `scripts/build-demo.sh` — builds the `.deb` on Termux.
- `.github/workflows/pages.yml` — example Pages deployment workflow; it expects a prepared `public/` directory and is a next-step template.

## Next step
On Termux, download this starter ZIP, extract it, and run:
```sh
cd TermuxForge-starter
bash scripts/build-demo.sh
```
The generated `.deb` will be in `dist/`.
