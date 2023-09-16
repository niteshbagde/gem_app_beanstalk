# to create amd write logs in logs directory with name that was defined
import logging 
import os
from datetime import datetime

# to name the log file with respect to date time
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# make dir if not
# os.makedirs("logs", exist_ok=True)

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE[0:10])
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

