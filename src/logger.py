import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Generate a log file name based on the current date and time
# The log file will be named in the format "MM_DD_YYYY_HH_MM

Logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE) # Create a path for the logs directory)
# Example: "logs/01_01_2023_12_00_00.log

os.makedirs(Logs_path, exist_ok=True)           # Create the logs directory if it does not exist
LOG_FILE_PATH = os.path.join(Logs_path, LOG_FILE)   # Create the full path for the log file

logging.basicConfig(            # Configure the logging settings
    filename=LOG_FILE_PATH, # Set the log file path
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s', # Define the log message format
    level=logging.INFO, # Set the logging level to INFO
)

