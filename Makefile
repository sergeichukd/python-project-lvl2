install:
	python3 -m poetry install

lint:
	python3 -m poetry run flake gendiff

check:
	python3 -m pytest

.PHONY: install lint test
