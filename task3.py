import sys
from pathlib import Path
from colorama import init, Fore, Style

EXCLUDED_DIRS = {'.git', '.idea', '__pycache__', 'venv'}


def print_directory_tree(path: Path, indent: str = ""):
    try:
        entries = sorted(path.iterdir(), key=lambda e: (not e.is_dir(), e.name.lower()))
    except PermissionError:
        print(indent + Fore.RED + f"[Permission Denied]: {path.name}" + Style.RESET_ALL)
        return

    for entry in entries:
        if entry.name in EXCLUDED_DIRS:
            continue

        if entry.is_dir():
            print(f"{indent}{Fore.BLUE}{entry.name}/{Style.RESET_ALL}")
            print_directory_tree(entry, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")


def main():
    init(autoreset=True)

    root = Path(sys.argv[1]) if len(sys.argv) >= 2 else Path.cwd()

    if not root.is_dir():
        print(f"Error: '{root}' is not a directory.")
        sys.exit(1)

    print_directory_tree(root)


if __name__ == "__main__":
    main()

