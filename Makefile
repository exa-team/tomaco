lint:
	@echo "Linting..."
	@pipenv run lint
	@echo "Security checks..."
	@pipenv run security

run:
	pipenv run python -m bottle --debug --reload tomaco.app

setup:
	@echo "Installing Python dependencies..."
	pip install pipenv
	pipenv install --dev --deploy
	@echo "Configuring pre-commit..."
	pre-commit

test:
	pipenv run test
