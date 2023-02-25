#!/bin/bash

docker rm tungtung_fastapi

docker build -f Dockerfile -t tungtung:first .
cd ../../
docker run -d -p 8000:8000 -v "$(pwd)":/workspace --name tungtung_fastapi --restart unless-stopped tungtung:first
