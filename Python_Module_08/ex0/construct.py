import os
import site
import sys


def check_matrix_environment() -> None:
    # Detects and prints the status of the Python environment environment.
    # In a virtual env, sys.prefix shifts away from sys.base_prefix
    is_venv = sys.prefix != sys.base_prefix

    if not is_venv:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")
    else:
        # Extract the name of the directory containing the virtual environment
        venv_name = os.path.basename(sys.prefix)
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("\nPackage installation path:")
        print(f" {site.getsitepackages()[0]}")
        # site.getsitepackages()
        # returns a list of active site-packages locations


if __name__ == "__main__":
    check_matrix_environment()
