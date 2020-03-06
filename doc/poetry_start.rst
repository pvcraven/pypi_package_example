Poetry
======

Poetry is a project to make Python packaging and managing dependencies easier.

https://python-poetry.org/

You can install poetry to your system with:

.. code-block:: text
    :caption: Install Poetry on MacOS or Linux:

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

.. code-block:: text
    :caption: Install Poetry using Windows PowerShell:

    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python

.. note::

   In the case of Windows, you need to add ``%USERPROFILE%\.poetry\bin`` to your ``%PATH%``.

Create a project with:

.. code-block:: text

    poetry new poetry-demo

This creates a set of files like:

.. code-block:: text

    poetry-demo
    ├── pyproject.toml
    ├── README.rst
    ├── poetry_demo
    │   └── __init__.py
    └── tests
        ├── __init__.py
        └── test_poetry_demo.py

From here, we can change into the directory and build our project:

.. code-block:: text

    C:\Users\craven\Desktop\poetry-demo>poetry build
    Creating virtualenv poetry-demo-lOj6q_DF-py3.7 in C:\Users\craven\AppData\Local\pypoetry\Cache\virtualenvs
    Building poetry-demo (0.1.0)
     - Building sdist
     - Built poetry-demo-0.1.0.tar.gz

     - Building wheel
     - Built poetry_demo-0.1.0-py3-none-any.whl

    C:\Users\craven\Desktop\poetry-demo>
