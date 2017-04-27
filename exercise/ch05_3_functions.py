import sys, os
sys.path.append(os.pardir)

import numpy as np
from dataset.mnist import load_mnist
from ch05_tl_net import TwoLayerNet


(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

### answers ###

ans_network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)
ans_iter_per_epoch = max(train_size / batch_size, 1)
ans_batch_mask = np.random.choice(train_size, batch_size)

x_batch = x_train[ans_batch_mask]
t_batch = t_train[ans_batch_mask]
ans_grad = ans_network.gradient(x_batch, t_batch)

ans_loss = ans_network.loss(x_batch, t_batch)

##################


### hints ###
hint_network = """
The network answer is as follow.

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

And check your answer as follow.
checkNet()
"""
hint_epoch = """
Epoch answer is as follow.

epoch = max(train_size / batch_size, 1)

So, check the answer as follow.
checkEpoch()
"""
hint_batch_mask = """
Batch aswer is as follow.

batch_mask = np.random.choice(train_size, batch_size)

So, check the answer as follow.
checkBatchMask()
"""

hint_grad = """
gradient answer is as follow.

grad = network.gradient(x_batch, t_batch)

And check your answer as follow.
checkGrad()
"""
hint_loss = """
loss answer is as follow.

loss = network.loss(x_batch, t_batch)

So, check your answer as follow.
checkLoss()
"""
##################

##########   inital message   ##############
print("*****************************")
print("")
print("This chpater is train neural net.")
print("Let's define the training .")
print("")
print("First of all, define the network as 'network'.")
print("Network initial argument are as follow.")
print("input_size=784, hidden_size=50, output_size=10")
print("")
print("And check your network as follow.")
print("checkNet()")

def checkNet():
    chk_1 = type(ans_network)==type(network)
    if chk_1:
        print("Goood!!!!")
        print("")
        print("Next step is calculate epoch.")
        print("Training size and batch size are defined as follows.")
        print("")
        print("train_size = x_train.shape[0]")
        print("batch_size = 100")
        print("")
        print("Let's define the epoch as 'epoch'")
        print("")
        print("And check your answer as follow.")
        print("checkEpoch()")
    else:
        print("Ooops, your answer is incorrect.")
        print("")
        print("If you want a hint type this->")
        print("hint_network")
        print("")
        print("And check defined answers as follow.")
        print("checkNet()")

def checkEpoch():
    chk_1 = ans_iter_per_epoch==epoch
    if chk_1:
        print("Tha's right!!!!")
        print("Next step is define batch mask.")
        print("You define batch mask as 'batch_mask'.")
        print("")
        print("And check your answer as follow.")
        print("checkBatchMask()")
    else :
        print("Sorry... your answer incorrect.")
        print("check the hint as follow.")
        print("")
        print("hint_epoch")
        print("")
        print("And check defined answers as follow.")
        print("checkEpoch()")

def checkBatchMask():
    chk_1 = (ans_batch_mask==batch_mask).all
    if chk_1:
        print("That's good!!!!!!")
        print("Next is calculate gradient.")
        print("")
        print("So, you define the gradient as 'gradient'")
        print("And check your answer as follow.")
        print("checkGrad()")
    else:
        print("Mmmm. your answer is incorrect.")
        print("Check the hint as follow.")
        print("")
        print("hint_batch_mask")
        print("And check your answer as follow")
        print("checkBatchMask()")

def checkGrad():
    #TODO : check true false.
    chk_1 = ans_grad==grad
    if chk_1:
        print("Goood!!!")
        print("Next is calculate loss.")
        print("So, you define the loss as 'loss'.")
        print("")
        print("And check the answer as follow.")
        print("checkLoss()")
    else :
        print("Sorry.... your answer is incorrect.")
        print("Check the answer as follow.")
        print("")
        print("hint_grad")
        print("")
        print("And check your answer as follow.")
        print("checkGrad()")

def checkLoss():
    chk_1 = ans_loss==loss
    if chk_1:
        print("Tha's right!!!!")
        print("Okay, now check the flow of predict.")
        print("The flow as follow.")
        print("")
        print(train_nn_all)
        print("")
        print("Tha's all.")
        print("So, next is lerning tips of training nural network.")
        print("")
        nextChapter()
    else:
        print("Mmmm. your answer in correct.")
        print("Check the hint as follow.")
        print("")
        print("hint_loss")
        print("")
        print("And check your answer as follow.")
        print("checkLoss()")


def nextChapter(file_name="ch06.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

