"""Logger setup"""

import logging

LOG_FILE = "ddb-data-export.log"


def setup_logger():
    """Set up logger with required configurations."""

    # Restricting boto3 logs from being logged in the logfile.
    for name in ["boto", "urllib3", "s3transfer", "boto3", "botocore", "nose"]:
        logging.getLogger(name).setLevel("CRITICAL")

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(LOG_FILE, mode="a")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("%(asctime)s %(levelname)-3s: %(message)s")
    file_handler.setFormatter(file_formatter)

    # create a stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_formatter = logging.Formatter("%(asctime)s %(levelname)-3s: %(message)s")
    stream_handler.setFormatter(stream_formatter)

    # add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
