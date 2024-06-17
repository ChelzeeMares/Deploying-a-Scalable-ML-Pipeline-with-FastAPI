import pytest
import unittest
from ml.model import train_model
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from ml.model import compute_model_metrics

#Test One
#Test train model
def test_train_model(self):
    model = train_model()
    self.assertIsInstance(model, LogisticRegression)  # Replace SomeModelClass with the actual model class

def test_predict(self):
    predictions = predict()
    self.assertIsInstance(predictions, np.ndarray)  # Assuming predictions are returned as a NumPy array

def test_evaluate_model(self):
    evaluation = evaluate_model()
    self.assertIsInstance(evaluation, dict)  # Assuming evaluation returns a dictionary




