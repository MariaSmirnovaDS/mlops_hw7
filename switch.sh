#!/bin/bash
# Переключение с Blue на Green

if [ "$1" == "green" ]; then
    sed -i 's/ml-service-blue:5000/ml-service-green:5000/g' nginx.conf
    docker-compose -f docker-compose.nginx.yml restart nginx
    echo "Switched to GREEN version"
elif [ "$1" == "blue" ]; then
    sed -i 's/ml-service-green:5000/ml-service-blue:5000/g' nginx.conf
    docker-compose -f docker-compose.nginx.yml restart nginx
    echo "Switched to BLUE version"
else
    echo "Usage: ./switch.sh [blue|green]"
fi
