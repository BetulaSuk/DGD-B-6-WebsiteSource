#!/bin/bash

docker-compose down

sudo rm -rf ./services/backend/migrations/*
echo ">>> removed aerich migration data"

sudo rm -rf ./services/mysql/data/*
echo ">>> removed mysql data"

sudo rm -rf ./services/elasticsearch/data/*
echo ">>> removed elasticsearch data"

sudo rm -rf ./services/elasticsearch/logs/*
echo ">>> removed elasticsearch log files"
