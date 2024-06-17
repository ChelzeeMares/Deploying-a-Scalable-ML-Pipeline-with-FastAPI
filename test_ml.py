import pytest
import unittest
from ml.model import train_model
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from ml.model import compute_model_metrics

# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_train_model(self):
    model = train_model()
    self.assertIsInstance(model, LogisticRegression)


# TODO: implement the second test. Change the function name and input as needed
def test_predict(self):
    predictions = predict()
    self.assertIsInstance(predictions, np.ndarray)

def test_evaluate_model(self):
    evaluation = evaluate_model()
    self.assertIsInstance(evaluation, dict) 
