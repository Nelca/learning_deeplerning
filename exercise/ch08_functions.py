import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from deep_convnet import DeepConvNet
from dataset.mnist import load_mnist
from common.layers import *



##########   questions and hints   ##############
view_predict = """
def predict(self, x, train_flg=False):
    for layer in self.layers:
        if question_1:
            x = question_2
        else:
            x = question_3
    return x
"""

hint_predict = """
predict answers is as follow.

question_1 = isinstance(layer, Dropout)
question_2 = layer.forward(x, train_flg)
question_3 = layer.forward(x)



And check your answer as follow.
checkDCNPredict()
"""

view_gradient = """
def gradient(self, x, t):
    # forward
    question_1

    # backward
    dout = 1
    dout = question_2

    tmp_layers = self.layers.copy()
    question_3
    for layer in tmp_layers:
        dout = question_4

    # configulation
    grads = {}
    for i, layer_idx in enumerate((0, 2, 5, 7, 10, 12, 15, 18)):
        grads['W' + str(i+1)] = question_5
        grads['b' + str(i+1)] = question_6

    return grads
"""

hint_gradient = """
gradient answers is as follow.

question_1 = 'self.loss(x, t)'
question_2 = 'self.last_layer.backward(dout)'
question_3 = 'tmp_layers.reverse()'
question_4 = 'layer.backward(dout)'
question_5 = 'self.layers[layer_idx].dW'
question_6 = 'self.layers[layer_idx].db'

So, define the answer and check as follow.
checkDCNGradient()
"""
hint_dcn = """
Deep conv net initialize answer is as follow.

network = DeepConvNet()
network.load_params("deep_convnet_params.pkl")

and check your answer as follow.
checkDCN()
"""
view_loop = """
acc = 0.0
batch_size = 100

for i in range(int(x_test.shape[0] / batch_size)):
    tx = x_test[i*batch_size:(i+1)*batch_size]
    tt = t_test[i*batch_size:(i+1)*batch_size]
    y = question_1
    y = np.argmax(y, axis=1)
    classified_ids.append(y)
    acc += question_2
    
acc = question_3
"""
hint_dcn_loop = """
loop answer is as follow.

question_1 = network.predict(tx, train_flg=False)
question_2 = np.sum(y == tt)
question_3 = acc / x_test.shape[0]

So, define the answer and check as follow.
checkDCNLoop()
"""



#############################################

##########   inital message   ##############
print("*****************************")
print("")
print("Last chpater is Lerning Deep lerning.")
print("Let's define Deep Convolutional Network.")
print("Network is as follow.")
print("")
print("conv - relu - conv- relu - pool -")
print("conv - relu - conv- relu - pool -")
print("conv - relu - conv- relu - pool -")
print("affine - relu - dropout - affine - dropout - softmax")
print("")
print("init function is so complecated, so define predict function.")
print("")
print(view_predict)
print("")
print("And check your answer as follow.")
print("checkDCNPredict")
#############################################


##########   answers   ##############

network = DeepConvNet()
layer = network.layers[0]
x = np.random.randn(2, 3, 4, 5)
train_flg = False

ans_predict_1 = isinstance(layer, Dropout)

if isinstance(layer, Dropout):
    ans_predict_2 = layer.forward(x, train_flg)
else:
    ans_predict_2 = layer.forward(x)

ans_predict_3 = layer.forward(x)

ans_grad_1 = 'self.loss(x, t)'
ans_grad_2 = 'self.last_layer.backward(dout)'
ans_grad_3 = 'tmp_layers.reverse()'
ans_grad_4 = 'layer.backward(dout)'
ans_grad_5 = 'self.layers[layer_idx].dW'
ans_grad_6 = 'self.layers[layer_idx].db'


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=False)
classified_ids = []
acc = 0.0
batch_size = 100

network.load_params("deep_convnet_params.pkl")
tx = x_test[0*batch_size:(0+1)*batch_size]
tt = t_test[0*batch_size:(0+1)*batch_size]
y = network.predict(tx, train_flg=False)
y = np.argmax(y, axis=1)
classified_ids.append(y)
acc += np.sum(y == tt)
 
ans_loop_1 = network.predict(tx, train_flg=False)
ans_loop_2 = np.sum(y == tt)
ans_loop_3 = acc / x_test.shape[0]


#############################################


##########   answer check functions   ##############

def checkDCNPredict():
    chk_1 = ans_predict_1==question_1
    chk_2 = ans_predict_2==question_2
    chk_3 = ans_predict_3==question_3
    if chk_1 and chk_2 and chk_3 :
        print("Goood!!!")
        print("Loss, accuracy functions is skipped.")
        print("So next is gradient")
        print("")
        print(view_gradient)
        print("")
        print("Fill in your answer and check as follow.")
        print("checkDCNGradient()")
    else:
        print("Mmmmm... your answer is incorrect.")
        print("Check the hint as follow.")
        print("")
        print("hint_predict")
        print("")
        print("And check your answer as follow.")
        print("checkDCNPredict()")


def checkDCNGradient():
    chk_1 = ans_grad_1==question_1
    chk_2 = ans_grad_2==question_2
    chk_3 = ans_grad_3==question_3
    chk_4 = ans_grad_4==question_4
    chk_5 = ans_grad_5==question_5
    chk_6 = ans_grad_6==question_6
    if chk_1 and chk_2 and chk_3 and chk_4 and chk_5 and chk_6 :
        print("That's greate!!!!!")
        print("Next is use the Deep Convolutional Network")
        print("")
        print("First of all define as 'network'")
        print("and load deep_convnet_params.pkl_params.")
        print("")
        print("So, check your answer as follow,")
        print("checkDCN()")
    else:
        print("Ooops,  your answer is incorrect.")
        print("Check the hint as follow.")
        print("")
        print("hint_gradient")
        print("")
        print("And check your answer as follow.")
        print("checkDCNGradient()")


def checkDCN():
    chk_1 = True
    if chk_1:
        print("That's Greaate!!!!")
        print("Next is predict.")
        print("Predict is on loop as follow.")
        print("")
        print(view_loop)
        print("")
        print("So, define the for loop and define acc.")
        print("If you want a hint type this.")
        print("")
        print("hint_dcn_loop")
        print("")
        print("And check your answer as follow.")
        print("checkDCNLoop()")
    else:
        print("Mmmmmm,,,, your answer is incorrect")
        print("Check the hint as follow.")
        print("")
        print("hint_dcn")
        print("")
        print("And check your answer as follow.")
        print("checkDCN()")

def checkDCNLoop():
    chk_1 = ans_loop_1==question_1
    chk_2 = ans_loop_2==question_2
    chk_3 = ans_loop_3==question_3
    if chk_1 and chk_2 and chk_3:
        print("Goood!!")
        print("Now calculated the accuracy.")
        print("So, check the accuracy.")
    else:
        print("Mmmmmm... your answer is incorrect.")
        print("If you want a hint type this.")
        print("")
        print("hint_dcn_loop")
        print("")
        print("And check your answer as follow.")
        print("checkDCNLoop()")
 

#############################################


##########   nest chapter function   ##############
def nextChapter(file_name=""):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

#############################################

