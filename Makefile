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

run_nested_json_plain:
	gendiff tests/fixtures/input_data/before_nested.json tests/fixtures/input_data/after_nested.json --format plain

run_nested_yml_plain:
	gendiff tests/fixtures/input_data/before_nested.yml tests/fixtures/input_data/after_nested.yml --format plain

check_interface: run_nested_json run_nested_yml run_nested_json_plain run_nested_yml_plain
	gendiff tests/fixtures/input_data/before_flat.json tests/fixtures/input_data/after_flat.json
	gendiff tests/fixtures/input_data/before_flat.yml tests/fixtures/input_data/after_flat.yml
	gendiff tests/fixtures/input_data/before_flat.json tests/fixtures/input_data/after_flat.json --format plain
	gendiff tests/fixtures/input_data/before_flat.yml tests/fixtures/input_data/after_flat.yml --format plain

install_app:
	pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ --no-cache-dir sergeichukd-gendiff

.PHONY: install test lint run_nested_json run_nested_yml run_nested_json_plain run_nested_yml_plain check_interface
