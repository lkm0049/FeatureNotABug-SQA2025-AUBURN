import logging
import os

def giveMeLoggingObject(name='kubesec-logger', log_file='forensics.log'):
    """
    Returns a configured logger instance.
    Logs will be written to `forensics.log` in the current directory.
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid adding multiple handlers if logger is reused
    if not logger.handlers:
        # Create file handler
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(fh)

    return logger

