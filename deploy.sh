set -e

# 이동
cd blog/

# .env 파일 생성
echo DJANGO_SECRET_KEY=${{ secrets.DJANGO_SECRET_KEY }} >> .env
echo DJANGO_SETTINGS_MODULE=${{ secrets.DJANGO_SETTINGS_MODULE }} >> .env
echo DEBUG=${{ secrets.DEBUG }} >> .env
echo RIOT_API_DEVELOPMENT_KEY=${{ secrets.RIOT_API_DEVELOPMENT_KEY }} >> .env
echo RIOT_API_KEY=${{ secrets.RIOT_API_KEY }} >> .env
echo SUMMONER_URL=${{ secrets.SUMMONER_URL }} >> .env

# 모듈 설치
pip install -r requirements.txt

# DB 마이그레이션
python3 manage.py makemigrations
python3 manage.py migrate

# 정적 파일 수집
python3 manage.py collectstatic --noinput

# gunicorn 재실행
# sudo systemctl restart gunicorn.service
