web: python manage.py migrate && playwright install chromium && playwright install-deps && gunicorn tamarindsaccoapi.wsgi:application --bind 0.0.0.0:$PORT
