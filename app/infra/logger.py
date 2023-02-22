# app.infra.logger
import logging
from logging.handlers import RotatingFileHandler
import os


# Define the log file path
log_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log')

# Check if the log folder exists, and create it if it doesn't
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Define the logger DEBUG, INFO, WARNING, ERROR, and CRITICAL
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Define the handler to write logs to a file
handler = RotatingFileHandler(
    os.path.join(log_folder, 'logs.log'),
    maxBytes=10*1024*1024,
    backupCount=3
)

# DEBUG, INFO, WARNING, ERROR, and CRITICAL
handler.setLevel(logging.DEBUG)

# Define the formatter for the logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(pathname)s:%(funcName)s - %(message)s')


handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)
