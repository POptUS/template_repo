from pathlib import Path


def compute(x):
    """
    Obtain the result of appyling our main computation to the given data x
    """
    # Print filename so that we can see if we are running from an installed
    # package or from a local clone.
    filename = Path(__file__).resolve()
    print(f"{filename} called")
    return 5.0 * x
