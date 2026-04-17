#!/usr/bin/env bash
pip install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:$(pwd)
python manage.py collectstatic --noinput
python manage.py migrate