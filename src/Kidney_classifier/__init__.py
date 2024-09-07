import os
import logging
import sys


'''
This file tries to store and show all logs durign the whole package.
It gives us the ability to understand what is happening during a runing file.

'''

# Create configuration variables for logging
Format_of_information = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
Log_directory = 'logs'
os.makedirs(Log_directory, exist_ok=True)
Log_file_path = os.path.join(Log_directory,'logs_file.log')

# Put variable into basicConfiguration function
logging.basicConfig(

    level=logging.INFO,
    format=Format_of_information,
    handlers=[
        logging.FileHandler(Log_file_path) , # Get the log file
        logging.StreamHandler(sys.stdout)    # See log on terminal
    ]
)


# Call the function and name it Kidney_classifier_logger, since we take care of this folder
logger = logging.getLogger(name="Kidney_classifier_logger")