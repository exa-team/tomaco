deploy:
	git push heroku master

lint:
	@echo "Javascript lint..."
	@npm run lint
	@echo "Python lint..."
	@pipenv run lint
	@echo "Security checks..."
	@pipenv run security

run: run-javascript run-python

run-javascript:
	npm run run

run-python:
	pipenv run run

setup:
	@echo "Installing Python dependencies..."
	pip install pipenv
	pipenv install --dev --deploy
	@echo "Installing Javascript dependencies..."
	npm install --save-dev
	@echo "Configuring pre-commit..."
	pre-commit

test: test-javascript test-python

test-javascript:
	npm run test

test-python:
	pipenv run test
