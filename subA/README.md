subA Amazing Optimization Method
======================================
We are pretending that this is an optimization tool such as POUNDERS with a
MATLAB and a Python implementation.  Please see
[POUNDERS](https://github.com/POptUS/IBCDFO/blob/main/pounders) for an concrete
example of a tool implementation.

We imagine that optimization method subA shares some commonality with a
different optimization method subB so that it is sensible for both to be
packaged together for distribution in the single python package
[mytemplate_pypkg](https://github.com/POptUS/template_repo/tree/main/mytemplate_pypkg/src/mytemplate).
However, since subA and subB are separate tools, they are located in the root of
the repo as separate folders for independent development.

Testing
=======
The subA package has unit testing integrated via the [Python `unittest` framework](https://docs.python.org/3/library/unittest.html).

## Executing tests
Since subA is included in
[mytemplate_pypkg](https://github.com/POptUS/template_repo/tree/main/mytemplate_pypkg/src/mytemplate)
via symlink, it should be tested through that package's testing facilities.

## Adding a new test case of subA functionality
The sub-package is constructed so that it can automatically locate all test cases whose filenames match the pattern `tests/Test*.py`.  The full set of tests in subA can be accessed by the main package with
[load_tests.py](https://github.com/POptUS/template_repo/blob/main/subA/py/load_tests.py), which follows the `unittest`
[load_tests protocol](https://docs.python.org/3/library/unittest.html?highlight=load_tests#load-tests-protocol).

To add a new test case to the subA test suite, create the new file by executing
```
$ cd subA/py/tests
$ cp TestTemplate.py Test<Test Case Name>.py
```
Edit the file and
* Change the name of the class to `Test<Test Case Name>`
* Delete `setup` and `teardown` if they will not be needed; write, otherwise.
* Rename `testNothing` with `test<First Test Name>` and write
* Add more tests to the case as needed and with each function starting with `test`
