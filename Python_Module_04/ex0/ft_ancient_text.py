#!/usr/bin/env python3
import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename)
        print("---")
        content = file.read()
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
