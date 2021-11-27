# dslr
42School Machine Learning Project: Logistic Regression

installation:

clone project
    ``git clone https://github.com/Alhuin/dslr && cd $_``

install pyenv and poetry
    ``brew install pyenv pyenv-virtualenv poetry``

install python 3.10.0
    ``pyenv install 3.10.0``

set python 3.10 as directory interpreter
    ``pyenv local 3.10.0``

create virtualenv with poetry and install dependencies
    ``poetry shell``
    ``poetry install``


usage:

run tests, lint and format
    ```poetry run tox```
