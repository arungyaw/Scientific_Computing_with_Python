import numpy as np

y = np.array([10,20])
predictions = np.array([8,25])

minus = y - predictions
errors = (minus) ** 2
mse = np.mean(errors)

print(minus)
print(errors)
print(mse)