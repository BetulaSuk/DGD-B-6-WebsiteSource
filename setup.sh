#!/bin/bash

docker-compose exec backend aerich init -t src.database.config.TORTOISE_ORM
docker-compose exec backend aerich init-db

echo ">>> RUN backend/setup/main.py!!!"
docker-compose exec backend python3 setup/main.py
echo ">>> COMPLETE backend/setup/main.py!!!"

sleep 3s

docker-compose exec backend aerich migrate
docker-compose exec backend aerich migrate
