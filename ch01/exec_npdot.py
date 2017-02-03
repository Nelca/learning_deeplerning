import numpy as np
import pdb

def testFunc(np_array):
    shape = np_array.shape
    print(shape)

a = np.random.randn(100,)
b = np.random.randn(100,5)
testFunc(a)

pdb.set_trace()

np.dot(a, b)
result = np.dot(a, b)

print(result)

