#!/bin/bash
docker build -f Dockerfile -t tungtung:mysql . && docker run -p 3306:3306 --env MYSQL_ROOT_PASSWORD=tldjsWkd!123 --name tungtung_mysql tungtung:mysql