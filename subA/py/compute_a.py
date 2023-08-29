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

    if x < -100:
        print("this line should never be covered")
        k = 1+1
        print("this line also should never be covered")

    return x**2
