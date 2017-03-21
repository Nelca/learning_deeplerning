import sys, os
sys.path.append(os.pardir)
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax

collect_ans_predict = np.array(['np.dot(z1,W2)+b2', 'sigmoid(a2)', 'softmax(a3)'])

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1_dot = np.dot(x, W1)
    a1 = a1_dot + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

def getAccurary(x, t, network):
    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p= np.argmax(y)
        if p == t[i]:
            accuracy_cnt += 1

    accuracy = float(accuracy_cnt) / len(x)
    return accuracy

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
    print("but it's a too long.")
    print("so use 'get_data' function as follow.")
    print("")
    print("x, t = get_data()")
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

def checkPredictFillin(ans, skip=False):
    ans = ans.replace(" ", "")
    if all(ans==collect_ans_predict) or skip:
        print("")
        print("Tha's greate!!!")
        print("Predict function was defined.")
        print("")
        print("Let's acutually use this function.")
        print("First of all define neural net.")
        print("Here was simplify it as follows")
        print("")
        print("Type this->")
        print("network = init_nework()")
        print("")
    else:
        print("")
        print("Ooops")
        print("yout answer is not collect.")
        print("If you want hint, type this -> hint_predict")
        print("")
        print("Or, type this->")
        print("checkPredictFillin(ans, skip=true)")
        print("")

def nextChapter(file_name="ch04.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)


printInitialMessage()
