# ARCHSETUP

### What

This is a repository with lists of packages that I need on a minimal (arguably) Arch Linux installation on a new PC.

### How

Packages are listed in the _.txt_ files. To install, run:

```bash
sudo pacman -S --needed - < a_kde_base.txt
# or
yay -S --needed - < a_kde_base.txt
```
