import subprocess
import os

try:
    result = subprocess.run(['tfsec', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print("tfsec is already installed.")
        print(result.stdout.decode())
except FileNotFoundError:
    # see here: https://github.com/aquasecurity/tfsec/tree/fbca9334c6660988b8c75a57c88d79e1ca6462d8 under `Bash script (Linux):`
    cmd = 'curl -s https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install_linux.sh | bash'
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    if result.returncode == 0:
        print("tfsec successfully installed.")
    else:
        print("failed to install tfsec.")
        print(result.stderr.decode())

print(f"original root {os.getcwd()}")
directory =  f"{ os.getcwd()}/terragoat"
os.chdir(directory)
print(f"switched root {os.getcwd()}")

command = f"tfsec --debug"


try:
    tfsec_output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(tfsec_output.stdout.decode())
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    print(e.stderr.decode())
