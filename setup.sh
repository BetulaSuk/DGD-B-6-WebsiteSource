#!/bin/bash

mkdir ./services/backend/migrations
mkdir ./services/elasticsearch/data
mkdir ./services/elasticsearch/logs
mkdir ./services/mysql/data

docker-compose up -d --build

sleep 3s

docker ps

sleep 3s

docker-compose exec backend aerich init -t src.database.config.TORTOISE_ORM
docker-compose exec backend aerich init-db

python3 ./setup/main.py

docker-compose exec backend aerich migrate
docker-compose exec backend aerich migrate
