echo -e "\nInstalling Essential Tools\n"

PKGS=(
  'kitty'                   # terminal
  'exa'                     # ls
  'bat'                     # cat
  'htop'                    # task manager
  'neofetch'                # system info
  'systemd-swap'            # swap

  # file system and partition tools
  'exfat-utils'
  'ntfs-3g'
  'gparted'
)

TOOLS=(
  # archiving tools
  'lrzip'
  'lrzop'
  'p7zip'
  'unarchiver'
  'unrar'
)

for PKG in "${PKGS[@]}"; do
    echo "INSTALLING: ${PKG}"
    sudo pacman -S "$PKG" --noconfirm --needed
done
for TOOL in "${TOOLS[@]}"; do
    echo "INSTALLING: ${TOOL}"
    sudo pacman -S "$TOOL" --noconfirm --needed --asdeps
done

sudo systemctl enable systemd-swap

echo -e "\nDone!\n"
