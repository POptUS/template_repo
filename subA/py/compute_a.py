from pathlib import Path


def compute_a(x):
    """
    Obtain the result of appyling computation A to the given data x
    """
    # Print filename so that we can see if we are running from an installed
    # package or from a local clone.
    filename = Path(__file__).resolve()
    print()
    print(f"{filename} called")
    return x**2
