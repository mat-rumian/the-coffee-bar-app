import logging as log
import sys

_LOG_LEVEL = {
    'critical': log.CRITICAL,
    'error': log.ERROR,
    'warning': log.WARNING,
    'info': log.INFO,
    'debug': log.DEBUG
}


def configure_logging(log_level: str):

    log_level = _LOG_LEVEL[log_level]

    root = log.getLogger()
    root.setLevel(log_level)

    formatter = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stdout_handler = log.StreamHandler(sys.stdout)
    stdout_handler.setLevel(log_level)
    stdout_handler.setFormatter(formatter)
    root.addHandler(stdout_handler)

    return log
