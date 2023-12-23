#!/bin/bash

mkdir ./services/backend/migrations
mkdir ./services/elasticsearch/data
mkdir ./services/elasticsearch/logs
mkdir ./services/mysql/data
mkdir ./services/backend/data/static
mkdir ./services/backend/data/static/100_PDF
mkdir ./services/backend/data/static/Arxiv_PDF

docker-compose up -d --build

docker ps
