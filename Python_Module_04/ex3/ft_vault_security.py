#!/usr/bin/env python3
def secure_archive(
    filename: str,
    mode: str = "r",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if mode == "r":
            with open(filename, "r") as f:
                data = f.read()
            return (True, data)

        elif mode == "w":
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")

        else:
            return (False, "Invalid mode")

    except Exception as e:
        return (False, str(e))


# Example usage for testing (matches your briefing example)
if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    # Test 1: Nonexistent file
    print(f"Reading nonexistent:\n{secure_archive('ghost_file.txt', 'r')}\n")

    # Test 2: Writing to a file
    secret_data = "[FRAGMENT 001] Knowledge must survive the entropy wars."
    print(
        f"Writing content:\n"
        f"{secure_archive('vault_alpha.txt', 'w', secret_data)}\n"
    )

    # Test 3: Reading the new file
    print(f"Reading regular file:\n{secure_archive('vault_alpha.txt', 'r')}")
