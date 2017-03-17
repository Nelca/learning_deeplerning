import numpy as np

w = np.array([[1, 2], [3, 4]])

def collect_identity_function(x):
    return x

def collect_softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 

    x = x - np.max(x) # オーバーフロー対策
    return np.exp(x) / np.sum(np.exp(x))

def printInitialMessage():
    print("")
    print("*******************************")
    print("")
    print("This section lerning about computing multidimentional arrays.")
    print("")
    print("First step is define numpy array as follows.")
    print("")
    print("a = np.array([1, 2])")
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

def checkSoftmax():
    chk_val = np.array([-1, 0, 1.3])
    result = softmax(chk_val)
    collect_result = collect_softmax(chk_val)
    if all(result == collect_result):
        print("")
        print("Goooodd!!")
        print("So, check the softmax results.")
        print("type tihs->")
        print("softmax(N2)")
        print("")
    else:
        print("")
        print("Mmmmm define function is not collect.")
        print("Check the function name as 'softmax'")
        print("If you want hint, type this -> hint_softmax")
        print("")

def nextChapter(file_name="ch03_2.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)


printInitialMessage()

