#!/bin/bash

docker-compose exec backend aerich migrate
docker-compose exec backend aerich upgrade

