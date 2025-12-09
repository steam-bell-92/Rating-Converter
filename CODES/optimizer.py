"""
Gradient descent optimizer for linear regression.
"""
import numpy as np


def gradient_descent(X, y, w_in, b_in, alpha, num_iters, cost_function, gradient_function, reg_lambda=0):
    """
    Perform gradient descent to optimize parameters w and b.
    
    Args:
        X: Input features (numpy array)
        y: Target values (numpy array)
        w_in: Initial weight parameter (scalar)
        b_in: Initial bias parameter (scalar)
        alpha: Learning rate (scalar)
        num_iters: Number of iterations (integer)
        cost_function: Function to compute cost
        gradient_function: Function to compute gradients
        reg_lambda: Regularization parameter (scalar, default=0)
    
    Returns:
        w: Optimized weight parameter (scalar)
        b: Optimized bias parameter (scalar)
        J_history: History of cost values (list)
    """
    m = len(X)
    w = w_in
    b = b_in
    J_history = []
    
    for i in range(num_iters):
        # Compute gradients
        dw, db = gradient_function(X, y, w, b, reg_lambda)
        
        # Update parameters
        # Note: This matches the notebook's implementation where alpha is divided by m.
        # The gradient dw already contains the sum (not mean), so we divide by m here.
        w = w - (alpha / m) * dw
        b = b - (alpha / m) * db
        
        # Save cost every 1000 iterations
        if i % 1000 == 0:
            cost = cost_function(X, y, w, b, reg_lambda)
            J_history.append(cost)
            
            # Print progress every 10000 iterations
            if i % 10000 == 0:
                print(f"Iteration {i:6d}: Cost {cost:0.2f}, w: {w:0.6f}, b: {b:0.6f}")
    
    return w, b, J_history
