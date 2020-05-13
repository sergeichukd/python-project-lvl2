install:
	python -m poetry install

test:
	python -m poetry run pytest gendiff

lint:
	python -m poetry run flake8 gendiff

check: test lint

.PHONY: install test lint