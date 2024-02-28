#!/bin/bash

#
# This returns exit codes that are compatible with the use of this
# script in CI jobs
#

SCRIPT_PATH=$(dirname -- "${BASH_SOURCE[0]}")
REPO_PATH=$SCRIPT_PATH/..

declare -a PACKAGES=("mytemplate_pypkg"
                     "mytemplate2_pypkg")
declare -a FOLDERS=("tools"
                    "examples")

pushd $REPO_PATH

# Let each python package determine if its code is acceptable
for pkg in "${PACKAGES[@]}"; do
    pushd $pkg &> /dev/null
    tox -r -e check || exit $?
    popd &> /dev/null
done

# Load virtual env so that flake8 is available and ...
pushd "${PACKAGES[0]}" &> /dev/null
. ./.tox/check/bin/activate || exit $?
popd &> /dev/null

# manually check python code *not* included in a package
for dir in "${FOLDERS[@]}"; do
    echo
    echo "Check python code in $dir/* ..."
    pushd $dir &> /dev/null
    flake8 --config=./.flake8 || exit $?
    popd &> /dev/null
done
echo
