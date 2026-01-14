# ARCHSETUP

### What

This is a repository with lists of packages that I need on a minimal (arguably) Arch Linux installation on a new PC.

### How

Packages are listed in the _YAML_ files. To install, run something like:

```bash
yq -r '.niri[]' packages.yaml | yay -S --needed -
```
