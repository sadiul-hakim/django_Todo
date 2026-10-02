pip install uvicorn
uvicorn config.asgi:application --port 8000 --reload



gunicorn --workers 3 --bind 0.0.0.0:80 config.wsgi:application
