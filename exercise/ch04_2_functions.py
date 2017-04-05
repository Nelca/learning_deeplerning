import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from common.functions import softmax, cross_entropy_error
from two_layer_net import TwoLayerNet


hint_nu_diff = """Numericl diff is as follow.

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

And check defined function as follow.
checkNuDiff()
"""
hint_grad_desc = """Gradient descent function as follow.

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_history = []

    for i in range(step_num):
        x_history.append( x.copy() )

        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, np.array(x_history)


And check defined function as follow.
checkGradDesc()
"""
view_simple_net = """Simple net is as follow.

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

"""
hint_weight_param = """
W1 param is as follow.
W1 = weight_init_std * np.random.randn(input_size, hidden_size)

So, you can define the weight as follow.
tlNet.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)

and check the answe as follow.
checkTlnetParam(tlNet)
"""
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

init_x = np.array([-3.0, 4.0])    

# for check answer net
weight_init_std =  0.01
input_size=784
hidden_size=50
output_size=10
net = TwoLayerNet(input_size=input_size, hidden_size=hidden_size, output_size=output_size)

# for answer net
tlNet = TwoLayerNet(input_size=input_size, hidden_size=hidden_size, output_size=output_size)

def collect_numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def chk_function(x):
    return 0.01*x**2 + 0.1*x 

def chk_function_2(x):
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)

def chk_function_3(x):
    return x[0]**2 + x[1]**2


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

def collect_gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_history = []

    for i in range(step_num):
        x_history.append( x.copy() )

        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, np.array(x_history)

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

dummy_f = lambda w: net.loss(x, t)

print("*****************************")
print("")
print("This chpater is lerning diffelential.")
print("")
print("Let's define the function of numerical diff.")
print("Like this->'numerical_diff'")
print("")
print("And check defined function as follow.")
print("checkNuDiff()")

def checkNuDiff(skip=False):
    x = 5
    f = chk_function
    ans = numerical_diff(f, x)
    collect_ans = collect_numerical_diff(f, x)
    if ans == collect_ans or skip:
        print("")
        print("OK!")
        print("Let's move to next step.")
        print("Next is lerning gradient.")
        print("")
        print("Let's check the gradient results as follow.")
        print("numerical_gradient(chk_function_2, np.array([3.0, 4.0]))")
        print("")
        print("or type this 'next_of_gradient_chk'")
        print("")
    else:
        print("")
        print("Mmmmm.")
        print("It's not collect of function.")
        print("")
        print("If you want hint type this ->")
        print("hint_nu_diff")
        print("")


def checkGradDesc(skip=False):
    f = chk_function_3
    init_x = np.array([-3.0, 4.0])    
    ans, ans_history = gradient_descent(f, init_x)
    collect_ans, collect_ans_history = collect_gradient_descent(f, init_x)
    if all(ans==collect_ans) or skip:
        print("")
        print("That's good !!!!")
        print("Next is nueral net gradient.")
        print("Check the neural net step by step.")
        print("")
        print("First of all, define neural net as follow.")
        print("net = simpleNet()")
        print("")
        print("If you want to see simple net, type this-> ")
        print("view_simple_net")
    else:
        print("")
        print("Mmmmm.")
        print("It's not collect of function.")
        print("")
        print("If you want hint type this ->")
        print("hint_grad_diff")
        print("")
        print("Or you will skip this")
        print("checkGradDesc(skip=True)")
        print("")

def checkTlnetParam(tlNet):
    ans = tlNet.params['W1']
    if ans.shape[0]==input_size and ans.shape[1]==hidden_size:
        print("")
        print("That's good !!!")
        print("")
        print("Next is the neteork bias.")
        print("So you define biases as follow.")
        print("tlNet.params['W1'] = bar")
        print("")
        print("And check the bias as follow.")
        print("checkBiasParan(tlNet)")
    else:
        print("")
        print("Mmmm it's not collect param defined.")
        print("")
        print("If you want the hint, type this ->")
        print("hint_weight_param")
        print("")
        print("And check the param as follow")
        print("checkTlnetParam(tlNet)")

def nextChapter(file_name="ch5.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

