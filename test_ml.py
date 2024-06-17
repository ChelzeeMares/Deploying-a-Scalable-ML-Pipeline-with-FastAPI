import pytest
import unittest
from ml.model import train_model
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from ml.model import compute_model_metrics

#Test One
#Test train model
def test_train_model():
    X_train = [[1, 2], [3, 4], [5, 6]]
    y_train = [0, 1, 0]
    model = train_model(X_train, y_train)
    assert IsInstance(model, LogisticRegression)





