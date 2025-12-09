"""
Main entry point for the linear regression training pipeline.
"""
import numpy as np
import pandas as pd
from config import (
    LEARNING_RATE, NUM_ITERATIONS, INITIAL_W, INITIAL_B, 
    REG_LAMBDA, DATA_FILE_PATH
)
from math_logic import compute_cost, compute_gradient
from optimizer import gradient_descent
from utils import plot_cost_history, plot_regression_line, print_model_summary


def load_and_prepare_data(file_path):
    """
    Load data from CSV file and prepare training data.
    
    Args:
        file_path: Path to the CSV file
    
    Returns:
        X_train: Input features (numpy array)
        y_train: Target values (numpy array)
    """
    # Read CSV file
    df = pd.read_csv(file_path)
    
    # Drop rows with missing values
    df.dropna(inplace=True)
    
    # Remove outliers using IQR method (matching notebook's implementation exactly)
    # Note: This matches the notebook's behavior where df1 is overwritten in each iteration,
    # so only the last column's (cc_rating) outlier filter is effectively applied.
    # This preserves the exact same data filtering as the original implementation.
    for i in ['cf_rating', 'cc_rating']:
        Q1 = df[i].quantile(0.25)
        Q3 = df[i].quantile(0.75)
        
        lower_bound = Q1 - 1.5 * (Q3 - Q1)
        upper_bound = Q3 + 1.5 * (Q3 - Q1)
        
        df1 = df[(df[i] >= lower_bound) & (df[i] <= upper_bound)]
    
    # Use df1 which has the last iteration's filter applied
    df = df1
    
    # Prepare training data
    X_train = df['cc_rating'].to_numpy().flatten()
    y_train = df['cf_rating'].to_numpy().flatten()
    
    print(f"Loaded {len(X_train)} training samples")
    print(f"CodeChef Rating Range: [{X_train.min():.0f}, {X_train.max():.0f}]")
    print(f"Codeforces Rating Range: [{y_train.min():.0f}, {y_train.max():.0f}]")
    
    return X_train, y_train


def main():
    """
    Main function to run the training pipeline.
    """
    print("\n" + "="*50)
    print("UNIVARIATE LINEAR REGRESSION TRAINING")
    print("="*50 + "\n")
    
    # Load and prepare data
    print("Loading data...")
    X_train, y_train = load_and_prepare_data(DATA_FILE_PATH)
    print()
    
    # Run gradient descent
    print(f"Starting gradient descent with:")
    print(f"  Learning Rate: {LEARNING_RATE}")
    print(f"  Iterations: {NUM_ITERATIONS}")
    print(f"  Initial w: {INITIAL_W}")
    print(f"  Initial b: {INITIAL_B}")
    print(f"  Regularization λ: {REG_LAMBDA}")
    print()
    
    w, b, J_history = gradient_descent(
        X_train, y_train,
        INITIAL_W, INITIAL_B,
        LEARNING_RATE, NUM_ITERATIONS,
        compute_cost, compute_gradient,
        REG_LAMBDA
    )
    
    # Print final results
    print_model_summary(w, b, X_train, y_train)
    
    # Plot results
    print("Generating plots...")
    plot_cost_history(J_history)
    plot_regression_line(X_train, y_train, w, b)
    
    print("\nTraining complete!")


if __name__ == "__main__":
    main()
