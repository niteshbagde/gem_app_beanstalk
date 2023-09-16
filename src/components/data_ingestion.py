# reading the dataset - data ingestion

import os
import sys

from src.exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.logger import logging







@dataclass
class DataIngestionconfig:
    train_data_path:str = os.path.join(r"data/artifacts" , "train.csv")
    test_data_path:str = os.path.join(r"data/artifacts" , "test.csv")
    raw_data_path:str = os.path.join(r"data/artifacts" , "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion method starts")
        try:
            df = pd.read_csv(r"data/gemstone.csv")
            logging.info("Data read as pandas DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path , index=False)

            logging.info("Train test Split")
            train_set , test_set = train_test_split(df , test_size=0.30, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path , index=False)
            test_set.to_csv(self.ingestion_config.test_data_path , index = False)

            logging.info("train test split done and the csv are exported. Data ingestion completed")

            return (
                self.ingestion_config.train_data_path ,
                self.ingestion_config.test_data_path 
            )

        except Exception as e:
            logging.info("Exception occured at data ingestion stage")
            raise CustomException(e,sys)









