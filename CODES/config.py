"""
Configuration file for storing all hyperparameters and constants.
"""

# Hyperparameters for gradient descent
LEARNING_RATE = 3.3e-7
NUM_ITERATIONS = 100000

# Initial parameter values
INITIAL_W = 1.0  # Initial weight (slope of line)
INITIAL_B = -185.0  # Initial bias (y-intercept of line)

# Regularization parameter
REG_LAMBDA = 1000  # Lambda parameter for regularization term

# File paths
DATA_FILE_PATH = 'final_cccf.csv'
