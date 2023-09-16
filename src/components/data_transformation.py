import sys 
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object


@dataclass
class DataTransformationoConfig:
    preprocessors_obj_file_path = os.path.join(r"data/artifacts/pickel" , "preprocessor.pkl")

class DataTransformation:

    def __init__(self):
        self.data_transformtion_config = DataTransformationoConfig() 

    def get_data_transformation_object(self):
        try:

            logging.info("Data transformation initiated")

            # catogorical and numerical split

            # appling encoding like ordinal

            catagorical_features = ['cut', 'color','clarity']
            numerical_features = ['carat', 'depth','table', 'x', 'y', 'z']

            cut_cat = ['Fair','Good','Very Good', 'Premium', 'Ideal']
            color_cat = ['D','E', 'F','G','H','I' ,'J' ]
            clarity_cat = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info("pipeline initiated")

            # Numerical pipleine
            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer" , SimpleImputer(strategy="median")),
                    ("scaling",StandardScaler())
                ]
            )


            # Catagorical Pipeline

            catagorical_pipeline = Pipeline(
                steps=[
                    ("imputer" , SimpleImputer(strategy="most_frequent")),
                    ("OrdinalEncoder",OrdinalEncoder(categories= [cut_cat,color_cat,clarity_cat])),
                    ("scaling", StandardScaler())
                ]
            )

            # combine the pipeline

            preprocessor = ColumnTransformer(
                [
                ("num_pipe", numerical_pipeline, numerical_features),
                ("cat_pipe", catagorical_pipeline, catagorical_features)
                ]) 
            logging.info("pipeline completed")
            return preprocessor
        
            

            

        except Exception as e:
            logging.info("Error in data transformation")
            CustomException(e,sys)



    def initiate_data_transformation(self, train_path , test_path):
        try:
            # reading train and test data:

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("read test and train data completed for data transformation")
            logging.info(f"Train data frame head : \n{train_df.head().to_string()}")
            logging.info(f"Test data frame head : \n{test_df.head().to_string()}")

            logging.info("Obtaining preprocessing object")

            target_column_name = "price"
            drop_columns = [target_column_name , 'id']
            # x train and y train
            input_feature_train_df = train_df.drop(columns = drop_columns , axis=1)
            target_feature_train_df = train_df[target_column_name]
            # x test and y test
            input_feature_test_df = test_df.drop(columns= drop_columns , axis=1)
            targest_feature_test_df = test_df[target_column_name]
            logging.info("applying preprocessing obj on train and test datasets")

            preprocessing_obj = self.get_data_transformation_object()

            # transforming using preprocessor object

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            logging.info("Applying preprocesing object on training and testing datasets") 


            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(targest_feature_test_df)]

            save_object(
                file_path=self.data_transformtion_config.preprocessors_obj_file_path,
                obj=preprocessing_obj
            )
            logging.info("preprocessor object saved")


            return (
                train_arr,
                test_arr,
                self.data_transformtion_config.preprocessors_obj_file_path,
            )

        except Exception as e:
            logging.info("Error occured in initiate_data_transformation")
            raise CustomException(e,sys)
            








