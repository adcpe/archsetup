import subprocess

y_refresh = ['yay', '-Syu']
y_install = ['yay', '-S']

p_refresh = ['sudo', 'pacman', '-Syu']
p_install = ['sudo', 'pacman', '-S', '--needed']
subprocess.call(p_refresh)

security = [
    'apparmor',
    'ufw',
]
subprocess.call(p_install + security)

sound = [
    'alsa-ucm-conf',
    'pipewire',
    'pipewire-alsa',
    'pipewire-jack',
    'pipewire-pulse',
    'wireplumber',
]
subprocess.call(p_install + sound)

dev_libs = [
    'djvulibre',
    'gd',
    'ghostscript',
    'icu',
    'imagemagick',
    'imagemagick-doc',
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
    'zlib',
]
subprocess.call(p_install + dev_libs)

compression = [
    'arj',
    'lrzip',
    'lzop',
    'p7zip',
    'unarchiver',
    'unrar'
]
subprocess.call(p_install + compression)

filesystems = [
    'exfat-utils',
    'ntfs-3g',
    'partitionmanager'
]
subprocess.call(p_install + filesystems)

group_1 = [
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
    'xdg-desktop-portal-kde',
]
subprocess.call(p_install + group_1)

group_2 = [
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
subprocess.call(p_install + group_2)

dev = [
    'dbeaver',
    'dbeaver-plugin-office',
    'discord',
    'mariadb',
    'postgresql',
]
subprocess.call(p_install + dev)

virt = [
    'libvirt',
    'qemu-full',
    'virt-manager',
]
subprocess.call(p_install + virt)

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
subprocess.call(p_install + fonts)

other = [
    'bitwarden',
    'github-cli',
    'keepassxc',
    'newsboat',
    'obsidian',
    'pkgstats',
    'rsync',
    'samba',
]
subprocess.call(p_install + other)

aur = [
    'archlinux-artwork',
    'dolphin-megasync-bin',
    'insomnia-bin',
    'megasync-bin',
    'protonvpn-cli',
    'slack-desktop',
    'ttf-ms-fonts',
    'visual-studio-code-bin',
    'zoom',
]
subprocess.call(y_install + aur)

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
