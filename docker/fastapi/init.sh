#!/bin/bash

docker build -f Dockerfile -t tungtung:first . && docker run -p 8000:8000 -v /Users/leejiwon/PycharmProjects/tungtung_fastapi:/workspace --name tungtung --restart unless-stopped tungtung:first
