echo -e "\nInstalling fonts\n"

PKGS=(
  # fonts
  'noto-fonts-emoji'
  'otf-fira-mono'
  'ttf-anonymous-pro'
  'ttf-fantasque-sans-mono'
  'ttf-fira-code'
  'ttf-fira-mono'
  'ttf-inconsolata'
  'ttf-linux-libertine'
  'ttf-roboto'
  'ttf-ubuntu-font-family'
  'xorg-fonts'

  # ttf-fonts
  'gnu-free-fonts'
  'noto-fonts'
  'ttf-bitstream-vera'
  'ttf-croscore'
  'ttf-dejavu'
  'ttf-droid'
  'ttf-font-awesome'
  'ttf-ibm-plex'
  'ttf-liberation'
)

AURPKGS=(
  'nerd-fonts-terminus'
  'nerd-fonts-victor-mono'
  'ttf-dejavu-emojiless'
  'ttf-ms-fonts'
)

sudo pacman -S ttf-font --needed

for PKG in "${PKGS[@]}"; do
    echo "INSTALLING: ${PKG}"
    sudo pacman -S "$PKG" --noconfirm --needed
done

for AURPKG in "${AURPKGS[@]}"; do
    echo "INSTALLING: ${AURPKG}"
    sudo pacman -S "$AURPKG" --noconfirm --needed
done

echo -e "\nDone!\n"
