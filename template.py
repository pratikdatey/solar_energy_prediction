import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format="[%(asctime)s: %(levelname)s: %(message)ss]:%(message)s")

while True:
    project_name =input('Enter the project name -  ')
    if project_name != '':
        break
logging.info('creating Project by name : {project_name}')


#list of files:
list_of_files = [
    f"src/__init__.py",
    f"src/utils.py",
    f"src/pipline/__init__.py",
    f"src/pipline/mongoDb_config.py",
    f"src/pipline/model_injection.py",
    f"src/pipline/model_transformer.py",
    f"src/pipline/model_trainer.py",
    f"src/pipline/training_pipline.py",
    f"src/pipline/prediction_pipline.py",
    "requirements.txt",]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(Path(filepath))
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating a directory at :{filedir} for file :{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating a new file at :{filename} at path :{filepath}")
    else:
        logging.info(f"file is already present at :{filepath}")