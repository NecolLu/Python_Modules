#!/usr/bin/env python3
import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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

        # Transform
        print("Transform data:")
        print("---")

        lines = content.splitlines()
        new_content: str = ""

        for line in lines:
            new_content += line + "#\n"

        print(new_content, end="")
        print("---")

        # Input without input()
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_filename: str = sys.stdin.readline().rstrip("\n")

        if new_filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")
            try:
                new_file = open(new_filename, "w")
                new_file.write(new_content)
                new_file.close()
                print(f"Data saved in file '{new_filename}'.")
            except Exception as e:
                sys.stderr.write(
                        f"[STDERR] Error opening file '{new_filename}': {e}\n"
                    )
                print("Data not saved.")

    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")


if __name__ == "__main__":
    main()
