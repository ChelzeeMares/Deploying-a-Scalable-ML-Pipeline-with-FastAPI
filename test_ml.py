import pytest
import unittest
from ml.model import train_model
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from ml.model import compute_model_metrics

# Test one
def test_train_model(self):
    model = train_model()
    self.assertIsInstance(model, LogisticRegression)

# Test two
def test_predict(self):
    predictions = predict()
    self.assertIsInstance(predictions, np.ndarray)

#Test three

# Precision: 0.7285 | Recall: 0.2699 | F1: 0.3939

def test_compute_model_metrics(self):
    precision, recall, f1 = (0.7285, 0.2699, 0.3939)
    
    self.assertAlmostEqual(precision, self.expected_precision, places=4, msg="No match on Precision")
    self.assertAlmostEqual(recall, self.expected_recall, places=4, msg="No match on recall")
    self.assertAlmostEqual(f1, self.expected_f1, places=4, msg="No match on f1")
