#!/bin/bash

docker rm -f tungtung_mysql
docker build -f Dockerfile -t tungtung:mysql . && docker run -d -p 3306:3306 --env MYSQL_ROOT_PASSWORD=tldjsWkd!123 --name tungtung_mysql --restart unless-stopped tungtung:mysql

python scripts/init.py