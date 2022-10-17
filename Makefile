clean: 
	rm -rf ./.venv

venv:
	python -m venv ./.venv

compile:
	python -m pip install pip-tools && pip-compile .requirements/requirements.in

compile_dev: compile
	pip-compile .requirements/dev-requirements.in

install: compile_dev
	pip-sync .requirements/requirements.txt .requirements/dev-requirements.txt

black:
	isort --profile black app && \
	black app

lint:
	mypy app --explicit-package-bases --namespace-packages --config-file=pyproject.toml
	pflake8 app
