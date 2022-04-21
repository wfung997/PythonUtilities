import datetime as dt
import logging

def initializeLogging(config):
    now = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    app_name = "myapp"
    log_filename = f"{app_name}_{now}.log"
    print(f'Writing logs to {log_filename}')
    level = logging.DEBUG
    log_format = "%(levelname)s % (asctime)s - %(message)s"
    datefmt = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(filename=log_filename, format=format,
                        datefmt=datefmt, level=level)
    logging.info(f"Start logging {app_name}")
