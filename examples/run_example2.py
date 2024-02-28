#!/usr/bin/env python

import numpy as np

from mytemplate2 import compute
from mytemplate2.subC import compute_c


def main():
    # ----- HARDCODED VALUES
    # Needed to test this example with CI
    SUCCESS = 0
    FAILURE = 1

    EPS = np.finfo(float).eps

    # ----- RUN EXAMPLE
    x = 1.1
    y = compute(x)
    y_c = compute_c(x)

    print()
    print(f"compute   gave {y} for an input of {x}")
    print(f"compute_c gave {y_c} for an input of {x}")
    print()

    if np.fabs(1.0 + y / 55.0) > EPS:
        print("compute result invalid")
        return FAILURE
    elif np.fabs(1.0 - y_c / 1.331) > 2.0 * EPS:
        print("compute_c result invalid")
        return FAILURE

    return SUCCESS


if __name__ == "__main__":
    exit(main())
