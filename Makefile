lint:
	@echo "Linting..."
	@pipenv run lint
	@echo "Security checks..."
	@pipenv run security

run:
	pipenv run python -m bottle --debug --reload tomaco.app

setup:
	pip install pipenv
	pipenv install --dev --deploy

test:
	pipenv run test
