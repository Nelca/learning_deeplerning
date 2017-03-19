import sys, os
sys.path.append(os.pardir)
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax
import pdb

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def collect_identity_function(x):
    return x

def printInitialMessage():
    print("")
    print("*******************************")
    print("")
    print("This section lerning about MNIST discirimination.")
    print("So define neural net of mnist step by step.")
    print("")
    print("First of all ,download mnist data")
    print("Get data is as follow.")
    print("(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)")
    print("")
    print("but it's a very borad.")
    print("so use get_data function()")
    print("")
    print("x, t = get_data()")
    print("")
    print("")
    print("")
    print("")


def checkIdf():
    chk_val = np.array([-1, 0, 1.3])
    result = identity_function(chk_val)
    collect_result = collect_identity_function(chk_val)
    if all(result == collect_result):
        print("")
        print("OK!!")
        print("So next is use the identity function.")
        print("")
        print("Type this->")
        print("Y = identity_function(N2)")
        print("")
    else:
        print("")
        print("Mmmmm define function is not collect.")
        print("Check the function name as 'identity_function'")
        print("If you want hint, type this -> hint_idf")
        print("")

def nextChapter(file_name="ch04.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)


printInitialMessage()

