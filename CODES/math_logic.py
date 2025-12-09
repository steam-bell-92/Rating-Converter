"""
Core mathematical functions for linear regression.
"""
import numpy as np


def compute_prediction(X, w, b):
    """
    Compute the model prediction.
    
    Args:
        X: Input features (numpy array)
        w: Weight parameter (scalar)
        b: Bias parameter (scalar)
    
    Returns:
        Predicted values: f(w,b) = w * x + b
    """
    return w * X + b


def compute_cost(X, y, w, b, reg_lambda=0):
    """
    Compute the cost function (MSE with optional regularization).
    
    Args:
        X: Input features (numpy array)
        y: Target values (numpy array)
        w: Weight parameter (scalar)
        b: Bias parameter (scalar)
        reg_lambda: Regularization parameter (scalar, default=0)
    
    Returns:
        Total cost (scalar)
    """
    m = len(X)
    y_pred = compute_prediction(X, w, b)
    error = y_pred - y
    
    # Mean squared error
    mse = np.sum(error ** 2) / (2 * m)
    
    # Add regularization term
    regularization = (reg_lambda / (2 * m)) * (w ** 2)
    
    return mse + regularization


def compute_gradient(X, y, w, b, reg_lambda=0):
    """
    Compute the gradient of the cost function.
    
    Args:
        X: Input features (numpy array)
        y: Target values (numpy array)
        w: Weight parameter (scalar)
        b: Bias parameter (scalar)
        reg_lambda: Regularization parameter (scalar, default=0)
    
    Returns:
        dw: Gradient with respect to w (scalar)
        db: Gradient with respect to b (scalar)
    """
    m = len(X)
    y_pred = compute_prediction(X, w, b)
    error = y_pred - y
    
    # Gradient for weight (with regularization)
    dw = np.dot(X, error) + reg_lambda * w
    
    # Gradient for bias (no regularization on bias)
    db = np.sum(error)
    
    return dw, db
