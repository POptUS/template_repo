import codecs
from pathlib import Path

from setuptools import setup

_PKG_ROOT = Path(__file__).resolve().parent


def readme_md():
    fname = _PKG_ROOT.joinpath("README.md")
    with codecs.open(fname, encoding="utf8") as fptr:
        return fptr.read()


def version():
    fname = _PKG_ROOT.joinpath("VERSION")
    with open(fname, "r") as fptr:
        return fptr.read().strip()


# Changes made to python_requires should be propagated to all tox.ini and all
# GitHub Action config files.
python_requires = ">=3.8"
code_requires = []
test_requires = ["numpy"]
install_requires = code_requires + test_requires

package_data = {
    "mytemplate": [
        "tests/*.csv",
        "PkgData/*.json",
        "subA/tests/*.csv",
    ]
}

project_urls = {
    "Source": "Git Hub",
    "Documentation": "httpx://mytemplate.org",
    "Tracker": "Git Hub Issues",
}

setup(
    name="mytemplate",
    version=version(),
    author="me",
    author_email="me@me.org",
    maintainer="me",
    maintainer_email="me@me.org",
    package_dir={"": "src"},
    package_data=package_data,
    url="https://mytemplate.org",
    project_urls=project_urls,
    license="MIT",
    description="Personal, custom tools for stuff",
    long_description=readme_md(),
    long_description_content_type="text/markdown",
    python_requires=python_requires,
    install_requires=install_requires,
    keywords="My Template Stuff",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Topic :: Scientific/Engineering",
    ],
)
