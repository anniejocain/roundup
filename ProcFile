web: gunicorn signalback.wsgi --log-file -
worker: celery -A items worker --loglevel=info -B
