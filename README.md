# Todo list
1. Implement error handling
2. Implement inout validation
3. Multithreading in celery
4. Pull file management to one file
5. Make mobile app to
   1. Show meals 
   2. Submit to health app
6. Implement google authentication for
7. Move relevant variables to .env
8. Move relevant configuration to etc
9. Add logging to app_celery
# Deployment
Start redis in docker container

    docker run --name some-redis -p 6379:6379 -d redis
Start Flask

    flask --debug run --port=5001
Start Celery

    celery -A app_celery.celery worker --loglevel=info
