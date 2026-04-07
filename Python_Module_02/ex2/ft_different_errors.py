#!/usr/bin/env python3
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "string" + 123


def test_error_types() -> None:
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            if i < 4:
                pass
            else:
                print("Operation completed successfully")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {type(e).__name__}: {e}")
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
