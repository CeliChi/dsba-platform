from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt
from get_path import get_plot_output_dir

def evaluate_model(model, X, y):
    y_predicted = model.predict(X)

    accuracy = accuracy_score(y, y_predicted)
    precision = precision_score(y, y_predicted, average="weighted", zero_division=0)
    recall = recall_score(y, y_predicted, average="weighted", zero_division=0)
    f1 = f1_score(y, y_predicted, average="weighted", zero_division=0)
    conf_matrix = confusion_matrix(y, y_predicted)

    print("Evaluation Metrics:")
    print(f"  Accuracy : {accuracy:.2f}")
    print(f"  Precision: {precision:.2f}")
    print(f"  Recall   : {recall:.2f}")
    print(f"  F1 Score : {f1:.2f}")
    print(f"  Confusion Matrix:\n{conf_matrix}")

    disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.savefig(get_plot_output_dir() / "confusion_matrix.png")
    print("Confusion matrix saved as confusion_matrix.png")

    # Fairness evaluation by class
    classes = np.unique(y)
    print("Per-Class Accuracy:")
    for cls in classes:
        indices = np.where(y == cls)[0]
        y_cls = y[indices]
        y_pred_cls = y_predicted[indices]
        acc = accuracy_score(y_cls, y_pred_cls)
        print(f"  Class {cls} accuracy: {acc:.2f}")