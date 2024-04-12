import mytemplate


def run_my_example():
    """
    This is a function that serves as an example/tutorial that we would point
    people toward to help them learn and understand our interface.

    Given this special role, we want to know at all times that it runs through
    and produces correct results.  In this case, by including this example in
    the repo we can also package it up inside a unittest TestCase (see
    tests/TestExample).  Part of this double role is that the example can
    function as a pass/fail system-level test in our suite.

    Since this function is written outside of the unittest framework, it cannot
    use any of the self.assert* routines.  Testing should be via assert
    statements, which are trapped by the TestCase wrapper and registered with
    the framework as a failure.
    """
    x = 1.1
    y = mytemplate.compute(x)

    print()
    print(f"compute gave me {y} for input {x}")
    print()
    assert y == 5.5
