"""
Simple example demonstrating how to use the refactored modules.
This shows the modular nature of the code.
"""
import numpy as np
from math_logic import compute_prediction, compute_cost, compute_gradient
from optimizer import gradient_descent

# Simple synthetic data for demonstration
print("="*50)
print("SIMPLE DEMONSTRATION")
print("="*50 + "\n")

# Create simple linear data: y = 2x + 3 with some noise
np.random.seed(42)
X_simple = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_simple = 2 * X_simple + 3 + np.random.randn(10) * 0.5

print("Training on simple linear data: y ≈ 2x + 3")
print(f"Data points: {len(X_simple)}")
print(f"X: {X_simple}")
print(f"y: {y_simple.round(2)}\n")

# Initial parameters
w_init = 0.0
b_init = 0.0

print(f"Initial parameters: w={w_init}, b={b_init}")

# Compute initial cost
initial_cost = compute_cost(X_simple, y_simple, w_init, b_init)
print(f"Initial cost: {initial_cost:.4f}\n")

# Run gradient descent
print("Running gradient descent...")
w_final, b_final, J_history = gradient_descent(
    X_simple, y_simple,
    w_init, b_init,
    alpha=0.01,  # Higher learning rate for small dataset
    num_iters=1000,
    cost_function=compute_cost,
    gradient_function=compute_gradient,
    reg_lambda=0  # No regularization for this simple example
)

print(f"\nFinal parameters: w={w_final:.4f}, b={b_final:.4f}")
print(f"Final model: y = {w_final:.4f}x + {b_final:.4f}")
print(f"Expected: y ≈ 2.0x + 3.0")

# Compute final cost
final_cost = compute_cost(X_simple, y_simple, w_final, b_final)
print(f"Final cost: {final_cost:.4f}")
print(f"Cost reduction: {initial_cost - final_cost:.4f}\n")

# Make predictions
y_pred = compute_prediction(X_simple, w_final, b_final)
print("Sample predictions:")
for i in range(0, 10, 3):
    print(f"  x={X_simple[i]:.0f}: y_true={y_simple[i]:.2f}, y_pred={y_pred[i]:.2f}")

print("\n" + "="*50)
print("DEMONSTRATION COMPLETE")
print("="*50)
