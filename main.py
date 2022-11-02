import logging
from src.app import foo


def main():
    foo()
    logger_test = logging.getLogger()
    logger_test.info('Hello world!, it is a logger!')


if __name__ == '__main__':
    main()
