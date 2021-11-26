# dslr
42School Machine Learning Project: Logistic Regression

installation:

install pyenv
    ```brew install pyenv pyenv-virtualenv```

install python 3.10.0
    ```pyenv install 3.10.0```

create virtualenv dslr
    ```pyenv virtualenv 3.10.0 dslr```

auto source environment
    ```pyenv local dslr```

install only prod dependencies
    ```pip install -e .```

install prod and dev dependencies
    ```pip install -e ".[dev]"```

usage: 

run tests
    ```pytest```

run coverage
    ```pytest --cov dslr```

run linter
    ```flake8```