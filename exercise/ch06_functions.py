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
view_adam = """
class Adam:

    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.iter = 0
        self.m = None
        self.v = None
        
    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key, val in params.items():
                self.m[key] = question_1 
                self.v[key] = question_2
        
        self.iter += 1
        lr_t  = self.lr * np.sqrt(1.0 - self.beta2**self.iter) / (1.0 - self.beta1**self.iter)         
        
        for key in params.keys():
            self.m[key] += (1 - self.beta1) * (grads[key] - self.m[key])
            self.v[key] += (1 - self.beta2) * (grads[key]**2 - self.v[key])
            
            params[key] -= lr_t * self.m[key] / (np.sqrt(self.v[key]) + 1e-7)
"""
hint_adam = """
adam answer is as follow.
question_1 = np.zeros_like(val)
question_2 = np.zeros_like(val)

And check your asnwer as follow.
checkAdam()
"""

view_weight_init_activation = """
for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i-1]

    w = question_1
    a = np.dot(x, w)
    z = question_2

    # z = ReLU(a)
    # z = tanh(a)

    activations[i] = z
"""
hint_wiah = """
weight init activation histogram answer is as follow.

question_1 = np.random.randn(node_num, node_num) * 1
question_2 = sigmoid(a)

And check your answer as follow.
checkWiah()
"""

view_batch_norm = """
grad_backprop = network.gradient(x_batch, t_batch)
grad_numerical = network.numerical_gradient(x_batch, t_batch)

for key in grad_numerical.keys():
    diff = question_1
    print(key + ":" + str(diff))
"""

hint_batch_norm = """
batch normarization answer is as follow.

question_1 = np.average( np.abs(grad_backprop[key] - grad_numerical[key]) )

So, check your answer as follow.
checkBatchNorm()
"""
view_dropout = """
self.layers['Dropout' + str(idx)] = Dropout(dropout_ration)
"""

hint_dropout = """
drop out answer is as follow.

question_1 = "self.layers['Dropout' + str(idx)] = Dropout(dropout_ration)"

So, check your answer as follow.
checkDropOut()
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

val = np.array([[1, 2], [3, 4]])
ans_adam_1 = np.zeros_like(val)
ans_adam_2 = np.zeros_like(val)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


node_num = 123
a = 10
ans_wia_1 = np.random.randn(node_num, node_num) * 1
ans_wia_2 = sigmoid(a)


grad_backprop = np.array([1, 2, 3])
grad_numerical = np.array([1, 2, 3])
key = 1
ans_batch_narom = np.average( np.abs(grad_backprop[key] - grad_numerical[key]) )

ans_dropout = "self.layers['Dropout' + str(idx)] = Dropout(dropout_ration)"

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
        print("Next is adam.")
        print("Andam is adagrad + momentum.")
        print("")
        print(view_adam)
        print("")
        print("Let's fill in the answer.")
        print("And check your answer as follow.")
        print("checkAdam()")
    else :
        print("Sorry, your answer is not correct.")
        print("Check the answer as follow.")
        print("")
        print("hint_ada_grad")
        print("")
        print("And check your answer as follow.")
        print("checkAdaGrad()")

def checkAdam():
    chk_1 = (ans_adam_1==question_1).all
    chk_2 = (ans_adam_2==question_2).all
    if chk_1 and chk_2:
        print("That's greate!!")
        print("Next is weight init activation histograrm.")
        print("")
        print(view_weight_init_activation)
        print("")
        print("Let's fill in the answer.")
        print("And check your answer as follow.")
        print("checkWiah()")
    else:
        print("Ooops!!")
        print("Your answer is incorrect.")
        print("")
        print("So, check the hint as follow.")
        print("hint_adam")
        print("")
        print("And check your answer as follow.")
        print("checkAdam()")

def checkWiah():
    chk_1 = ans_wia_1==questioin_1
    chk_2 = ans_wia_2==questioin_2
    if chk_1 and chk_2:
        print("OK!!!!!")
        print("Next is batch normalization.")
        print("")
        print(view_batch_norm)
        print("")
        print("Let's fill in the answer.")
        print("And check your answer as follow.")
        print("checkBtachNorm()")
    else:
        print("Mmmmm.... your answer is incorrect.")
        print("Check the hint as follow.")
        print("")
        print("hint_wiah")
        print("")
        print("And check your answer as follow.")
        print("checkWiah()")

def checkBtachNorm():
    if ans_batch_narom==questioin_1:
        print("Okay!!")
        print("Next is dorop out.")
        print("Drop out is the training network technique.")
        print("dropout calclatioin is as follow.")
        print("")
        print(view_dropout)
        print("")
        print("So, fill in your answer and check as follow.")
        print("checkDropOut()")
    else:
        print("Ummmm.. your answer is incorrect.")
        print("Check the hint as follow.")
        print("")
        print("hint_batch_norm")
        print("")
        print("And check your answer as follow.")
        print("checkBtachNorm()")


def checkDropOut():
    chk_1 = ans_dropout == question_1
    if chk_1:
        print("That's good!!")
        print("Let's move next chapter.")
        print("")
        nextChapter()
    else :
        print("Sorry... your answer is incorrect.")
        print("Check the hint type this.")
        print("")
        print("hint_dropout")
        print("")
        print("And check your answer as follow")
        print("checkDropOut()")



def nextChapter(file_name="ch07.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

