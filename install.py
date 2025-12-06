import os
import shutil
import subprocess


# reusable function
def run_command(command, cwd=None):
    # print(command)
    process = subprocess.Popen(
        command,
        shell=True,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    for line in process.stdout:  # type: ignore
        print(line, end='')      # print live output

    process.wait()
    if process.returncode != 0:
        print(f'\nCommand failed: {command}')
        exit(1)
    print('')


# check if ~/yay exists, delete it and then install yay
yay_dir = os.path.expanduser('~') + '/yay'

if os.path.exists(yay_dir) and os.path.isdir(yay_dir):
    shutil.rmtree(yay_dir)

run_command('git clone https://aur.archlinux.org/yay-bin.git ' + yay_dir)
run_command('makepkg -si --noconfirm', cwd=yay_dir)

# enable colored output & update all packages and repos
run_command('yay -Syyu --combinedupgrade --save')


# start system installation
yay_install = ['yay -S --needed']

security = [
    'apparmor',
    'ufw',
]
run_command(' '.join(yay_install + security))

sound = [
    'alsa-ucm-conf',
    'pipewire',
    'pipewire-alsa',
    'pipewire-jack',
    'pipewire-pulse',
    'wireplumber',
]
run_command(' '.join(yay_install + sound))

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
run_command(' '.join(yay_install + dev_libs))

compression = [
    'arj',
    'lrzip',
    'lzop',
    'p7zip',
    'unarchiver',
    'unrar',
    'unzip',
]
run_command(' '.join(yay_install + compression))

filesystems = [
    'exfat-utils',
    'ntfs-3g',
    'partitionmanager',
]
run_command(' '.join(yay_install + filesystems))

terminal_utilities = [
    'base-devel',
    'bat',
    'bat-extras',
    'exa',
    'fastfetch',
    'htop',
    'kitty',
    'man-db',
    'openssh',
    'reflector',
    'starship',
    'xclip',
]
run_command(' '.join(yay_install + terminal_utilities))

desktop_environment = [
    'alsa-ucm-conf',
    'ark',
    'bluez',
    'bluez-utils',
    'chromium',
    'dolphin',
    'firefox',
    'foliate',
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
    'vlc',
    'xdg-user-dirs',
    'xdg-desktop-portal',
    'xdg-desktop-portal-kde',
]
run_command(' '.join(yay_install + desktop_environment))

dev_tools = [
    'dbeaver',
    'dbeaver-plugin-office',
    'discord',
    'mariadb',
    'postgresql',
]
run_command(' '.join(yay_install + dev_tools))

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
    'ttf-libertinus',
    'ttf-roboto',
    'ttf-ubuntu-font-family',
    'ttf-delugia-code',
    'ttf-victor-mono-nerd',
    'ttf-cascadia-code',
    'ttf-cascadia-code-nerd',
    'ttf-cascadia-mono-nerd',
    'ttf-mononoki-nerd',
]
run_command(' '.join(yay_install + fonts))

various = [
    'github-cli',
    'keepassxc',
    'obsidian',
    'pkgstats',
    'samba',
]
run_command(' '.join(yay_install + various))

aur = [
    'archlinux-artwork',
    'insomnia-bin',
    'ttf-ms-fonts',
    'visual-studio-code-bin',
    'zen-browser-bin',
]
run_command(' '.join(yay_install + aur))

theming = [
    'plasma6-themes-qogir-git',
    'qogir-icon-theme',
    'qogir-gtk-theme',
    'qogir-cursor-theme',
    'layan-gtk-theme-git',
    'layan-cursor-theme-git',
    'plasma6-themes-layan-git',
    'plasma6-themes-orchis-kde-git',
    'orchis-theme-git',
    'tela-circle-icon-theme-all',
]
run_command(' '.join(yay_install + theming))

# enable services
post_install = [
    'sudo systemctl enable --now apparmor',
    'sudo systemctl enable --now ufw',
    'sudo ufw enable',
    'sudo systemctl start pkgstats.timer',
    'sudo systemctl enable --now bluetooth',
    'sudo systemctl enable --now sddm',
]

for task in post_install:
    run_command(task)
