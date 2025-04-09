import pickle
from preprocessing import load_and_preprocess_data
from get_path import get_model_dir

def predict():
    # Load trained model
    trained_model_path = get_model_dir() / "model.pkl"
    with open(trained_model_path, 'rb') as f:
        model = pickle.load(f)
        print(f"Model loaded from {trained_model_path}")

        _, X_test, _, y_test = load_and_preprocess_data()
        test_sample = X_test[0].reshape(1, -1)
        prediction = model.predict(test_sample)
        print(f"Prediction for {test_sample.tolist()}: {prediction}")
        print(f"True label: {y_test[0]}")

if __name__ == '__main__':
    predict()