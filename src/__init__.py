# external module imports
import os
import logging
import json

# external package imports
from pathlib import Path
from logging.config import dictConfig

DATA_FOLDER = os.getenv("DATA_FOLDER")
BALL_MACHINE_USAGE_FILE = os.getenv("BALL_MACHINE_USAGE_FILE")
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

APP_DIR = Path().absolute().parent
CONFIG_DIR = Path.joinpath(APP_DIR, "config")
LOG_DIR = Path.joinpath(APP_DIR, "logs")
LOG_FILENAME = Path.joinpath(LOG_DIR, "fitness_tracker.log")
LOG_CONF_FILENAME = Path.joinpath(CONFIG_DIR, "logging_config.json")

logger = logging.getLogger(__name__)


def setup_logging(logging_config=LOG_CONF_FILENAME, log_filename=LOG_FILENAME):
    try:
        with open(logging_config, "r") as conf_file:
            config = json.load(conf_file)["logging"]
            config["handlers"]["file"]["filename"] = log_filename
            dictConfig(config)
    except FileNotFoundError:
        logger.exception("File/path does not exist")


setup_logging()
