from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
from get_path import get_plot_output_dir

def load_and_preprocess_data(test_size=0.2, random_state=42):
    # Load the iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split the dataset into training and test set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test

def exploratory_analysis():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = iris.target_names[df['species']]

    # Plot species count
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='species')
    plt.title("Species Count")
    plt.savefig(get_plot_output_dir() / "species_count.png")
    plt.show()
    plt.close()

    # Comparison of petal length and width by species
    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=df, x='petal length (cm)', y='petal width (cm)', hue='species')
    plt.title("Petal Length VS Width by Species")
    plt.savefig(get_plot_output_dir() / "petal_length_vs_width.png")
    plt.show()
    plt.close()

    # Comparison of sepal length and width by species
    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', hue='species')
    plt.title("Sepal Length VS Width by Species")
    plt.savefig(get_plot_output_dir() / "sepal_length_vs_width.png")
    plt.show()
    plt.close()

    # Correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.drop('species', axis=1).corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Feature Correlation Matrix")
    plt.savefig(get_plot_output_dir() / "feature_correlation.png")
    plt.show()
    plt.close()

if __name__ == '__main__':
    exploratory_analysis()