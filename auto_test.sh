#!/usr/bin/env bash


set -a
. ./.env
set +a


export MONGO_DB_NAME=test_galaxy_swapi_db

echo "----------------------------------------------------------------"
echo "-      Exporting new database name for mongoDB testing...      -"
echo "-      MONGO_DB_NAME: $MONGO_DB_NAME                           -"
echo "----------------------------------------------------------------"

exec nosetests -vv --with-coverage --cover-package=. --cover-erase --detailed-errors 