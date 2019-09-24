DATABASE_NAME:="tomaco_dev"

help:
	@echo "Yesterday is history, tomorrow is a mystery, and today is a gift... that’s why they call it the present\n"
	@echo "deploy .................................... Force the deploy to Heroku (must have a 'heroku' origin)"
	@echo "docker-migrate ............................ Run the database migration inside container"
	@echo "docker-run ................................ Run frontend and backend inside container"
	@echo "docker-setup .............................. Create and configure the application and database usinc containers"
	@echo "docker-test ............................... Run frontend and backend tests inside container"
	@echo "help ...................................... This screen"
	@echo "lint ...................................... Evaluate code's quality"
	@echo "run ....................................... Run frontend and backend (make -j2 run)"
	@echo "run-javascript ............................ Run just frontend side"
	@echo "run-python ................................ Run just backend side"
	@echo "setup ..................................... Setup the whole project for development purpose"
	@echo "setup-database ............................ Configure the database for development purpose"
	@echo "setup-dependencies ........................ Install frontend and backend dependencies"
	@echo "makemigrate ............................... Create database migrations"
	@echo "migrate-down .............................. Run the database migration (downgrade)"
	@echo "migrate-up................................. Run the database migration (upgrade)"
	@echo "test ...................................... Run frontend and backend tests"
	@echo "test-javascript ........................... Run the frontend tests"
	@echo "test-python ............................... Run the backend tests"
	@echo

deploy:
	git push heroku master

docker-migrate:
	docker-compose run --rm tomaco ./bin/wait-for-it.sh -t 30 postgres:5432 -- \
		flask db upgrade --directory tomaco/migrations

docker-run:
	docker-compose up

docker-setup: docker-run docker-migrate

docker-test:
	docker-compose run --rm app sh -c "npm run test & pytest ."

lint:
	@echo "Javascript lint..."
	npm run lint
	@echo "Python lint..."
	pipenv run lint
	@echo "Security checks..."
	pipenv run security

run:
	./bin/run.sh

run-javascript:
	npm run run

run-python:
	FLASK_APP=tomaco.wsgi:application FLASK_ENV=development pipenv run run

setup: setup-database setup-dependencies migrate
	@echo "Create static folder..."
	@mkdir -p tomaco/static

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
	cd tomaco; pipenv run makemigrate

migrate-down:
	@echo "Downgrading migrations..."
	cd tomaco; pipenv run migrate_down

migrate-up:
	@echo "Running migrations..."
	cd tomaco; pipenv run migrate_up

test: test-javascript test-python

test-javascript:
	npm run test

test-python:
	pipenv run test

