import os, sys

from src.exception import CustomException
from src.logger import logging

from src.utils import load_object

import pandas as pd


class PredictionPipeline:
    def __init__(self):
        pass

    def Predict(self,features):

        try:
            preprocessor_path = os.path.join(r"data/artifacts/pickel" , "preprocessor.pkl")

            model_path = os.path.join(r"data/artifacts/pickel" , "model.pkl")

            preprocessor = load_object(preprocessor_path)

            model = load_object(model_path)

            data_scale = preprocessor.transform(features)

            pred = model.predict(data_scale)

            return pred
        
        
        
        except Exception as e:
            logging.info("error occured while model prediction")
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(
            self, 
            carat : float,
            depth : float,
            table : float,
            x : float,
            y : float,
            z : float,
            cut : str,
            color : str,
            clarity : str
    ):
    
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity


    def get_data_as_dataframe(self):
        try:

            # create dictonary
            custom_data_input_dic = {

                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]

            }

            # read dictonary as datafram using pandas

            df = pd.DataFrame(custom_data_input_dic)
            logging.info("data gathered . inputs converted to dataframe")

            return df

        except Exception as e:
            logging.info("exception occured in prediction pipeline")
            raise CustomException(e,sys)
















