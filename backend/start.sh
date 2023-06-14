pkill redis
pkill start.sh
redis-server --daemonize yes --bind 127.0.0.1
celery -A tasks worker -B --loglevel=INFO

