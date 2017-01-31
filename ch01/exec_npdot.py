# coding: utf-8
import numpy as np
import pdb

a = np.array([1, 2, 3])
b = np.array([[4, 5], [4, 5], [4, 5]])

c = np.random.randn(63,)
d = np.random.randn(63,5)
shape_a = a.shape
shape_b = b.shape

pdb.set_trace()

result = np.dot(a, b)
result_2 = np.dot(c, d)

print(result)
print(result_2)

