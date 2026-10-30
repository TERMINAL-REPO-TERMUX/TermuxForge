from pathlib import Path
from datetime import datetime, timezone
import hashlib

root = Path("public/dists/stable")

files = [
    root / "main/binary-aarch64/Packages",
    root / "main/binary-aarch64/Packages.gz",
]

now = datetime.now(timezone.utc)
date = now.strftime("%a, %d %b %Y %H:%M:%S UTC")

lines = [
    "Origin: TermuxForge",
    "Label: TermuxForge",
    "Suite: stable",
    "Codename: stable",
    "Date: " + date,
    "Architectures: aarch64",
    "Components: main",
    "Description: TermuxForge APT Repository",
    "",
    "MD5Sum:",
]

for file in files:
    data = file.read_bytes()
    checksum = hashlib.md5(data).hexdigest()
    relative_path = file.relative_to(root)
    lines.append(f" {checksum} {len(data)} {relative_path}")

lines.extend(["", "SHA1:"])

for file in files:
    data = file.read_bytes()
    checksum = hashlib.sha1(data).hexdigest()
    relative_path = file.relative_to(root)
    lines.append(f" {checksum} {len(data)} {relative_path}")

lines.extend(["", "SHA256:"])

for file in files:
    data = file.read_bytes()
    checksum = hashlib.sha256(data).hexdigest()
    relative_path = file.relative_to(root)
    lines.append(f" {checksum} {len(data)} {relative_path}")

release_file = root / "Release"
release_file.write_text("\n".join(lines) + "\n")

print("Release file created successfully!")
