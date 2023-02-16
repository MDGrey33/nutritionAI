from app.infra import logger


def write_file(content: str, filename: str):
    with open(filename, 'w') as f:
        f.write(content)
        logger.logger.debug(f'{filename} written successfully')
    return f'{filename} written successfully'

