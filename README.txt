Group Member: Yunhang Chi, Wenxi Huang, Shiyu Mao, Zhongke Sun
Date: April 9 2025

** This is README.txt file for our MLOps project **

The project includes the following files

/dsba-platform
├── main.py
├── preprocessing.py
├── model_training.py
├── model_evaluation.py
├── model_prediction.py
├── model_registry.py
├── __init__.py
├── requirements.txt
├── Dockerfile
└── CLI.py


Let me explain how the project work:

Firstly, the project aim to build a docker and realize the most classical model in the machine learning -- using RandomForestClassifier to classify the iris dataset.

You will find all model code in the '.py' scripts:
--preprocessing.py: used for dataset loading, splitting, and exploratory data analysis through visualizations.
--model_training.py: defines and trains a RandomForestClassifier, then saves the trained model to model.pkl and invokes evaluation.
--model_evaluation.py: computes standard performance metrics and generates a confusion matrix.
--model_prediction.py: loads the saved model and performs inference on a pre-defined test data.
--model_registry.py: used for future versioning and model tracking features.
--main.py: used for the entire machine learning pipeline including preprocessing, exploratory analysis, training, evaluation, and prediction.

'requirements.txt' will list all required libraries we need for the project.

'Dockerfile' defines how to create a Docker image for our model. 
-- 'FROM python:3.11-slim' is used to prepare a light python envrionment
-- 'WORKDIR/app' is used to set working directory
-- 'COPY requirements.txt requirements.txt' is used to copy local requirements.txt to image/app/requirements.txt
-- 'COPY COPY . .' is used to copy functional '.py' scripts and configuration files to image/app
-- 'RUN pip install --no-cache-dir -r requirements.txt' will execute 'pip' to install scikit-learn
-- 'CMD ["python", "main.py"]' is used to define - when we run the docker container, we will execute python main.py

CLI.py is Command Line Interface. You can just put 'python CLI.py' in your python terminal. And you will see a series of commands. Then you can choose.

If you need to run the project, make sure you have downloaded the DockerDesktop in your computer, and keep you logged in.

If you want to run and test the entire project, from build, run, push, pull, delete, stop..., please make sure you replace all 'zhongkesun' in my 'CLI.py' to your Docker account name.

If you just want to try our model, you can run 'python CLI.py pull' in your python terminal, then you will have our model, run 'run_model' you will get a result.

You can use the following commands via our 'CLI.py'

- python CLI.py build
- python CLI.py run_container
- python CLI.py push
- python CLI.py pull
- python CLI.py run_model
- python CLI.py stop
- python CLI.py delete
- python CLI.py train
- python CLI.py predict
- python CLI.py visualize

Please feel free to email us if you have any other questions about the project.
