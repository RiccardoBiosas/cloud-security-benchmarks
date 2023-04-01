import os
from pathlib import Path
from checkov.terraform.runner import Runner

repo_root = Path(__file__).resolve().parent.parent.parent.parent
target_directory =  f"{repo_root}/terragoat"

checkov_runner = Runner()
checkov_output = checkov_runner.run(
    root_folder=target_directory,
    external_checks_dir="",
    files=[target_directory],
)

checkov_results = checkov_output.get_dict()["results"]
print(len(checkov_results["failed_checks"]))

for check in checkov_results["failed_checks"]:
    print(check)
