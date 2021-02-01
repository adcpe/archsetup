#!/usr/bin/env bash

echo -e "\nInstalling AUR packages\n"

git clone https://aur.archlinux.org/yay.git ~/yay
cd ~/yay
makepkg -si

PKGS=(
  'slack-desktop'
  'insomnia'
  'heroku-cli'
  'exercism-bin'
  'etcher-bin'
  'zoom'
  'skypeforlinux-stable-bin'
  'onedrive-abraunegg'
)

for PKG in "${PKGS[@]}"; do
    echo "INSTALLING: ${PKG}"
    yay -S "$PKG" --noconfirm --needed
done

echo -e "\nDone!\n"
