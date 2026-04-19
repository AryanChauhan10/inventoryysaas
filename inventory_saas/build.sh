#!/usr/bin/env bash
pip install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:/opt/render/project/src
python manage.py collectstatic --noinput
python manage.py migrate