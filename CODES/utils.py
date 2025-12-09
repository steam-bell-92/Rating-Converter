"""
Utility functions for plotting and visualization.
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_cost_history(J_history):
    """
    Plot the cost function history over iterations.
    
    Args:
        J_history: List of cost values from training
    """
    plt.figure(figsize=(10, 6))
    plt.plot(J_history, linewidth=2)
    plt.xlabel('Iteration (x1000)')
    plt.ylabel('Cost')
    plt.title('Cost Function History During Gradient Descent')
    plt.grid(True)
    plt.show()


def plot_regression_line(X, y, w, b):
    """
    Plot the data points and the regression line.
    
    Args:
        X: Input features (numpy array)
        y: Target values (numpy array)
        w: Weight parameter (scalar)
        b: Bias parameter (scalar)
    """
    plt.figure(figsize=(10, 6))
    
    # Plot data points
    plt.scatter(X, y, alpha=0.5, label='Training Data')
    
    # Plot regression line
    x_line = np.linspace(X.min(), X.max(), 100)
    y_line = w * x_line + b
    plt.plot(x_line, y_line, 'r-', linewidth=2, label=f'y = {w:.6f}x + {b:.2f}')
    
    plt.xlabel('CodeChef Rating')
    plt.ylabel('Codeforces Rating')
    plt.title('Linear Regression: CodeChef vs Codeforces Ratings')
    plt.legend()
    plt.grid(True)
    plt.show()


def compute_r2_score(y_true, y_pred):
    """
    Compute the R² score for model evaluation.
    
    Args:
        y_true: True target values (numpy array)
        y_pred: Predicted values (numpy array)
    
    Returns:
        R² score (scalar)
    """
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    return r2


def print_model_summary(w, b, X, y):
    """
    Print a summary of the trained model.
    
    Args:
        w: Weight parameter (scalar)
        b: Bias parameter (scalar)
        X: Input features (numpy array)
        y: Target values (numpy array)
    """
    y_pred = w * X + b
    r2 = compute_r2_score(y, y_pred)
    
    print("\n" + "="*50)
    print("MODEL SUMMARY")
    print("="*50)
    print(f"Final Model: y = ({w:.6f})x + ({b:.2f})")
    print(f"Weight (w): {w:.6f}")
    print(f"Bias (b): {b:.2f}")
    print(f"R² Score: {r2:.6f}")
    print("="*50 + "\n")
