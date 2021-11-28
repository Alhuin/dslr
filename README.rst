============
DSLR: 42School Machine Learning Project: Logistic Regression
============

***************
Prerequisites
***************

- pyenv and python 3.10
    - ``brew install pyenv pyenv-virtualenv``
    - ``pyenv install 3.10.0``

- poetry
    - ``curl -sSL https://install.python-poetry.org/ | ~/.pyenv/versions/3.10.0/bin/python -``
    - ``export PATH="$HOME/.local/bin:$PATH"``

***************
Installation
***************

- clone project
    - ``git clone https://github.com/Alhuin/dslr && cd $_``

- set python 3.10 as directory interpreter
    - ``pyenv local 3.10.0``

- setup poetry virtualenv
    - ``poetry shell``
    - ``poetry install``


******
Usage
******

- run tests and lint
    ```poetry run tox```
