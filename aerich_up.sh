#!/bin/bash
cd ~/tzy/fastapi-vue
docker-compose exec backend aerich migrate
docker-compose exec backend aerich upgrade

