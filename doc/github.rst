GitHub and GitHub Community
===========================

If you host your files on GitHub, they have recommended supporting files for
documentation.

* ``README.md`` or ``README.rst`` This file is shown at the bottom of your
  GitHub page. It (along with most other files) can be in Markdown or Restructured
  Text format. Look at the bottom of the `pypi_package_example GitHub site`_ for
  this website's Read Me. You can click on the `README.rst`_ to see this file,
  and hit the 'Raw' button to see the source.

  * Badges - Badges are small graphics you can stick on your site to visually
    list information about your project. See this project's `README.rst`_.

* ``CODE_OF_CONDUCT.md`` Public projects should have a code of conduct. Add it
  before you need one, not after. See GitHub's `Code of Conduct`_ suggestions,
  and the `Contributor Covenant`_ for open source projects.
* ``CONTRIBUTING.md`` Encourage contributions to your project by telling
  interested developers how to get started.
* ``license.md`` Post a license for how people can use the software. See
  `Choose a License`_ for help in selecting one.
* ``.github/ISSUE_TEMPLATE/bug_report.md`` When people report a bug, GitHub
  will use the contents of this file as a template. This file, and similar ones
  like ``pull_request_template.md`` have a few different places they can reside
  in. I like putting them in ``.github`` rather than pollute the root directory.
  You can also have multiple templates, depending on if it is a bug, feature
  request, etc.
* ``.github/PULL_REQUEST_TEMPLATE/pull_request_template.md`` When developers create
  a pull request a bug, GitHub will use the contents of this file as a template.

.. _pypi_package_example GitHub site: https://github.com/pvcraven/pypi_package_example
.. _README.rst: https://github.com/pvcraven/pypi_package_example/blob/master/README.rst
.. _Code of Conduct: https://help.github.com/en/github/building-a-strong-community/adding-a-code-of-conduct-to-your-project
.. _Contributor Covenant: https://www.contributor-covenant.org/
.. _Choose a License: https://choosealicense.com/
