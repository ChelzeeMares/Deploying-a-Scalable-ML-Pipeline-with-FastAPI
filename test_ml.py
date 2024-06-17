import pytest
import unittest
from ml.model import train_model
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from ml.model import compute_model_metrics

#Test One
#Test train model
def test_train_model():
    model = train_model()
    assertIsInstance(model, LogisticRegression)


def test_predict():
    predictions = predict()
    assertIsInstance(predictions, np.ndarray)

def test_evaluate_model():
    evaluation = evaluate_model()
    assertIsInstance(evaluation, dict) 




