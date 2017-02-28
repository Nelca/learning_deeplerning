import numpy as np
import sys

print("")
print("")
print("")
print("Hello. This section is lerning activation function.")
print("")
print("First of all, let's  define a test function.")
print("Be careful whith indentation.")
print("type this ")
print("")
print("def testFunction() :")
print("    print (\"Greate!\")")
print("    checkDefFunc()")
print("")
print("and type this->testFunction()")

def sigmoid(x):
    return 1 / (1 + np.exp(-x))    

def relu(x):
    return np.maximum(0, x)

def checkDefFunc():
    print("You can now define the function.")
    print("So next step is check array kyodou ")
    print("")
    print("type this-> x = np.array([-1, 1, 2])")
    print("y = x > 0")
    print("y")
    print("")
    print("")
    print("Is displayed this ? ")
    print("array([False, True, True], dtype=bool)")
    with open("ch03_1.py") as ch03_1_f:
        ch03_1_code = ch03_1_f.read()
        exec(ch03_1_code)

