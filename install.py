import subprocess

yay_install = ['yay', '-S']

pacman_refresh = ['sudo', 'pacman', '-Syu']
pacman_install = ['sudo', 'pacman', '-S', '--needed']
subprocess.call(pacman_refresh)

security = [
    'apparmor',
    'ufw',
]
subprocess.call(pacman_install + security)

sound = [
    'alsa-ucm-conf',
    'pipewire',
    'pipewire-alsa',
    'pipewire-jack',
    'pipewire-pulse',
    'wireplumber',
]
subprocess.call(pacman_install + sound)

dev_libs = [
    'djvulibre',
    'gd',
    'ghostscript',
    'icu',
    'imagemagick',
    'libheif',
    'libraw',
    'librsvg',
    'libwebp',
    'libwmf',
    'libxml2',
    'libxslt',
    'libzip',
    'ocl-icd',
    'oniguruma',
    'openexr',
    'openjpeg2',
    'pango',
    'postgresql-libs',
    're2c',
    'tk',
    'zlib',
]
subprocess.call(pacman_install + dev_libs)

compression = [
    'arj',
    'lrzip',
    'lzop',
    'p7zip',
    'unarchiver',
    'unrar'
]
subprocess.call(pacman_install + compression)

filesystems = [
    'exfat-utils',
    'ntfs-3g',
    'partitionmanager'
]
subprocess.call(pacman_install + filesystems)

base_tools = [
    'base-devel',
    'bat',
    'bat-extras',
    'exa',
    'htop',
    'kitty',
    'man-db',
    'openssh',
    'reflector',
    'xclip',
    'xdg-user-dirs',
    'xdg-desktop-portal',
    'xdg-desktop-portal-kde',
]
subprocess.call(pacman_install + base_tools)

desktop_environment = [
    'alsa-ucm-conf',
    'ark',
    'bluez',
    'bluez-utils',
    'chromium',
    'dolphin',
    'firefox',
    'fwupd',
    'gnome-keyring',
    'gwenview',
    'hunspell-en_US',
    'hunspell-es_pe',
    'hyphen-en',
    'hyphen-es',
    'kate',
    'kcalc',
    'kcolorchooser',
    'kcron',
    'kdialog',
    'kfind',
    'khelpcenter',
    'ksystemlog',
    'ktimer',
    'kwalletmanager',
    'kwallet-pam',
    'libreoffice-still',
    'libsecret',
    'networkmanager-openvpn',
    'okular',
    'openvpn',
    'packagekit-qt5',
    'plasma-pa',
    'plasma',
    'qbittorrent',
    'sof-firmware',
    'spectacle',
    'starship',
    'vlc',
]
subprocess.call(pacman_install + desktop_environment)

dev_tools = [
    'dbeaver',
    'dbeaver-plugin-office',
    'discord',
    'mariadb',
    'postgresql',
]
subprocess.call(pacman_install + dev_tools)

virt = [
    'libvirt',
    'qemu-full',
    'virt-manager',
]
subprocess.call(pacman_install + virt)

fonts = [
    'gnu-free-fonts',
    'noto-fonts',
    'otf-fira-mono',
    'otf-font-awesome',
    'ttc-iosevka',
    'ttf-anonymous-pro',
    'ttf-bitstream-vera',
    'ttf-croscore',
    'ttf-dejavu',
    'ttf-droid',
    'ttf-hack',
    'ttf-ibm-plex',
    'ttf-inconsolata',
    'ttf-liberation',
    'ttf-linux-libertine',
    'ttf-roboto',
    'ttf-ubuntu-font-family',
]
subprocess.call(pacman_install + fonts)

various = [
    'bitwarden',
    'github-cli',
    'keepassxc',
    'newsboat',
    'obsidian',
    'pkgstats',
    'rsync',
    'samba',
]
subprocess.call(pacman_install + various)

aur = [
    'archlinux-artwork',
    'insomnia-bin',
    'protonvpn-cli',
    'slack-desktop',
    'ttf-ms-fonts',
    'visual-studio-code-bin',
    'zoom',
]
subprocess.call(yay_install + aur)

post_install = [
    ['sudo', 'systemctl', 'enable', '--now', 'apparmor'],
    ['sudo', 'systemctl', 'enable', '--now', 'ufw'],
    ['sudo', 'ufw', 'enable'],
    ['sudo', 'systemctl', 'enable', 'sddm'],
    ['sudo', 'systemctl', 'enable', 'bluetooth'],
    ['sudo', 'usermod', '-aG', 'libvirt', 'adc'],
    ['sudo', 'systemctl', 'start', 'pkgstats.timer'],
]

for cmd in post_install:
    subprocess.call(cmd)
