#!/bin/bash
set -e

echo "Starting SSH ..."
service ssh start

python /code/application.py