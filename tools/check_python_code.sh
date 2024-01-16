#!/bin/bash

#
# This returns exit codes that are compatible with the use of this
# script in CI jobs
#

SCRIPT_PATH=$(dirname -- "${BASH_SOURCE[0]}")
REPO_PATH=$SCRIPT_PATH/..

declare -a PACKAGES=("mytemplate_pypkg"
                     "mytemplate2_pypkg")

pushd $REPO_PATH

# Let each python package determine if its code is acceptable
for pkg in "${PACKAGES[@]}"; do
    pushd $pkg
    tox -r -e check || exit $?
    popd
done

# Load virtual env so that flake8 is available and ...
pushd "${PACKAGES[0]}"
. ./.tox/check/bin/activate || exit $?
popd

# manually check python code *not* included in a package
echo
echo "Check python code in tools/* ..."
pushd tools
flake8 --config=./.flake8 || exit $?
popd
echo

popd
