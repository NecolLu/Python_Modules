import sys

# Step 1: Gracefully check for missing dependencies
missing_dependencies = []

try:
    import pandas as pd
except ImportError:
    missing_dependencies.append("pandas")

try:
    import numpy as np
except ImportError:
    missing_dependencies.append("numpy")

try:
    import matplotlib
    import matplotlib.pyplot as plt
except ImportError:
    missing_dependencies.append("matplotlib")

# Optional package allowed by the subject
try:
    import requests
except ImportError:
    requests = None  # type: ignore


# If any packages are missing, print clear instructions and stop
if missing_dependencies:
    print("LOADING STATUS: Missing dependencies detected!")
    print(f"The following programs are missing:"
          f" {', '.join(missing_dependencies)}")
    print("\n[To install using pip]:")
    print("  pip install -r requirements.txt")
    print("\n[To install using Poetry]:")
    print("  poetry install")
    sys.exit(1)


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    # Print the exact versions currently installed in the environment
    print(f" [OK] pandas ({pd.__version__}) - Data manipulation ready")
    print(f" [OK] numpy ({np.__version__}) - Numerical computation ready")
    if requests:
        print(
            f" [OK] requests ({requests.__version__}) - Network access ready"
            )
    print(f" [OK] matplotlib ({matplotlib.__version__}) - Visualization ready")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    # Step 2: Generate mock data using numpy (No hardcoded range/lists allowed)
    # This creates 1000 rows of random numbers across 3 columns
    raw_data = np.random.randn(1000, 3)
    df = pd.DataFrame(raw_data, columns=["Signal_Alpha",
                                         "Signal_Beta",
                                         "Sentinels"
                                         ])

    print("Generating visualization...")

    # Step 3: Create a line graph using matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(df["Signal_Alpha"].cumsum(), label="Alpha Stream", color="green")
    plt.plot(df["Signal_Beta"].cumsum(), label="Beta Stream", color="cyan")
    plt.title("Zion Mainframe Data Stream Analysis")
    plt.xlabel("Ticks")
    plt.ylabel("Signal Amplitude")
    plt.legend()

    # Save the chart as an image file
    output_file = "matrix_analysis.png"
    plt.savefig(output_file)

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()
