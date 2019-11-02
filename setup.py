#!/usr/bin/env python

from os import path
import sys
from setuptools import setup

BUILD = 0
VERSION = "1.0.0"
RELEASE = VERSION

if __name__ == "__main__":

    # List of all the required packages.
    install_requires = [
        'arcade',
    ]

    # This project uses data classes. But data clases were introduced in 3.7.
    # So if we are using 3.6, use an add-on package that backports it.
    if sys.version_info[0] == 3 and sys.version_info[1] == 6:
        install_requires.append('dataclasses')

    if "--format=msi" in sys.argv or "bdist_msi" in sys.argv:
        # hack the version name to a format msi doesn't have trouble with
        VERSION = VERSION.replace("-alpha", "a")
        VERSION = VERSION.replace("-beta", "b")
        VERSION = VERSION.replace("-rc", "r")

    # Grab the long description out of the README
    fname = path.join(path.dirname(path.abspath(__file__)), "README.rst")
    with open(fname, "r") as f:
        long_desc = f.read()

    # Here are our setup parameters
    setup(
          name="arcade",
          version=RELEASE,
          description="Sample Python Package",
          long_description=long_desc,
          author="Paul Vincent Craven",
          author_email="paul.craven@simpson.edu",
          license="MIT",
          url="https://pypi-package-example.readthedocs.io/en/latest/",
          download_url="http://arcade.academy",
          install_requires=install_requires,
          packages=["pypi_package_example",
                    ],
          python_requires='>=3.6',
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
          package_data={'arcade': ['examples/images/*.png']},
          project_urls={
                        'Documentation': 'https://pypi-package-example.readthedocs.io/en/latest/',
                        'Issue Tracker': 'https://github.com/pvcraven/pypi_package_example/issues',
                        'Source': 'https://github.com/pvcraven/pypi_package_example',
          },
         )
