import logging
from rich.logging import RichHandler


def get_logger(logger_name="default"):
    logging.basicConfig(
        level="NOTSET",
        format="%(asctime)s [%(name)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[RichHandler(rich_tracebacks=True)]
    )
    return logging.getLogger(logger_name)
