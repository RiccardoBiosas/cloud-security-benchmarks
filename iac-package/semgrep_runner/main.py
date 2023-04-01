import subprocess
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent.parent
target_directory =  f"{repo_root}/terragoat"

command = [
    "docker", "run", "--rm", "-v",
    f"{target_directory}:/src", "returntocorp/semgrep",
    "--config=auto",
]

try:
    semgrep_output = subprocess.run(command, stdout=subprocess.PIPE)
    print(semgrep_output)
    print(semgrep_output.stdout.decode())
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    print(e.stderr.decode())
