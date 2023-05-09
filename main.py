
from src.components.mongoDb_acsses import mongo_database
from src.components.model_transformation import data_transformation
from src.components.model_trainer import initiate_model_trainer



if __name__=='__main__':

    obj=mongo_database()
    train_path,test_path=obj.initiate_mongodb_connection()


    model_transformations=data_transformation()
    train_arr, test_arr = model_transformations.initiate_preprocessing(train_path,test_path)




    model_training=initiate_model_trainer()
    model_training.model_training(train_arr,test_arr)
