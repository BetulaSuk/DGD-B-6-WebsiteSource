#!/bin/bash

docker-compose up -d --build

sleep 3s

docker ps

sleep 3s

docker-compose exec backend aerich init -t src.database.config.TORTOISE_ORM
docker-compose exec backend aerich init-db

python3 ./setup/main.py

docker-compose exec backend aerich migrate
docker-compose exec backend aerich migrate
