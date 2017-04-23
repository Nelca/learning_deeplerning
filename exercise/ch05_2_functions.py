import sys, os
sys.path.append(os.pardir)
from layer_naive import *
import numpy as np
from collections import OrderedDict

two_layer_init = """
def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01):
    self.params = {}
    self.params['W1'] = question_1
    self.params['b1'] = question_2
    self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size) 
    self.params['b2'] = np.zeros(output_size)

    self.layers = OrderedDict()
    self.layers['Affine1'] = question_3(self.params['W1'], self.params['b1'])()
    self.layers['Relu1'] = Relu()
    self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])

    self.lastLayer = SoftmaxWithLoss()
 
"""
hint_tl_init = """
two layer init answer is as follow.

question_1 = weight_init_std * np.random.randn(input_size, hidden_size)
question_2 = np.zeros(hidden_size)
question_3 = Affine

Check your answer as follow.
checkTLInit()
"""

two_layer_predict = """
def predict(self, x):
    for layer in self.layers.values():
        x = 'question_1'
    
    return x
"""
hint_tl_predict = """
predict answe is as follow.

question_1 = 'layer.forward(x)'

And check your answe as follow
checkTLPredict
"""

two_layer_loss = """
def loss(self, x, t):
    y = self.'question_1'(x)
    return self.'question_2'.forward(y, t)
"""

hint_tl_loss = """
The answers is as follow.

question_1 = "predict"
question_2 = "lastLayer"

And check your answe as follow.
checkTLLoss()
"""

two_layer_accuracy = """
    def accuracy(self, x, t):
        y = self.predict(x)
        y = question_1
        if t.ndim != 1 : t = np.argmax(t, axis=1)
        
        accuracy = question_2
        return accuracy
"""
hint_tl_accuracy = """
two layer net's accuracy function answer is as follow.

question_1 = np.argmax(y, axis=1)
question_2 = np.sum(y == t) / float(x.shape[0])

So, check your answer as follow.
checkTLAccuracy()
"""
two_layer_ng = """
def numerical_gradient(self, x, t):
    loss_W = lambda W: self.loss(x, t)
    
    grads = {}
    grads['W1'] = question_1(loss_W, self.params['W1'])
    grads['b1'] = question_1(loss_W, self.params['b1'])
    grads['W2'] = question_1(loss_W, self.params['W2'])
    grads['b2'] = question_1(loss_W, self.params['b2'])
    
    return grads
"""

# tow layer net
weight_init_std = 0.01
input_size = 65
hidden_size = 65


class Affine:
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


ans_1 = weight_init_std * np.random.randn(input_size, hidden_size)
ans_2 = np.zeros(hidden_size)
ans_3 = Affine

ans_tl_predict_1 = "layer.forward(x)"

ans_tl_loss_1 = "predict"
ans_tl_loss_2 = "lastLayer"

y = np.arra([[1, 2], [3, 4]])
t = np.arra([[1, 2], [3, 4]])
x = np.array([1, 2, 3])
ans_tl_accuracy_1 = np.argmax(y, axis=1)
ans_tl_accuracy_2 = np.sum(y == t) / float(x.shape[0])



print("*****************************")
print("")
print("Let's learning two layer net of backpropagation.")
print("")
print("And check defined answers as follow.")
print("checkMLForward()")


def checkTLInit():
    chk_ans_1 = len(ans_1) == len(question_1)
    chk_ans_2 = (ans_2 == question_2).all
    chk_ans_3 = ans_3 == question_3
    if chk_ans_1 and chk_ans_2 and chk_ans_3:
        print("")
        print("That's right!!!")
        print("Next is predict")
        print("")
        print(two_layer_predict)
        print("")
        print("You fill in these 'questioin' as string, and check your answer as follow.")
        print("checkTLPredict()")
    else:
        print("Sorry.. your answe incorrect.")
        print("check the hint as follow")
        print("hint_tl_init")
        print("")
        print("And check your answer asa follow.")
        print("checkTLInit()")

def checkTLPredict():
    chk_1 = ans_tl_predict_1==question_1
    if chk_1:
        print("")
        print("Goooood!!!")
        print("Next step is loss function.")
        print("")
        print(two_layer_loss)
        print("")
        print("")
        print("Let's define loss function and check your answer as follow.")
        print("checkTLLoss()")
    else:
        print("Mmm... your answer incorrect.")
        print("")
        print("check the hint as follow")
        print("hint_tl_init")
        print("")
        print("And check your answer as follow.")
        print("checkTLPredict()")

def checkTLLoss():
    chk1 = questioin_1 == ans_tl_loss_1
    chk2 = questioin_2 == ans_tl_loss_2
    if chk1 and chk2:
        print("That's good!")
        print("Next is accuracy.")
        print("")
        print(two_layer_accuracy)
        print("")
        print("Let's put your answer in 'questioni_*' ")
        print("And check your answer as below.")
        print("checkTLAccuracy()")
    else:
        print("Mmmmm... your answer is incorrect.")
        print("Check the hint as below.")
        print("")
        print("hint_tl_loss")
        print("")
        print("And check your answer as below.")
        print("checkTLLoss()")

def checkTLAccuracy():
    chk1_ = ans_tl_accuracy_1==question_1
    chk2_ = ans_tl_accuracy_2==question_2
    if chk_1 and chk_2:
        print("")
        print("Gooood!!!")
        print("Next is numerical gradient.")
        print("Numerical gradient is as follow.")
        print("")
        print(two_layer_ng)
        print("")
        print("Let's put your answer in 'questioni_*' ")
        print("And check your answer as below.")
        print("checkTLNG()")
    else:
        print("Sorry... your answer is incorrect.")
        print("Let's check the hint as 'hint_tl_accuracy'")
        print("")
        print("And check your answer as follow.")
        print("checkTLAccuracy()")

def checkTLNG():
    if True:
        print("")
        print("")
        print("")
        print("")
    else :
        print("")
        print("")
        print("")

def nextChapter(file_name="ch05_3.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

