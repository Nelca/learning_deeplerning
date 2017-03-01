import numpy as np
import sys

print("sigmoid is this->1 / (1 + np.exp(-x))")
print("So let's define sigmoid function:")
print("first of all a = np.array([1, 2, 3])")

check_a = np.array([1, 2, 3])
check_b = np.array([[1, 2, 3], [4, 5, 6]])


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

check_c = sigmoid(check_a)
