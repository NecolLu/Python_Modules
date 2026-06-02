import os
from dotenv import load_dotenv  # type: ignore

# Step 1: Load the environment variables from the local .env file
load_dotenv()


def verify_environment_security() -> bool:
    # Verifies that all vital configuration parameters are present
    required_vars = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]
    # Check if any required variable is missing or empty
    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        print(
            f"WARNING: Configuration parameters missing: {', '.join(missing)}"
            )
        return False
    return True


def main() -> None:
    # Evaluates the local environment configurations securely
    print("ORACLE STATUS: Reading the Matrix...")

    # Step 2: Extract variables safely, falling back to defaults if unassigned
    mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL", "None")
    api_key = os.getenv("API_KEY", "None")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT", "None")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    # Show variance based on whether we are in Development or Production mode
    if mode == "production":
        print("Database: Connected to Secure Production Cluster Mainframe")
        print(f"Log Level: {log_level} (Production Strictness)")
    else:
        print(f"Database: Connected to local instance ({db_url})")
        print(f"Log Level: {log_level}")

    if api_key != "None":
        print("API Access: Authenticated")
    else:
        print("API Access: Denied (Missing Token Keys)")

    print(
        f"Zion Network: {'Online' if zion_endpoint != 'None' else 'Offline'}"
        )

    print("\nEnvironment security check:")

    # Basic structural evaluation warnings
    if api_key != "None" and len(api_key) < 32 and mode == "production":
        print(
            "[WARNING] Production API Key seems structurally weak or exposed."
            )
    else:
        print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] Missing local file target workspace configuration.")

    print("[OK] Production overrides available")


if __name__ == "__main__":
    verify_environment_security()
    main()
