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
checkMLForword()

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

print("*****************************")
print("")
print("This chpater is lerning backword.")
print("")
print("Let's define the MulLayer fforward functioin..")
print("")
print("MulLayer class is defined as follow.")
print(disp_mullayer)
print("")
print("So you define these answers as follow")
print("MulLayer.forword(x, y) = foo")
print("")
print("And check defined answers as follow.")
print("checkMLForword()")

def checkMLForword():
    collect_ans = MulLayer.forword()
    ans = MulLayer.forword()


def nextChapter(file_name="ch06.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

