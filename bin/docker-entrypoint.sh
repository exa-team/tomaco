#!/usr/bin/env bash

./bin/wait-for-it.sh -t 60 postgres:5432
flask db upgrade --directory tomaco/migrations
npm run run & flask run --host=0.0.0.0 --port=8080
