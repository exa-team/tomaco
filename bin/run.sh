#!/usr/bin/env bash

npm run run & FLASK_APP=tomaco.wsgi:application FLASK_ENV=development pipenv run run
