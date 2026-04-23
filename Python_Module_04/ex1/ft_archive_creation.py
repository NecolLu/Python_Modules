#!/usr/bin/env python3
import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename)
        print("---")

        content: str = file.read()
        print(content, end="")

        print("---")
        file.close()
        print(f"File '{filename}' closed.")

        # Transform data
        print("Transform data:")
        print("---")

        lines = content.splitlines()
        new_content: str = ""

        for line in lines:
            new_content += line + "#\n"

        print(new_content, end="")
        print("---")

        # Ask user if want to save data
        new_filename: str = input("Enter new file name (or empty): ")

        if new_filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")

            new_file = open(new_filename, "w")
            new_file.write(new_content)
            new_file.close()

            print(f"Data saved in file '{new_filename}'.")

    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
