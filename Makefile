DATABASE_NAME:="tomaco_dev"

help:
	@echo "Yesterday is history, tomorrow is a mystery, and today is a gift... that’s why they call it the present\n"
	@echo "deploy .................................... Force the deploy to Heroku (must have a 'heroku' origin)"
	@echo "help ...................................... This screen"
	@echo "lint ...................................... Evaluate code's quality"
	@echo "run ....................................... Run frontend and backend (make -j2 run)"
	@echo "run-docker ................................ Run frontend and backend inside container"
	@echo "run-javascript ............................ Run just frontend side"
	@echo "run-python ................................ Run just backend side"
	@echo "setup ..................................... Setup the whole project for development purpose"
	@echo "setup-database ............................ Configure the database for development purpose"
	@echo "setup-dependencies ........................ Install frontend and backend dependencies"
	@echo "makemigrate ............................... Create database migrations
	@echo "migrate ................................... Run the database migration"
	@echo "test ...................................... Run frontend and backend tests"
	@echo "test-docker ............................... Run frontend and backend tests inside container"
	@echo "test-javascript ........................... Run the frontend tests"
	@echo "test-python ............................... Run the backend tests"
	@echo

deploy:
	git push heroku master

lint:
	@echo "Javascript lint..."
	npm run lint
	@echo "Python lint..."
	pipenv run lint
	@echo "Security checks..."
	pipenv run security

run: run-javascript run-python

run-docker: docker-compose up

run-javascript:
	npm run run

run-python:
	FLASK_APP=tomaco.wsgi:application pipenv run run

setup: setup-database setup-dependencies migrate

setup-database:
	@echo "\nConfiguring database..."
	@dropdb --if-exists $(DATABASE_NAME)
	@createdb $(DATABASE_NAME)
	@echo "\nIf you don't have a 'root' user yet, please execute: "
	@echo "psql -c \"CREATE USER root\" $(DATABASE_NAME)"

setup-dependencies:
	@echo "\nInstalling Python dependencies..."
	@pip install pipenv
	@pipenv install --dev --deploy
	@echo "\nInstalling Javascript dependencies..."
	@npm install --save-dev
	@echo "\nConfiguring pre-commit..."
	@pre-commit

makemigrate:
	@echo "Creating migrations..."
	cd tomaco; flask db migrate

migrate:
	@echo "Running migrations..."
	cd tomaco; flask db upgrade

test: test-javascript test-python

test-docker:
	docker-compose run --rm app sh -c "npm run test & pytest ."

test-javascript:
	npm run test

test-python:
	pipenv run test
