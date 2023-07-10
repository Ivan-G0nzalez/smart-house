import json
from src.util.logger import logger


def read_json_file(path:str)-> dict:
    logger.info(f"reading the file {path}")
    with open(path) as file:
        file_content = json.load(file)

    logger.info("Data was readed")
    return file_content

