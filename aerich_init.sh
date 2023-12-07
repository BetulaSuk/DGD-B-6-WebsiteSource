#!/bin/bash
cd ~/tzy/fastapi-vue
docker-compose exec backend aerich init -t src.database.config.TORTOISE_ORM
docker-compose exec backend aerich init-db

