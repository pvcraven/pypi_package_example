Building and Deployment
=======================

* ``/requirements.txt`` This should be a simple list of every package required
  to *develop* your project. The packages required to *run* the project go in
  setup.py. This file makes it easy for automatic setup of virtual environment,
  and automated builds.
* ``/setup.py`` This is one of the two required files.
  You can use the setup file to build the project. For more info,
  refer back to :ref:`core`.
* ``/make.bat``, ``make.sh``, ``make.py`` There are so many different commands for building, testing,
  and deployment, I like having a "make" file with a instructions to make the process easier.
* ``/build/`` This is automatically created by setup.py when you build.
* ``/dist/`` This is automatically created by setup.py when we build wheels.

Additional Build Info
---------------------
* bdist / wheels - If you have the **wheel** package installed, you can create a
  one-file distribution of your project. If the project is pure Python, that wheel
  can work on any platform. If you've got platform-specific libraries, you can
  make wheels for each platform. See Python's `packaging projects`_ for more info.
* Twine - You can upload your project to the PyPi repository got other people to use, with the
  twine_ module.
* AWS - If you deploy on a server, Amazon Web Services has a great Python-based command-line
  interface.

.. _packaging projects: https://packaging.python.org/tutorials/packaging-projects/
.. _twine: https://github.com/pypa/twine
