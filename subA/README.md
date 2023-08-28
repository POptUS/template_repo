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
Since subA is included in
[mytemplate_pypkg](https://github.com/POptUS/template_repo/tree/main/mytemplate_pypkg/src/mytemplate)
via symlink, it should be tested through that package's testing facilities.
