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

    process.wait()
    if process.returncode != 0:
        print(f'\nCommand failed: {command}')
        exit(1)


post_install = [
    'sudo systemctl enable --now apparmor',
    'sudo systemctl enable --now ufw',
    'sudo ufw enable',
    'sudo systemctl start pkgstats.timer',
    'sudo systemctl enable --now bluetooth',
    'sudo systemctl enable --now sddm',
]

for task in post_install:
    print(task + '\n')
    run_command(task)
