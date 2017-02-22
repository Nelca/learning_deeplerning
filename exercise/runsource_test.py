import numpy as np

print("it's a rs file!!")
print("is this printed?")

a = np.array([1, 2])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.dot(a, b)

def print_func():
    print("print_func")


def print_func_with_arg(a):
    print(a)
