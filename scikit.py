import numpy as np
from sklearn.linear_model import SGDRegressor
import matplotlib.pyplot as plt


# Create an array of x values from -10 to 10 with 0.1 interval
x = np.linspace(-2,2,2023)

# Calculate the y values for the function 3x^2-3x+4
y = 3 * x**2 - 3 * x + 4

# Reshape the arrays to fit the model
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

plt.plot(x)

# Create an SGDRegressor object with a small learning rate and no regularization
sgd = SGDRegressor(learning_rate='constant', eta0=0.001, penalty=None)

# Fit the model to the data
sgd.fit(x, y.ravel())

# Print the coefficients and intercept of the model
print('Coefficients:', sgd.coef_)
print('Intercept:', sgd.intercept_)

# Compare with the analytical solution: x = 0.5, y = 2.75
print('Analytical solution: x = 0.5, y = 2.75')