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

ans_network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

hint_network = """
The network answer is as follow.

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

And check your answer as follow.
checkNet()
"""

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
    chk_1 = ans_network==network
    if chk_1:
        print("Goood!!!!")
        print("")
        print("Next step is calculate epoch.")
        print("Training size and batch size are defined as follows.")
        print("")
        print("train_size = x_train.shape[0]")
        print("batch_size = 100")
        print("")
        print("Let's define the epoch as 'iter_per_epoch'")
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

def nextChapter(file_name="ch06.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

