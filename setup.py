#!/usr/bin/env python

from setuptools import setup

from pypi_package_example import __version__

if __name__ == "__main__":

    # Call the setup function with our setup parameters.
    # This kicks off the build.
    setup(version=__version__)
