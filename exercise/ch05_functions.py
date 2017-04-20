import sys, os
sys.path.append(os.pardir)
from layer_naive import *
import numpy as np
from collections import OrderedDict

disp_mullayer = """
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
"""

hint_ml_forward = """
forword function is as follow.

def forward(self, x, y):
    self.x = x
    self.y = y                
    out = x * y
    return out

So, you define the function as below.
And check the answer as follow.
checkMLForward()

"""

hint_ml_backward = """
backward function is as follow.

def backward(self, dout):
    dx = dout * self.y
    dy = dout * self.x

    return dx, dy

And check defined answers as follow.
checkMLBackward()

"""

hint_relu_forward = """
forward function is as follow.

def forward(self, x):
    self.mask = (x <= 0)
    out = x.copy()
    out[self.mask] = 0

    return out

so, you define the function of Relu.forward .
And check your answer as follow.
checkReLUForward()
"""

hint_relu_backward = """
ReLU backward function is as follow.

def backward(self, dout):
    dout[self.mask] = 0
    dx = dout

    return dx


so, you define the function of Relu.backward .
And check your answer as follow.
checkReLUBadkward()
"""

hint_affine_forward = """
Affine forward is as follow.

def forward(self, x):
    self.original_x_shape = x.shape
    x = x.reshape(x.shape[0], -1)
    self.x = x

    out = np.dot(self.x, self.W) + self.b

    return out

And check your answer as follow.
checkAffineForward()
"""

hint_affine_backward = """
Affine backward is as follow.

def backward(self, dout):
    dx = np.dot(dout, self.W.T)
    self.dW = np.dot(self.x.T, dout)
    self.db = np.sum(dout, axis=0)
    
    dx = dx.reshape(*self.original_x_shape)
    return dx

And check your answer as follow.
checkAffineBackward()
"""

class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

class AnsMulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y                
        out = x * y
        return out

    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x
        return dx, dy

class Relu:
    def __init__(self):
        self.mask = None


class AnsRelu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx


class Affine:
    def __init__(self, W, b):
        self.W =W
        self.b = b
        
        self.x = None
        self.original_x_shape = None
        self.dW = None
        self.db = None

class AnsAffine:
    def __init__(self, W, b):
        self.W =W
        self.b = b
        
        self.x = None
        self.original_x_shape = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.original_x_shape = x.shape
        x = x.reshape(x.shape[0], -1)
        self.x = x

        out = np.dot(self.x, self.W) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        
        dx = dx.reshape(*self.original_x_shape)
        return dx

mul_layer = MulLayer()
ans_mul_layer = AnsMulLayer()

relu_layer = Relu()
ans_relu_layer = AnsRelu()

hidden_size = 2
w1 = 0.01 * np.random.randn(2, hidden_size)
b1 = np.zeros(hidden_size)
affine_layer = Affine(w1, b1)
ans_affine_layer = AnsAffine(w1, b1)

##########   inital message   ##############
print("*****************************")
print("")
print("This chpater is lerning backword.")
print("")
print("Let's define the MulLayer forward functioin..")
print("")
print("MulLayer class is defined as follow.")
print(disp_mullayer)
print("")
print("So you define these answers as follow")
print("MulLayer.forward(x, y) = foo")
print("")
print("And check defined answers as follow.")
print("checkMLForward()")

def checkMLForward():
    chk_x = 2
    chk_y = 3
    correct_ans = ans_mul_layer.forward(chk_x, chk_y)
    chk_ans = mul_layer.forward(chk_x, chk_y)
    if correct_ans==chk_ans:
        print("")
        print("Goood!!!!")
        print("")
        print("Next step is backward.")
        print("Let's define backward function like forward function.")
        print("")
        print("And check defined answers as follow.")
        print("checkMLBackward()")
    else:
        print("")
        print("Ooops, your answer is incorrect.")
        print("")
        print("If you want a hint type this->")
        print("hint_ml_forward")
        print("")
        print("And check defined answers as follow.")
        print("checkMLForward()")

def checkMLBackward():
    dout = 1
    correct_ans = ans_mul_layer.backward(dout)
    chk_ans = mul_layer.backward(dout)
    if correct_ans == chk_ans:
        print("")
        print("OK!!!")
        print("Mul layer is defined.")
        print("")
        print("Next is ReLU layer.")
        print("Let's define the ReLU forward functioin.")
        print("")
        print("ReLU layer is defined as 'Relu'.")
        print("So, you define the relu forward function as follow.")
        print("Relu.forward = foo")
        print("")
        print("And check your answer as follow.")
        print("checkReLUForward()")
    else:
        print("")
        print("Result is incorrect.....")
        print("")
        print("If you want a hint type this->")
        print("hint_ml_backward")
        print("")
        print("And check defined answers as follow.")
        print("checkMLBackward()")

def checkReLUForward():
    chk_array = np.array([[1, 2], [3, 4]])
    ans_chk = ans_relu_layer.forward(chk_array)
    chk = relu_layer.forward(chk_array)
    if (ans_chk==chk).all():
        print("")
        print("Yeah!!! thas's good!")
        print("Next is  ReLU backward.")
        print("")
        print("Let's define the backward function of Relu.")
        print("")
        print("And check your answe as follow.")
        print("checkReLUBackward()")
    else:
        print("Sorry! Your asnwer incorrect...")
        print("")
        print("If you want hint type this")
        print("hint_relu_forward")
        print("")
        print("And check defined answers as follow.")
        print("checkReLUForward()")

def checkReLUBackward():
    chk_array = np.array([[1, 2], [3, 4]])
    ans_chk = ans_relu_layer.backward(chk_array)
    chk = relu_layer.backward(chk_array)
    if (ans_chk==chk).all():
        print("")
        print("Good!!")
        print("Your answe is correct.")
        print("")
        print("Next is Affine layer.")
        print("Affine is defined as this -> Affine.")
        print("Let's define the affine forward function as follow.")
        print("Affine.forward = foo")
        print("")
        print("And check your answe as follow.")
        print("checkAffineForward()")
    else:
        print("")
        print("Mmmm, your answe is incorrect.")
        print("")
        print("If you want a hint type this.")
        print("hint_relu_backward")
        print("")
        print("And check your answe as follow.")
        print("checkReLUBackward()")

def checkAffineForward():
    chk_array = np.array([[1, 2], [3, 4]])
    chk_ans = affine_layer.forward(chk_array)
    chk_correct_ans = ans_affine_layer.forward(chk_array)
    if (chk_ans==chk_correct_ans).all():
        print("Gooood!!")
        print("Next is Affine backward.")
        print("")
        print("So, define the backward function of affine layer")
        print("And check your answe as follow.")
        print("checkAffineBackward()")
    else:
        print("Ooops your answer is incorrect.")
        print("If you want a hint type this -> ")
        print("hint_affine_forward")
        print("")
        print("And check your answe as follow.")
        print("checkAffineForward()")

def checrAffineBackward(skip=False):
    chk_num = 6
    chk_ans = affine_layer.backward(chk_num)
    chk_correct_ans = ans_affine_layer.backward(chk_num)
    if (chk_ans==chk_correct_ans).all or skip:
        print("")
        print("Very good!!!")
        print("Next is two layer net.")
        nextChapter()
        
    else:
        print("Mmm... your answer is incorrect.")
        print("If you want a hint type this -> ")
        print("hint_affine_backward")
        print("")
        print("And check your answe as follow.")
        print("checkReLUBackward()")


def nextChapter(file_name="ch05_2.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

