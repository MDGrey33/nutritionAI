import os
import json
from app.infra import logger


class File:
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def get_path(self):
        filepath = self.path + self.name
        return filepath

    def write(self, data, mode='w'):
        try:
            # Create folder if it doesn't exist
            if not os.path.exists(self.path):
                os.makedirs(self.path)
                logger.logger.debug(f"Created directory {self.path}")

            file_path = os.path.join(self.path, self.name)

            # Create file if it doesn't exist
            if not os.path.exists(file_path):
                with open(file_path, mode) as f:
                    json.dump({}, f)
                logger.logger.debug(f"Created file {file_path}")

            # Read data from file
            with open(file_path, "r") as f:
                file_data = json.load(f)

            # Update data with new object
            file_data.update(data)

            # Write data to file
            with open(file_path, mode) as f:
                json.dump(file_data, f, indent=4)

            logger.logger.debug(f"Wrote object to {file_path}")
            return True

        except OSError as e:
            logger.logger.error(f"Error accessing directory or file: {str(e)}")
            return False
