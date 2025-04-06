# myLogger.py
import logging

def get_logger(name='kubesec-logger', log_file='forensics.log'):
    logger = logging.getLogger(name)

    # Prevent duplicate handlers if this function is called multiple times
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger
