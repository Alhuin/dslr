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
- Data Visualization
    - describe: describe the dataset (pandas.describe() style)
        ``python dslr/describe.py [-h] csv_path``

    - histogram: plot house marks by class as histograms
        ``python dslr/histogram.py [-h] [--all] [-c COURSE]``

    - scatter plot: plot comparison of class marks distribution as scatter plots
        ``python/dslr scatter_plot.py [-h] [--all] [-c COURSES COURSES] [-afo ALL_FOR_ONE]``

    - pair plot: plot the dataset as a pair plot
        ``python dslr/pair_plot.py [-h]``

- Logistic Regression
    - train
    - predict

- Tests & Lint
    - run tests and lint with tox
        ``poetry run tox``

    - run tests and coverage locally
        ```poetry run coverage run --source=dslr -m pytest && poetry run coverage report -m``
