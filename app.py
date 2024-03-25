import logging
from flask import Flask

from loggers import init_logging
from settings import Settings

logger = logging.getLogger(name=__name__)
app = Flask(__name__)


@app.route("/")
def hello_world():
    # stdlib logging logger
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL")
    # Flask default logger
    app.logger.debug("DEBUG Flask")
    app.logger.info("INFO Flask")
    app.logger.warning("WARNING Flask")
    app.logger.error("ERROR Flask")
    app.logger.critical("CRITICAL Flask")
    return "Hello World!"


if __name__ == "__main__":
    init_logging()
    app.run()
    app.config.update(Settings.model_dump())
