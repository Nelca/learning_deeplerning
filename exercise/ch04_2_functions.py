import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
batch_size = 10

def collect_numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def chk_function(x):
    return 0.01*x**2 + 0.1*x 

def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

def _numerical_gradient_no_batch(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val
        
    return grad


def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        
        return grad


print("*****************************")
print("")
print("This chpater is lerning diffelential.")
print("")
print("Let's define the function of numerical diff.")
print("Like this->'numerical_diff'")
print("")
print("And check defined function as follow.")
print("checkNuDiff()")

def checkNuDiff():
    x = 5
    f = chk_function
    ans = numerical_diff(f, x)
    collect_ans = collect_numerical_diff(f, x)
    if True:
        print("")
        print("OK!")
        print("")
    else:
        print("")
        print("NG")
        print("")

def nextChapter(file_name="ch5.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

