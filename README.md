# Bliss

_**Originally written for my [Pydough](https://github.com/Stephen-RA-King/pydough) cookiecutter project. 'Burden' uses the ridiculously usefull invoke library to automate**_
_**numerous project maintenance and publishing tasks.**_

![](assets/bliss.png)

[Invoke][invoke-url] provides a clean, high level API for running shell commands and defining/organizing task functions from a tasks.py file:

## Installation

Copy the "tasks.py.jinja" file to the root of your project (remove jinja suffix)

## Usage example

Burden provides the following tasks...

```shell
inv --list
Available tasks:

  bandit                     Runs bandit against selected python files.
  build                      Creates a new sdist & wheel build using the PyPA tool.
  clean                      Removes all test, build, log and lint artifacts from the environment.
  docs                       Build documentation.
  lint                       Run all lint tasks on 'src' files only.
  lint-all                   Run all lint tasks on all files.
  lint-black (bl, black)     Runs black formatter against selected python files.
  lint-flake8 (fl, flake8)   Run flake8 against selected files.
  lint-isort (is, isort)     Run isort against selected python files.
  mypy                       Run mypy against selected python files.
  psr                        Runs semantic-release publish.
  publish                    Uploads a build to the PyPI-test and PyPI python repositories.
  pypi                       Uploads a build to the PyPI python repository.
  pypi-test                  Uploads a build to the PyPI-test python repository.
  safety                     Runs safety to check for insecure requirements.
  secure                     Runs all security tools.
  tests                      Run tests using pytest.
  update                     Updates the development environment
```

## Meta

[![](assets/linkedin.png)](https://www.linkedin.com/in/sr-king)
[![](assets/github.png)](https://github.com/Stephen-RA-King)
[![](assets/pypi.png)](https://pypi.org/project/bliss)
[![](assets/www.png)](https://www.justpython.tech)
[![](assets/email.png)](mailto:sking.github@gmail.com)

Stephen R A King : [sking.github@gmail.com](mailto:sking.github@gmail.com)

Distributed under the MIT license. See [license][license-url] for more information.

Created with Cookiecutter template: [**pydough**][pydough-url] version 1.2.1

<!-- Markdown link & img dfn's -->

[bandit-image]: https://img.shields.io/badge/security-bandit-yellow.svg
[bandit-url]: https://github.com/PyCQA/bandit
[black-image]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[pydough-url]: https://github.com/Stephen-RA-King/pydough
[codeclimate-image]: https://api.codeclimate.com/v1/badges/7fc352185512a1dab75d/maintainability
[codeclimate-url]: https://codeclimate.com/github/Stephen-RA-King/bliss/maintainability
[codecov-image]: https://codecov.io/gh/Stephen-RA-King/bliss/branch/main/graph/badge.svg
[codecov-url]: https://app.codecov.io/gh/Stephen-RA-King/bliss
[codefactor-image]: https://www.codefactor.io/repository/github/Stephen-RA-King/bliss/badge
[codefactor-url]: https://www.codefactor.io/repository/github/Stephen-RA-King/bliss
[codeql-image]: https://github.com/Stephen-RA-King/bliss/actions/workflows/codeql-analysis.yml/badge.svg
[codeql-url]: https://github.com/Stephen-RA-King/bliss/actions/workflows/codeql-analysis.yml
[commitizen-image]: https://img.shields.io/badge/commitizen-friendly-brightgreen.svg
[commitizen-url]: http://commitizen.github.io/cz-cli/
[conventional-commits-image]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square
[conventional-commits-url]: https://conventionalcommits.org
[deepsource-image]: https://static.deepsource.io/deepsource-badge-light-mini.svg
[deepsource-url]: https://deepsource.io/gh/Stephen-RA-King/bliss/?ref=repository-badge
[downloads-image]: https://static.pepy.tech/personalized-badge/bliss?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads
[downloads-url]: https://pepy.tech/project/bliss
[format-image]: https://img.shields.io/pypi/format/bliss
[invoke-url]: https://github.com/pyinvoke/invoke
[isort-image]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[isort-url]: https://github.com/pycqa/isort/
[lgtm-alerts-image]: https://img.shields.io/lgtm/alerts/g/Stephen-RA-King/bliss.svg?logo=lgtm&logoWidth=18
[lgtm-alerts-url]: https://lgtm.com/projects/g/Stephen-RA-King/bliss/alerts/
[lgtm-quality-image]: https://img.shields.io/lgtm/grade/python/g/Stephen-RA-King/bliss.svg?logo=lgtm&logoWidth=18
[lgtm-quality-url]: https://lgtm.com/projects/g/Stephen-RA-King/bliss/context:python
[license-image]: https://img.shields.io/pypi/l/bliss
[license-url]: https://github.com/Stephen-RA-King/bliss/blob/main/license
[mypy-image]: http://www.mypy-lang.org/static/mypy_badge.svg
[mypy-url]: http://mypy-lang.org/
[pre-commit-image]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-url]: https://github.com/pre-commit/pre-commit
[pre-commit.ci-image]: https://results.pre-commit.ci/badge/github/Stephen-RA-King/bliss/main.svg
[pre-commit.ci-url]: https://results.pre-commit.ci/latest/github/Stephen-RA-King/bliss/main
[pypi-url]: https://pypi.org/project/bliss/
[pypi-image]: https://img.shields.io/pypi/v/bliss.svg
[python-version-image]: https://img.shields.io/pypi/pyversions/bliss
[readthedocs-image]: https://readthedocs.org/projects/bliss/badge/?version=latest
[readthedocs-url]: https://bliss.readthedocs.io/en/latest/?badge=latest
[requirements-status-image]: https://requires.io/github/Stephen-RA-King/bliss/requirements.svg?branch=main
[requirements-status-url]: https://requires.io/github/Stephen-RA-King/bliss/requirements/?branch=main
[status-image]: https://img.shields.io/pypi/status/bliss.svg
[tests-image]: https://github.com/Stephen-RA-King/bliss/actions/workflows/tests.yml/badge.svg
[tests-url]: https://github.com/Stephen-RA-King/bliss/actions/workflows/tests.yml
[wiki]: https://github.com/Stephen-RA-King/bliss/wiki
