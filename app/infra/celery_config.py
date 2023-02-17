from celery import Celery
from flask import Flask
from dotenv import load_dotenv
import os
from app.infra import logger

app = Flask(__name__)
logger.logger.debug('celery config initiated flask app')

load_dotenv()
REDIS_CONNECTION_STRING = os.getenv("REDIS_CONNECTION_STRING")

app.config.update(
    CELERY_BROKER_URL=REDIS_CONNECTION_STRING,
    result_backend=REDIS_CONNECTION_STRING
)


celery = Celery(__name__, broker=app.config['CELERY_BROKER_URL'])
logger.logger.debug('updating celery configuration')
celery.conf.update(app.config)
