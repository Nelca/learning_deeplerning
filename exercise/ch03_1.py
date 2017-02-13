import numpy as np
import sys

print("sigmoid is thid->1 / (1 + np.exp(-x))")
print("So let's define sigmoid function:")

check_a = np.array([1, 2, 3])
check_b = np.array([[1, 2, 3], [4, 5, 6]])

check_c = sigmoid(check_a)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

