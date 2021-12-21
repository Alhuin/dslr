============
DSLR: 42School AI Project: Data Science x Logistic Regression
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

- setup poetry virtualenv and launch poetry shell
    - ``make install``


******
Usage
******
- Data Visualization
    - describe: describe the dataset (pandas.describe() style)
        ``make describe -- [-h] csv_path``

    - histogram: plot house marks by class as histograms
        ``make histogram -- [-h] [--all] [-c COURSE]``

    - scatter plot: plot comparison of class marks distribution as scatter plots
        ``make scatter_plot -- [-h] [--all] [-c COURSES COURSES] [-afo ALL_FOR_ONE]``

    - pair plot: plot the dataset as a pair plot
        ``make pair_plot -- [-h]``

- Logistic Regression
    - train: train from the given dataset
        ``make train -- [-h] csv_path``

    - predict: make a prediction
        ``make predict -- [-h] csv_path``

- Tests & Lint
    - check lint with isort, black, flake8, mypy and bandit
        ``make lint``

    - run tests and coverage
        ``make test``

- Dev tools
    - format with isort and black
        ``make format``

    - clean project
        ``make clean``

    - run pre-commit configuration
        ``make pre-commit``
