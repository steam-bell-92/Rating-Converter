# Linear Regression Training Code

This directory contains a production-ready Python implementation of the univariate linear regression model for converting ratings between CodeChef and Codeforces.

## File Structure

- **config.py**: Configuration file with all hyperparameters
  - Learning rate, number of iterations
  - Initial parameters (w, b)
  - Regularization parameter
  - Data file path

- **math_logic.py**: Core mathematical functions
  - `compute_prediction(X, w, b)`: Model prediction f(w,b) = wx + b
  - `compute_cost(X, y, w, b, reg_lambda)`: Cost function with regularization
  - `compute_gradient(X, y, w, b, reg_lambda)`: Gradient computation

- **optimizer.py**: Gradient descent implementation
  - `gradient_descent()`: Optimizes parameters using gradient descent
  - Accepts cost and gradient functions as arguments
  - Returns final parameters and cost history

- **utils.py**: Visualization and utility functions
  - `plot_cost_history()`: Plot cost over iterations
  - `plot_regression_line()`: Plot data and fitted line
  - `compute_r2_score()`: Calculate R² score
  - `print_model_summary()`: Display model results

- **main.py**: Main entry point
  - Loads and preprocesses data
  - Runs gradient descent
  - Displays results and plots

## Usage

### Basic Usage

```bash
# Install dependencies
pip install numpy pandas matplotlib

# Run the training pipeline
python main.py
```

### Expected Output

The model will train for 100,000 iterations and produce:
- Final weight (w): ~0.915958
- Final bias (b): ~-185.00
- R² Score: ~0.391470

These values match the original Jupyter notebook implementation.

## Model Details

- **Type**: Univariate Linear Regression
- **Algorithm**: Gradient Descent with L2 Regularization
- **Dataset**: CodeChef and Codeforces ratings (6256 samples after outlier removal)
- **Formula**: `codeforces_rating = w × codechef_rating + b`

## Configuration

To modify hyperparameters, edit `config.py`:

```python
LEARNING_RATE = 3.3e-7    # Learning rate
NUM_ITERATIONS = 100000    # Number of gradient descent iterations
INITIAL_W = 1.0           # Initial weight
INITIAL_B = -185.0        # Initial bias
REG_LAMBDA = 1000         # L2 regularization parameter
```

## Module Usage

You can also import and use individual components:

```python
from config import LEARNING_RATE, NUM_ITERATIONS
from math_logic import compute_prediction, compute_cost, compute_gradient
from optimizer import gradient_descent
import numpy as np

# Your training data
X_train = np.array([1104, 1200, 1500, ...])
y_train = np.array([286, 400, 700, ...])

# Run gradient descent
w, b, J_history = gradient_descent(
    X_train, y_train,
    w_in=1.0, b_in=-185.0,
    alpha=LEARNING_RATE,
    num_iters=NUM_ITERATIONS,
    cost_function=compute_cost,
    gradient_function=compute_gradient,
    reg_lambda=1000
)

# Make predictions
predictions = compute_prediction(X_train, w, b)
```
