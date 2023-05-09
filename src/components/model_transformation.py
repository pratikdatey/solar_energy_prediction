from src.logger import logging
from src.exception import CustomException
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from src.utils import save_object
import os
import sys
from dataclasses import dataclass



@dataclass
class preprocessor:
    def __init__(self):
        self.preprocessing_config=os.path.join('Artifacts','preprocessor.pkl')



class data_transformation:
    def __init__(self):
        self.preprocessing_info=preprocessor()

    
    def get_transformer(self):
        try:
            logging.info('scaling started...')
            standard_scaling=Pipeline(steps=[
                ("standard scaling",StandardScaler(with_mean=False))])
            
            return standard_scaling
        
        except Exception as e:
            raise CustomException(e,sys)
        


    def initiate_preprocessing(self,train_path,test_path):
        try:
            train=pd.read_csv(train_path)
            test=pd.read_csv(test_path)

            logging.info('Initializing preprocessing')
            target_col=['Clearsky DHI','Clearsky DNI','Clearsky GHI']

            input_train=train.drop(target_col,axis=1)
            output_train=train[target_col]

            input_test=test.drop(target_col,axis=1)
            output_test=test[target_col]


            scale=self.get_transformer()
            

            train_data=scale.fit_transform(input_train)
            test_data=scale.fit_transform(input_test)
            logging.info("successfully standard scaling completed")



            train_arr=np.c_[train_data,np.array(output_train)]
            test_arr=np.c_[test_data,np.array(output_test)]
            logging.info('concating train and test completed')



            save_object(self.preprocessing_info.preprocessing_config,scale)
            logging.info('saving preprocessing pickle file')



            return (train_arr, test_arr)



        except Exception as e:
            raise CustomException(e,sys)



        





