import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist


hint_nu_diff = """Numericl diff is as follow.

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

And check defined function as follow.
checkNuDiff()
"""

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

def collect_numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def chk_function(x):
    return 0.01*x**2 + 0.1*x 

def _numerical_gradient_no_batch(f, x):
    h = 1e-4
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
    if ans == collect_ans:
        print("")
        print("OK!")
        print("Let's move to next step.")
        print("The numerical diff is not fit a array.")
        print("Nu is not ")
        print("")
        print("")
    else:
        print("")
        print("Mmmmm.")
        print("It's not collect of function.")
        print("")
        print("If you want hint type this ->")
        print("hint_nu_diff")
        print("")

def nextChapter(file_name="ch5.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

