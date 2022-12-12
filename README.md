# ARCHSETUP

## F.A.Q.

### What is this?

This is a repository with lists of packages that I need on a minimal, good-to-go Arch Linux installation on a new machine.

### How does it work?

Aside from `plasma_config`, `post_install` and, of couse this `README`; all the file are plain text files with names of packages available on the Arch Main Repositories or the Arch User Repositories (AUR).

Together with a [function](https://gitlab.com/adcpe/dots/-/blob/main/.config/fish/functions/ignite.fish) I keep on my dotfiles repo, I parse the contents of each file separately and mass install everything.

### Is this the first iteration of `ARCHSETUP`?

No. Previously I had migrated to Fish scripts with lists of files packages. Each file was a self-executable.

Before that, the first version was the same concept but with Bash scripts.

### Why put so much work on something that is not going to be repeated very often?

True. But I believe that this is preparing me for a worst case scenario.

This latest version also allows me to use any language or tool I see fit in the future, which is also important to me.

### Cool.

Thank you.
