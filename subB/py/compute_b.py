from pathlib import Path


def compute_b(x):
    r"""
    :param x: :math:`x \in \R`
    :return: :math:`x^3`
    """
    # Print filename so that we can see if we are running from an installed
    # package or from a local clone.
    filename = Path(__file__).resolve()
    print()
    print(f"{filename} called")
    return x**3
