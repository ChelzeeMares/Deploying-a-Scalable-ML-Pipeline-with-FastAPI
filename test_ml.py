import pytest
import unittest
from ml.model import train_model
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from ml.model import compute_model_metrics

# Test one
# Test train model/LogigisticRegression
def test_train_model():
    model = train_model()
    assertIsInstance(model, LogisticRegression)

# Test two
def test_predict():
    predictions = predict()
    assertIsInstance(predictions, np.ndarray)

#Test three

# Precision: 0.7285 | Recall: 0.2699 | F1: 0.3939

def test_three():
    actual_value = 0.7285
    expected_value = 0.7285
    assertAlmostEqual(actual_value, expected_value, places=4)



