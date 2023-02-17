from flask import Flask
from app.infra import logger

app = Flask(__name__)
logger.logger.debug('flask app initiated')

from app import routes
logger.logger.debug('general routes imported')

from app.routes import plan
logger.logger.debug('plan routes imported')

if __name__ == "__main__":
    logger.logger.debug('starting flask app')
    app.run(debug=True)
