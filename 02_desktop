#!/usr/bin/env bash

echo -e "\nInstalling Desktop Environment\n"

PKGS=(
  'sddm'                   # window manager
  'sddm-kcm'               # wm config tool
  'plasma'                 # desktop environment
  'kde-system'             # desktop environment

  # Desktop environment base programs
  'dolphin'                # file explorer
  'ark'                    # (de)compression tool
  'gwenview'               # image viewer
  'kate'                   # text editor
  'okular'                 # document viewer
  'kcalc'                  # calculator
  'spectacle'              # screenshots
  'kcolorchooser'          # color chooser
  'ktorrent'               # torrents
  'redshift'               # screen color temperature adjuster
  'celluloid'              # video player
  'cantata'                # music player
  'ktimer'
  'kfind'
  'kdialog'

  # office suite
  'libreoffice-fresh'
  'hunspell-en_US'
  'hunspell-es_pe'
  'hyphen-en'
  'hyphen-es'
)

DEPS=(
  'mpd'                   # music player daemon
)

for PKG in "${PKGS[@]}"; do
    echo "INSTALLING: ${PKG}"
    sudo pacman -S "$PKG" --noconfirm --needed
done

for DEP in "${DEPS[@]}"; do
    echo "INSTALLING: ${DEP}"
    sudo pacman -S "$DEP" --noconfirm --needed --asdeps
done

sudo systemctl enable sddm.service
sudo systemctl enable NetworkManager

echo -e "\nDone!\n"
