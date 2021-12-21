NAME := dslr
INSTALL_STAMP := .install.stamp
POETRY := $(shell command -v poetry 2> /dev/null)
.DEFAULT_GOAL := help

.PHONY: help

#	Utils

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  install     		install packages and prepare environment"
	@echo "  clean       		remove all temporary files"
	@echo "  fclean       		clean and remove poetry virtual environment"
	@echo "  lint        		run the code linters"
	@echo "  format      		reformat code"
	@echo "  test        		run all the tests"
	@echo "  pre-commit     	run pre-commit config"
	@echo "  describe       	describe the given dataset"
	@echo "  histogram      	plot house marks by class as histograms"
	@echo "  scatter_plot   	plot class marks distribution as scatter plots"
	@echo "  pair_plot      	plot the dataset as a pair plot"
	@echo "  train        		train from the given dataset"
	@echo "  predict        	make predictions"
	@echo ""
	@echo "To give arguments to a target threw make, please use 'make <target> -- <arguments>'"
	@echo "	eg: make describe -- -h"

.PHONY: install
install: $(INSTALL_STAMP)

$(INSTALL_STAMP): pyproject.toml poetry.lock
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) install
	touch $(INSTALL_STAMP)

.PHONY: clean
clean:
	find . -type d -name "__pycache__" | xargs rm -rf {};
	rm -rf $(INSTALL_STAMP) .coverage

.PHONY: fclean
fclean: clean
	$(POETRY) env remove $(shell $(POETRY) env list | grep -E '(.*?) \(Activated\)' | awk '{print $$1}')

.PHONY: lint
lint: install
	$(POETRY) run isort --profile=black --lines-after-imports=2 --check-only ./tests/ $(NAME)
	$(POETRY) run black --check ./tests/ $(NAME) --diff
	$(POETRY) run flake8 --ignore=W503,E501 ./tests/ $(NAME)

.PHONY: format
format: install
	$(POETRY) run isort --profile=black --lines-after-imports=2 ./tests/ $(NAME)
	$(POETRY) run black ./tests/ $(NAME)

.PHONY: test
test: install
	$(POETRY) run coverage run --source=$(NAME) -m pytest -vv && $(POETRY) run coverage report -m

#	Project

.PHONY: describe
describe: install
	$(POETRY) run python dslr/data_viz/describe.py $(filter-out $@,$(MAKECMDGOALS))

.PHONY: histogram
histogram: install
	$(POETRY) run python dslr/data_viz/histogram.py $(filter-out $@,$(MAKECMDGOALS))

.PHONY: scatter_plot
scatter_plot: install
	$(POETRY) run python dslr/data_viz/scatter_plot.py $(filter-out $@,$(MAKECMDGOALS))

.PHONY: pair_plot
pair_plot: install
	$(POETRY) run python dslr/data_viz/pair_plot.py $(filter-out $@,$(MAKECMDGOALS))

.PHONY: predict
predict: install
	$(POETRY) run python dslr/logistic_regression/logreg_predict.py $(filter-out $@,$(MAKECMDGOALS))

.PHONY: train
train: install
	$(POETRY) run python dslr/logistic_regression/logreg_train.py $(filter-out $@,$(MAKECMDGOALS))

%:
	@:
