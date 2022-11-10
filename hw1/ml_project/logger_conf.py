import logging

logger: logging.Logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handlers: list[logging.Handler] = []

stream_handler: logging.StreamHandler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_FORMAT = (
    "- %(asctime)s "
    "- %(name)s "
    "- [%(levelname)s] "
    "- (%(module)s).%(funcName)s(%(lineno)d) "
    "- %(message)s")
stream_formatter: logging.Formatter = logging.Formatter(stream_FORMAT)
stream_handler.setFormatter(stream_formatter)

logger.addHandler(stream_handler)
