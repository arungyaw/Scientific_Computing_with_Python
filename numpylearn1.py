import numpy as np

#Creating a vector
student_a = np.array([5,8])

weights = np.array([10,2])

#Creating a matrix

data = np.array([[5,8],[2,10]])

result = np.dot(data,weights)
print(data.shape)

print(result)