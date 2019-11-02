Core Files and Directories
==========================

There are only two required files, and one required directory:

* ``pypi_package_example`` This is the main project directory
  where all the Python source code goes.
  The directory should be named the same as your package name. Check the
  `PyPi Package Index`_ to make sure there isn't a conflict before picking
  your package name.
* ``pypi_package_example/__init__.py`` This is the starting file for your
  project. It is run when you import your package. It should not do much
  processing, it should just load in all the functions and classes that you
  plan on using in your project.
* ``setup.py`` This specifies how your project is to be built, and other
  meta information about the project. See the example `setup.py`_ for this project.
  Also, see the official `Writing the Setup Script`_ documentation.
  You can build the project with ``python setup.py build``.


.. _PyPi Package Index: https://pypi.org/
.. _setup.py: https://github.com/pvcraven/pypi_package_example/blob/master/setup.py
.. _Writing the Setup Script: https://docs.python.org/3.8/distutils/setupscript.html