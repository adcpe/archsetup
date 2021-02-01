#!/usr/bin/env bash

echo -e "\nInstalling devtools\n"

PKGS=(
  'postgresql'
  'redis'
  'nodejs'
  'ruby'
  'python'
)

AURPKGS=(
  'visual-studio-code-bin'
)

for PKG in "${PKGS[@]}"; do
    echo "INSTALLING: ${PKG}"
    sudo pacman -S "$PKG" --noconfirm --needed
done

for AURPKG in "${AURPKGS[@]}"; do
    echo "INSTALLING: ${AURPKG}"
    yay -S "$AURPKG" --noconfirm --needed
done

# install asdf - version manager for different languages
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.8.0

# import the Node.js release team's OpenPGP keys to main keyring
bash -c '${ASDF_DATA_DIR:=$HOME/.asdf}/plugins/nodejs/bin/import-release-team-keyring'

asdf plugin add nodejs
asdf plugin add php
asdf plugin add python
asdf plugin add ruby
asdf plugin add rust
asdf install

# copying completions for fish
mkdir -p ~/.config/fish/completions
cp ~/.asdf/completions/asdf.fish ~/.config/fish/completions

echo -e "\nDone!\n"
