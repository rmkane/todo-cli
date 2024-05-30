import logging
import logging.config
import os

from datetime import datetime

DEFAULT_FILE_PREFIX = "app"
DEFAULT_LOG_DIR = "log"
DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def setup_logging(
    default_level=logging.INFO,
    log_dir=DEFAULT_LOG_DIR,
    log_file_prefix=DEFAULT_FILE_PREFIX,
    log_format=DEFAULT_LOG_FORMAT,
):
    # Ensure the logs directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Set the log file name with the current date
    today = datetime.now().strftime("%Y%m%d")
    log_file = os.path.join(log_dir, f"{log_file_prefix}-{today}.log")

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": log_format,
                "datefmt": "%Y-%m-%d %H:%M:%S"
            }
        },
        "handlers": {
            "file_handler": {
                "level": default_level,
                "formatter": "standard",
                "class": "logging.FileHandler",
                "filename": log_file,
            },
            "console_handler": {
                "level": logging.WARNING,
                "formatter": "standard",
                "class": "logging.StreamHandler",
            }
        },
        "root": {
            "handlers": ["file_handler", "console_handler"],
            "level": default_level,
        }
    }

    logging.config.dictConfig(logging_config)
