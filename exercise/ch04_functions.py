import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

hint_ms_error = ""
hint_ce_error = """Cross entropy error is as follow

def entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

And check your define function as follow.
checkCeError()

"""

hint_random_data = """Get random data is as follow.

batch_size = 10
train_size = x_train.shape[0]
batch_mask = np.random.choice(train_size, batch_size)
random_x = x_train[batch_mask]
random_t = t_train[batch_mask]

And check the answers as follow.
checkRandomData(random_x, random_t)

"""

chk_y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
chk_t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

train_size = x_train.shape[0]
batch_size = 10

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def collect_mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

def collect_cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

print("*****************************")
print("")
print("This chpater is lerning gradient.")
print("First of all lean loss function.")
print("Famours loss function is mean squared error.")
print("")
print("So let's define mean squared error function.")
print("Like this ->")
print("def mean_squared_error(y, t):")
print(".....")
print("")
print("And check your define function as follow.")
print("checkMsError()")
print("")

def checkMsError():
    ans = mean_squared_error(chk_y, chk_t)
    collect_ans = collect_mean_squared_error(chk_y, chk_t)
    if ans==collect_ans:
        print("")
        print("OK!!")
        print("Next is cross entropy error.")
        print("")
        print("Define a coross entropy error as follow.")
        print("")
        print("def cross_entropy_error(y, t):")
        print(".....")
        print("")
        print("And check your define function as follow.")
        print("checkCeError()")
        print("")
    else:
        print("")
        print("Mmm, function is not collect.")
        print("")
        print("If you nedd a hint type as follow.")
        print("hint_ms_error")
        print("")
        print("")

def checkCeError():
    ans = cross_entropy_error(chk_y, chk_t)
    collect_ans = collect_cross_entropy_error(chk_y, chk_t)
    if ans==collect_ans:
        print("")
        print("That's good!")
        print("")
        print("Next step is calcuration of many data.")
        print("That use mini batch.")
        print("")
        print("Mini batch will retrieve data randomly from all data.")
        print("So, let's get traindata randomly as follow.")
        print("")
        print("random_x: this is a traindata")
        print("random_t: this is a labeldata")
        print("")
        print("You can use data as follow.")
        print("x_train: this is a traindata")
        print("t_train: this is a labeldata")
        print("")
        print("And check the answers as follow.")
        print("checkRandomData(random_x, random_t)")
        print("")
    else:
        print("")
        print("Mmm, function is not collect.")
        print("")
        print("If you nedd a hint type as follow.")
        print("hint_ce_error")
        print("")

def checkRandomData(x, t):
    chk_batch_x = batch_size == x.shape[0]
    chk_batch_t = batch_size == t.shape[0]
    if chk_batch_x and chk_batch_t:
        print("")
        print("Okay!!!!")
        print("")
        print("Next is lerning differential.")
        print("")
        nextChapter()
    else:
        print("")
        print("ooops, data is not collect.")
        print("")
        print("If you want a hint type this->")
        print("hint_random_data")
        print("")
        print("And check the answers as follow.")
        print("checkRandomData(random_x, random_t)")
        print("")

def nextChapter(file_name="ch04_2.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

