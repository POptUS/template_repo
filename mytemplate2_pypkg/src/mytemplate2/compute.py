from pathlib import Path


def compute(x):
    r"""
    :param x: :math:`x \in \R`
    :return: :math:`-50 x`
    """
    # Print filename so that we can see if we are running from an installed
    # package or from a local clone.
    filename = Path(__file__).resolve()
    print(f"{filename} called")
    return -50.0 * x
