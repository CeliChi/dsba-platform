**Group Members**: Yunhang Chi, Wenxi Huang, Shiyu Mao, Zhongke Sun  
**Date**: April 9, 2025  

This is README.txt file for our MLOps project

The project includes the following files

<pre>
/dsba-platform
├── main.py
├── get_path.py
├── preprocessing.py
├── model_training.py
├── model_evaluation.py
├── model_prediction.py
├── model_registry.py
├── __init__.py
├── requirements.txt
├── Dockerfile
└── CLI.py
</pre>



Let us explain how the project work:

Firstly, the project aim to build a docker and realize the most classical model in the machine learning -- using RandomForestClassifier to classify the iris dataset.

You will find all model code in the '.py' scripts:
- get_path.py: used to get the project path, and create relevant directories.
- preprocessing.py: used for dataset loading, splitting, and exploratory data analysis through visualizations.
- model_training.py: defines and trains a RandomForestClassifier, then saves the trained model to model.pkl and invokes evaluation.
- model_evaluation.py: computes standard performance metrics and generates a confusion matrix.
- model_prediction.py: loads the saved model and performs inference on a pre-defined test data.
- model_registry.py: used for future versioning and model tracking features.
- main.py: used for the entire machine learning pipeline including preprocessing, exploratory analysis, training, evaluation, and prediction.

'requirements.txt' will list all required libraries we need for the project.

'Dockerfile' defines how to create a Docker image for our model. 
<pre>
'FROM python:3.11-slim'                              # Used to prepare a light python envrionment
'WORKDIR/app'                                        # Used to set working directory
'COPY requirements.txt requirements.txt'             # Used to copy local requirements.txt to image/app/requirements.txt
'COPY COPY . .'                                      # Used to copy functional '.py' scripts and configuration files to image/app
'RUN pip install --no-cache-dir -r requirements.txt' # Will execute 'pip' to install scikit-learn
'CMD ["python", "main.py"]'                          # Used to define - when we run the docker container, we will execute python main.py
</pre>


CLI.py is Command Line Interface. You can just put 'python CLI.py' in your python terminal. And you will see a series of commands. Then you can choose.

If you need to run the project, make sure you have downloaded the DockerDesktop in your computer, and keep you logged in.

If you want to run and test the entire project, from build, run, push, pull, delete, stop..., please make sure you replace all 'wenxi1203' with your Docker account username.

If you just want to try our model, you can run 'python CLI.py pull' in your python terminal, then you will have our model, run 'run_model' you will get a result.

You can use the following commands via our 'CLI.py'

<pre>
python CLI.py build
python CLI.py run_container
python CLI.py push
python CLI.py pull
python CLI.py run_model
python CLI.py stop
python CLI.py delete
python CLI.py train
python CLI.py predict
python CLI.py visualize
</pre>


Please feel free to email us if you have any other questions about the project.
