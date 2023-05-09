from src.exception import CustomException
from src.logger import logging
from pymongo import MongoClient
import pandas as pd 
import os
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import sys
from src.components.model_transformation import data_transformation

from config.config import port,client_name,Mongo_DB_url,datbase_name








@dataclass
class Mongo_Client_info:
    raw_data_path:str=os.path.join('Artifacts','raw_data.csv')
    train_data_path:str=os.path.join('Artifacts','train_data.csv')
    test_data_path:str=os.path.join('Artifacts','test_data.csv')


class mongo_database:
    def __init__(self):
        self.mongodb_config=Mongo_Client_info()

    def initiate_mongodb_connection(self):
        try:
            logging.info("Starting fetching the data from MongoDB Databases")

            url = MongoClient(Mongo_DB_url,port)
            db = url[datbase_name]
            collection = db[client_name]
            cursor = collection.find()
            list_cur = list(cursor)
            data = pd.DataFrame(list_cur)
            data=data.drop(['_id','Timestamp'],axis=1)

            logging.info("Fetched raw data from server")
            os.makedirs(os.path.dirname(self.mongodb_config.train_data_path),exist_ok=True)
            data.to_csv(self.mongodb_config.raw_data_path,index=False,header=True)

            logging.info("splitting the data into training and testing")
            train,test=train_test_split(data,test_size=0.2,random_state=42)
            train.to_csv(self.mongodb_config.train_data_path,index=False,header=True)
            test.to_csv(self.mongodb_config.test_data_path,index=False,header=True)

            logging.info("successfully completed splitting the data into training and testing")
            return (self.mongodb_config.train_data_path,
                    self.mongodb_config.test_data_path)
        
        except Exception as e:
            raise CustomException(e,sys)















