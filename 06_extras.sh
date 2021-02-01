echo -e "\nInstalling extras\n"

PKGS=(
  'keepassxc'
  'discord'
)

for PKG in "${PKGS[@]}"; do
    echo "INSTALLING: ${PKG}"
    sudo pacman -S "$PKG" --noconfirm --needed
done


npm i -g trash-cli

echo -e "\nDone!\n"
