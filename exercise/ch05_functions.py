import sys, os
sys.path.append(os.pardir)
from layer_naive import *

disp_mullayer = """

class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
"""

hint_ml_forword = """
forword function is as follow.

def forward(self, x, y):
        self.x = x
        self.y = y                
        out = x * y

So, you define the function as below.
And check the answer as follow.
checkMLForward()

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


mul_layer = MulLayer()
ans_mul_layer = AnsMulLayer()

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
        print("Let's define backward function like forward.")
        print("")
        print("And check defined answers as follow.")
        print("checkMLBackward()")
    else:
        print("")
        print("Ooops, your answer is incorrect.")
        print("")
        print("If you want a hint type this->")
        print("hint_ml_forword")
        print("")
        print("And check defined answers as follow.")
        print("checkMLForward()")


def nextChapter(file_name="ch06.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

