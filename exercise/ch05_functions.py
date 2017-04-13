import sys, os
sys.path.append(os.pardir)
from layer_naive import *

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



mul_layer = MulLayer()
ans_mul_layer = AnsMulLayer()

relu_layer = Relu()
ans_relu_layer = AnsRelu()

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
    chk_num = 1
    ans_chk = ans_relu_layer.forward(chk_num)
    chk = relu_layer.forward(chk_num)
    if ans_chk==chk:
        print("")
        print("OK")
        print("")
    else:
        print("")
        print("Your asnwer incorrect")
        print("")


def nextChapter(file_name="ch06.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

