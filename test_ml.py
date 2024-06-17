import pytest
import unittest
from ml.model import train_model, inference, compute_model_metrics
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import numpy as np

#Test One
#Test train model
def test_train_model():
    X_train = [[1, 2], [3, 4], [5, 6]]
    y_train = [0, 1, 0]
    model = train_model(X_train, y_train)
    assert isinstance(model, LogisticRegression)

#Test Two

def test_inference():
    X_train = [[1, 2], [3, 4], [5, 6]]
    y_train = [0, 1, 0]
    X_test = [[7, 8], [9, 10]]
    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    assert isinstance(preds, np.ndarray)
    assert preds.shape == (len(X_test),)

#Test Three

def test_compute_model_metrics():
 
    y_true = [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
    y_pred = [0, 1, 1, 0, 1, 0, 0, 0, 1, 1]  # One false negative, one false positive
    
    # Expected values for precision, recall, and F1-score
    expected_precision = 0.8333
    expected_recall = 0.8333
    expected_f1 = 0.8333
    
    # Call the compute_model_metrics function
    precision, recall, f1 = compute_model_metrics(y_true, y_pred)
    
    # Compare computed metrics with expected values
    unittest.TestCase().assertAlmostEqual(precision, expected_precision, delta=1)
    unittest.TestCase().assertAlmostEqual(recall, expected_recall, delta=1)
    unittest.TestCase().assertAlmostEqual(f1, expected_f1, delta=1)



