#!/usr/bin/env python

from os import path
from setuptools import setup

VERSION = "1.0.0"

if __name__ == "__main__":

    # List of all the required packages.
    install_requires = [
        "arcade",
    ]

    # Grab the long description out of the README
    fname = path.join(path.dirname(path.abspath(__file__)), "README.rst")
    with open(fname, "r") as f:
        long_desc = f.read()

    # Call the setup function with our setup parameters.
    # This kicks off the build.
    setup(
        name="arcade",
        version=VERSION,
        description="Sample Python Package",
        long_description=long_desc,
        author="Paul Vincent Craven",
        author_email="paul.craven@simpson.edu",
        license="MIT",
        url="https://pypi-package-example.readthedocs.io/en/latest/",
        install_requires=install_requires,
        packages=["pypi_package_example"],
        python_requires=">=3.6",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        test_suite="tests",
        package_data={"arcade": ["examples/images/*.png"]},
        project_urls={
            "Documentation": "https://pypi-package-example.readthedocs.io/en/latest/",
            "Issue Tracker": "https://github.com/pvcraven/pypi_package_example/issues",
            "Source": "https://github.com/pvcraven/pypi_package_example",
        },
    )
