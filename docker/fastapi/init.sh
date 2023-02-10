#!/bin/bash

docker rm tungtung_fastapi
cd ../../
docker build -f Dockerfile -t tungtung:first . && docker run -p 8000:8000 -v "$(pwd)":/workspace --name tungtung_fastapi --restart unless-stopped tungtung:first
