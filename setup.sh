#!/bin/bash

docker-compose exec backend aerich init -t src.database.config.TORTOISE_ORM
docker-compose exec backend aerich init-db

echo ">>> RUN setup/main.py!!!"
python3 ./setup/main.py
echo ">>> COMPLETE setup/main.py!!!"

sleep 3s

docker-compose exec backend aerich migrate
docker-compose exec backend aerich migrate
