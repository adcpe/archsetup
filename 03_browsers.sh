echo -e "\nInstalling Browsers\n"

PKGS=(
  'min'
  'firefox'
)

for PKG in "${PKGS[@]}"; do
    echo "INSTALLING: ${PKG}"
    sudo pacman -S "$PKG" --noconfirm --needed
done

echo -e "\nDone!\n"
