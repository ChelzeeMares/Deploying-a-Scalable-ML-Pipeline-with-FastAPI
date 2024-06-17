import pytest
import unittest
from ml.model import train_model
from ml.model import predict
from ml.model import evaluate_model
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from ml.model import compute_model_metrics

#Test One
#Test train model
def test_train_model():
    model = train_model()
    assert IsInstance(model, LogisticRegression)





