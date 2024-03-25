from pathlib import Path
import logging
import logging.config
from logging.handlers import RotatingFileHandler

from settings import Settings

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": Settings.LOG_FORMAT,
            "style": Settings.LOG_STYLE,
            "datefmt": Settings.LOG_DATE_TIME_FORMAT,
            "validate": True,
        }
    },
    "filters": {
        "warning_filter": {
            "()": "loggers.SelectedLevelFilter",
            "level": logging.WARNING,
        },
        "error_filter": {"()": "loggers.SelectedLevelFilter", "level": logging.ERROR},
    },
    "handlers": {
        "default": {
            "class": logging.StreamHandler,
            "level": Settings.LOG_LEVEL,
            "formatter": "default",
        },
        "warning_file_handler": {
            "class": RotatingFileHandler,
            "formatter": "default",
            "filters": ["warning_filter"],
            "filename": Settings.LOG_PATH / "warning.log",
            "maxBytes": 1024,
            "backupCount": 3,
            "encoding": "utf-8",
        },
        "error_file_handler": {
            "class": RotatingFileHandler,
            "formatter": "default",
            "filters": ["error_filter"],
            "filename": Settings.LOG_PATH / "error.log",
            "maxBytes": 1024,
            "backupCount": 3,
            "encoding": "utf-8",
        },
    },
    "root": {
        "level": Settings.LOG_LEVEL,
        "handlers": ["default", "warning_file_handler", "error_file_handler"],
    },
    "loggers": {
        # TODO: Add extra loggers here 😊
    },
}


def init_logging():
    Path(Settings.LOG_PATH).mkdir(parents=True, exist_ok=True)
    logging.config.dictConfig(LOGGING_CONFIG)


class SelectedLevelFilter(logging.Filter):
    def __init__(self, level: int, name: str = "") -> None:
        self._selected_level_name = level
        super().__init__(name=name)

    def filter(self, record: logging.LogRecord) -> bool:
        if record.levelno == self._selected_level_name:
            return True
        return False
