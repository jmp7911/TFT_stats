#!/bin/bash

# 모듈 설치
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

# DB 마이그레이션
python3 manage.py makemigrations
python3 manage.py migrate

# 정적 파일 수집
python3 manage.py collectstatic --noinput

# gunicorn 재실행
# sudo systemctl restart gunicorn.service
