lint:
	@echo "Linting..."
	@pipenv run lint
	@echo "Security checks..."
	@pipenv run security

run:
	pipenv run python tomaco/app.py

setup:
	pip install pipenv
	pipenv install --dev --deploy

test:
	pipenv run test
