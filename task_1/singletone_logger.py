import datetime
import logging
import os


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonType):
    _logger: logging = None

    def __init__(self) -> None:
        self._logger = logging.getLogger("lerna")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] > %(message)s"
        )

        now = datetime.datetime.now()
        dirname = os.path.abspath("log")

        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        fileHandler = logging.FileHandler(
            f"{dirname}/log_{now.strftime('%Y-%m-%d')}.log"
        )

        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

    @property
    def logger(self) -> logging.getLogger:
        return self._logger
