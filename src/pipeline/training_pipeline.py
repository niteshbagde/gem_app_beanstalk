from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer




# test code
if __name__ == "__main__":
    obj = DataIngestion()
    train_data , test_data = obj.initiate_data_ingestion()
    # print(train_data,test_data)
    datatransformation = DataTransformation()
    trainarray , testarray , _ = datatransformation.initiate_data_transformation(train_data , test_data)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(trainarray , testarray)
