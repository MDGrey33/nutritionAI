# Todo list

1. Implement error handling
2. Implement input validation
3. Learn about celery and fine tune
4. Pull file management to one package
5. Make mobile app to
   1. Show meals 
   2. Submit to health app
6. Implement google authentication for

# Deployment

Start redis in docker container

    docker run --name some-redis -p 6379:6379 -d redis
Start Flask

    flask --debug run --port=5001
Start Celery

    celery -A app.infra.app_celery.celery worker --loglevel=info   
