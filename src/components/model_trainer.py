from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object




rfr=RandomForestRegressor(random_state=42)



class model_trainer_config:
    def __init__(self):
        self.model_save_config= os.path.join('Artifacts','RandomForestRegressor.pkl')



class initiate_model_trainer:
    def __init__(self):
        self.model_info = model_trainer_config()


    def model_training(self,train_arr,test_arr):
        logging.info('model data train test spliting insitiated')
        trainx,testx,trainy,testy = train_arr[:,:-3],test_arr[:,:-3],train_arr[:,-3:],test_arr[:,-3:]

        logging.info('model training insitiated')
        rfr.fit(trainx,trainy)

        pred=rfr.predict(testx)

        score=r2_score(testy,pred)

        save_object(self.model_info.model_save_config,rfr)
        logging.info('saved trained model')

        logging.info(f"r2 score of model is {score}")


        return print(score)
















