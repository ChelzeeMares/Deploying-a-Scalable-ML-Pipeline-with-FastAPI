import pytest
import unittest
from ml.model import train_model
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from ml.model import compute_model_metrics

# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # add description for the first test
    """
   
    X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
    
    model = train_model(X, y)
    
    unittest.TestCase().assertIsInstance(model, LogisticRegression)

if __name__ == '__main__':
    unittest.main()
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # add description for the second test
    """
    X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
        
    model = train_model(X, y)
    
    unittest.TestCase().assertTrue(isinstance(model, LogisticRegression))
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """

    y_true = [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
    y_pred = [0, 1, 1, 0, 1, 0, 0, 0, 1, 1]  # One false negative, one false positive
    
    # Expected values for precision, recall, and F1-score
    expected_precision = 0.7285
    expected_recall = 0.2699
    expected_f1 = 0.3939
    
    # Call the compute_model_metrics function
    precision, recall, f1 = compute_model_metrics(y_true, y_pred)
    
    # Compare computed metrics with expected values
    unittest.TestCase().assertAlmostEqual(precision, expected_precision, delta=0.3)
    unittest.TestCase().assertAlmostEqual(recall, expected_recall, delta=0.3)
    unittest.TestCase().assertAlmostEqual(f1, expected_f1, delta=0.3)
pass
