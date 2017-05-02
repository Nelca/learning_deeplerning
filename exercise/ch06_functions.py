import numpy as np

view_momentum = """
class Momentum:

    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None
        
    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():                                
                self.v[key] = np.zeros_like(val)
                
        for key in params.keys():
            
            question_2
            self.v[key] = 'question_1'
            params[key] += 'question_2'
"""

hint_momentum = """
momentum answers is as follow.

question_1 = 'self.momentum * self.v[key] - self.lr * grads[key] '
question_2 = 'self.v[key]'

and check your answer as follow.
checkMomentum()
"""

view_nesterov = """
class Nesterov:

    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = 'question_1'
        self.v = None
        
    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = 'question_2'
            
        for key in params.keys():
            self.v[key] *= self.momentum
            self.v[key] -= self.lr * grads[key]
            params[key] += 'question_3'
            params[key] -= 'question_4'
"""

hint_nesterov = """
nesterov answer is as follow.

question_1 = 'momentum'
question_2 = 'np.zeros_like(val)'
question_3 = 'self.momentum * self.momentum * self.v[key]'
question_4 = '(1 + self.momentum) * self.lr * grads[key]'

And check your answer as follow.
checkNesterov()
"""
view_adagrad = """
class AdaGrad:

    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None
        
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = question_1
            
        for key in params.keys():
            self.h[key] += question_2
            params[key] -= question_3
"""

ans_momentum_1 = 'self.momentum * self.v[key] - self.lr * grads[key] '
ans_momentum_2 = 'self.v[key]'

ans_nesterov_1 = 'momentum'
ans_nesterov_2 = 'np.zeros_like(val)'
ans_nesterov_3 = 'self.momentum * self.momentum * self.v[key]'
ans_nesterov_4 = '(1 + self.momentum) * self.lr * grads[key]'

ans_adagrad_1 = 'np.zeros_like(val)'
ans_adagrad_2 = 'grads[key] * grads[key]'
ans_adagrad_3 = 'self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)'

##########   inital message   ##############
print("*****************************")
print("")
print("This chpater is lerning technique of neural netwok.")
print("Lerning set is")
print("")
print("1.update parameters")
print("2.weight initialize")
print("3.batch normalization")
print("4.regularization")
print("5.verification of hyper parameters")
print("")
print("So, first step is update parameters.")
print("first technique is 'Momentum'")
print("Momentum is as follow")
print("")
print(view_momentum)
print("")
print("Plese fill in 'question_*'")
print("And check your answer as follow.")
print("checkMomentum()")

#############################################

##########   answer check functions   ##############

def checkMomentum(skip=False):
       
    chk_1 = ans_momentum_1.replace(" ", "")==question_1.replace(" ", "")
    chk_2 = ans_momentum_2.replace(" ", "")==question_2.replace(" ", "")
    if chk_1 and chk_2:
        print("Very good!!!")
        print("Next is Nesterov.")
        print("")
        print(view_nesterov)
        print("")
        print("Let's fill in the answer.")
        print("And check your answer as follow.")
        print("checkNesterov()")
    else:
        print("Mmm... your answer is incorrect.")
        print("If you want a hint type this -> ")
        print("hint_momentum")
        print("")
        print("And check your answe as follow.")
        print("checkMomentum()")


def checkNesterov():
    chk_1 = ans_nesterov_1.replace(" ", "")==question_1.replace(" ", "")
    chk_2 = ans_nesterov_2.replace(" ", "")==question_2.replace(" ", "")
    chk_3 = ans_nesterov_3.replace(" ", "")==question_3.replace(" ", "")
    chk_4 = ans_nesterov_4.replace(" ", "")==question_4.replace(" ", "")
    if chk_1 and chk_2 and chk_3 and chk_4:
        print("Greate !!!!!")
        print("Next is AdaGrad.")
        print("AdaGrad is as follow.")
        print("")
        print(view_adagrad)
        print("")
        print("Let's fill in the answer.")
        print("And check your answer as follow.")
        print("checkAdaGrad()")
    else :
        print("Mmmm.. your answer is incorrect.")
        print("check the hint as follow.")
        print("")
        print("hint_nesterov")
        print("")
        print("Anc check your answer as follow.")
        print("checkNesterov()")

def checkAdaGrad():
    chk_1 = ans_adagrad_1.replace(" ", "")==question_1.replace(" ", "")
    chk_2 = ans_adagrad_2.replace(" ", "")==question_2.replace(" ", "")
    chk_3 = ans_adagrad_3.replace(" ", "")==question_3.replace(" ", "")
    if chk_1 and chk_2 and chk_3 :
        print("That's greate !!")
        print("")
        print("")
    else :
        print("Sorry, your answer is not correct.")
        print("")
        print("")


def nextChapter(file_name="ch07.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

