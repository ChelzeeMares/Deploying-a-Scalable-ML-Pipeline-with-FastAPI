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
   
    # Generate dummy data
    X, y = make_classification(n_samples=100, n_features=20, random_state=42)
    
    # Call the train_model function
    model = train_model(X, y)
    
    # Assert that the returned object is of type LogisticRegression (or any other expected type)
    self.assertIsInstance(model, LogisticRegression)

if __name__ == '__main__':
    unittest.main()
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # add description for the second test
    """
    X, y = make_classification(n_samples=100, n_features=20, random_state=42)
        
    # Call the train_model function
    model = train_model(X, y)
    
    # Check if the model uses Logistic Regression algorithm
    self.assertTrue(isinstance(model, LogisticRegression))
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Example ground truth labels and predictions
    y_true = [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
    y_pred = [0, 1, 1, 0, 1, 0, 0, 0, 1, 1]  # One false negative, one false positive
    
    # Expected values for precision, recall, and F1-score
    expected_precision = 0.8333
    expected_recall = 0.8333
    expected_f1 = 0.8333
    
    # Call the compute_model_metrics function
    precision, recall, f1 = compute_model_metrics(y_true, y_pred)
    
    # Compare computed metrics with expected values
    self.assertAlmostEqual(precision, expected_precision, places=4)
    self.assertAlmostEqual(recall, expected_recall, places=4)
    self.assertAlmostEqual(f1, expected_f1, places=4)
pass
