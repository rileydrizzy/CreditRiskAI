.DEFAULT_GOAL := help

help:
	@echo "    prepare              desc of the command prepare"
	@echo "    install              desc of the command install"


setup:
	@echo "Running setup..."
	. ./run_setup.sh

precommit:
	@echo "Running precommit on all files"
	pre-commit run --all-files

export:
	@echo "Exporting dependencies to requirements file"
	python -m pip freeze > requirements.txt

