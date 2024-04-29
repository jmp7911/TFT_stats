#!/bin/bash

sudo apt update
sudo apt-get upgrade

# Front 의존성 설치
yarn install
gulp

# 모듈 설치
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

# DB 마이그레이션
python3 manage.py makemigrations
python3 manage.py migrate

# 커버리지 설정파일 생성
echo "[run]" > .coveragerc
echo "omit = venv/*, manage.py, config/*, */migrations/*, */tests/*, */__init__.py" >> .coveragerc

# 코드 커버리지
python3 -m coverage run manage.py test
python3 -m coverage report

# 정적 파일 수집
python3 manage.py collectstatic --noinput

# gunicorn 재실행
sudo systemctl restart gunicorn.service
