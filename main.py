from model_training import train_model
from model_prediction import predict
from preprocessing import exploratory_analysis
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

if __name__ == "__main__":
    exploratory_analysis()
    train_model()
    predict()