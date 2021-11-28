============
DSLR: 42School Machine Learning Project: Logistic Regression
============

***************
Prerequisites
***************

- pyenv and poetry
    - ``brew install pyenv pyenv-virtualenv poetry``

- python 3.10.0
    - ``pyenv install 3.10.0``

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
