install:
	poetry install

update:
	poetry update

build: update install
	poetry build

test:
	poetry run pytest --cov=gendiff --cov-report xml tests/

lint:
	poetry run flake8 gendiff

check: test lint

run_nested_json:
	gendiff tests/fixtures/input_data/before_nested.json tests/fixtures/input_data/after_nested.json

run_nested_yml:
	gendiff tests/fixtures/input_data/before_nested.yml tests/fixtures/input_data/after_nested.yml

.PHONY: install test lint run_nested_json run_nested_yml
