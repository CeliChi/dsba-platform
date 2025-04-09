'''
Author : Zhongke Sun
Date : 2025/04/09

ATTENTION: If you need to run this entire project, please replace all 'wenxi1203' with your Docker account username, otherwise you will get an error when build/push your container and image.
ATTENTION: Otherwise, if you just want to run our model, you can just 'pull' my Docker image from Docker Hub and run it. (I have already pushed my Docker image to Docker Hub)
'''


import argparse
import os
from pathlib import Path

DOCKER_IMAGE = "wenxi1203/ml_iris_model"
CONTAINER_NAME = "iris_container"

os.chdir(Path(__file__).resolve().parent)

# This function is to build the Docker image
def build_image():
    os.system(f"docker build -t {DOCKER_IMAGE} .")

# This function is to run the Docker container
def run_container():
    os.system(f"docker run --name {CONTAINER_NAME} {DOCKER_IMAGE}")

# This function is to push my Docker image to Docker Hub
def push_image():
    os.system("docker login")
    os.system(f"docker push {DOCKER_IMAGE}")

# This function is to pull my Docker image from Docker Hub
def pull_image():
    os.system(f"docker pull {DOCKER_IMAGE}")

# This function is to run my Docker image, my iris machine learning model
def run_model():
    os.system(f"docker run {DOCKER_IMAGE}")

# This function is to stop my Docker container
def stop_container():
    os.system(f"docker stop $(docker ps -q --filter ancestor={DOCKER_IMAGE})")

# This function is to delete my Docker container
def delete_container():
    os.system(f"docker rm $(docker ps -aq --filter ancestor={DOCKER_IMAGE})")

# This function is to train the model (from model_training.py)
def train_model():
    os.system("python model_training.py")

# This function is to run prediction (from model_prediction.py)
def run_prediction():
    os.system("python model_prediction.py")

# This function is to run exploratory visualization
def run_visualization():
    os.system("python -c \"from preprocessing import exploratory_analysis; exploratory_analysis()\"")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MLOPS CLI for Docker and ML workflow")
    parser.add_argument('command', choices=[
        'build', 'run_container', 'push', 'pull', 'run_model',
        'stop', 'delete', 'train', 'predict', 'visualize'
    ], help="Command to execute")

    args = parser.parse_args()

    if args.command == 'build':
        build_image()
    elif args.command == 'run_container':
        run_container()
    elif args.command == 'push':
        push_image()
    elif args.command == 'pull':
        pull_image()
    elif args.command == 'run_model':
        run_model()
    elif args.command == 'stop':
        stop_container()
    elif args.command == 'delete':
        delete_container()
    elif args.command == 'train':
        train_model()
    elif args.command == 'predict':
        run_prediction()
    elif args.command == 'visualize':
        run_visualization()
