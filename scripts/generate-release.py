from pathlib import Path
import hashlib

root = Path("dists/stable")
files = [
    root / "main/binary-aarch64/Packages",
    root / "main/binary-aarch64/Packages.gz",
]

lines = [
    "Origin: TermuxForge",
    "Label: TermuxForge",
    "Suite: stable",
    "Codename: stable",
    "Architectures: aarch64",
    "Components: main",
    "Description: TermuxForge APT Repository",
    "",
    "SHA256:",
]

for file in files:
    data = file.read_bytes()
    checksum = hashlib.sha256(data).hexdigest()
    relative_path = file.relative_to(root)

    lines.append(
        f" {checksum} {len(data)} {relative_path}"
    )

release_file = root / "Release"
release_file.write_text("\n".join(lines) + "\n")

print("Release file created successfully!")
