import logging
import sys


def initialize_logger(name, level=logging.DEBUG, log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
    """
    Initializes and returns a logger with the given name and level.

    Parameters:
    - name: The name of the logger.
    - level: The logging level (e.g., logging.DEBUG, logging.INFO).
    - log_format: The format of the log messages.

    Returns:
    A configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)  # Set the logger level

    # Create a console handler and set its level
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter(log_format)
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    # Avoid logging messages to be propagated to the root logger
    logger.propagate = False

    return logger
