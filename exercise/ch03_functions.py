import numpy as np

hint_sigmoid = ""
hint_step_func = ""
hint_ReLU = ""

print("**************************")
print("")
print("Hello. This section is lerning neural netowok.")
print("First of all, lerning a activation function.")
print("")
print("Let's define 'sigmoid' function.")
print("If you want hint, type this ->")
print("hint_sigmoid")
print("")
print("and type this->checkSigmoid()")

def collect_sigmoid(x):
    return 1 / (1 + np.exp(-x))

def collect_step_function(x):
    return np.array(x > 0, dtype=np.int)

def collect_ReLU(x):
    return np.maximum(0, x)

def checkSigmoid():
    chk_num = np.array([-1.0, 0.5, 2.1])
    result = sigmoid(chk_num)
    collect_result = collect_sigmoid(chk_num)
    if all(result == collect_result):
        print("")
        print("OK!!!")
        print("Sigmoid is collect.")
        print("")
        print("Next activatioin function is 'step function'.")
        print("Define the 'step_function', and type checkStepFunction()")
        print("If you want hint, type this -> hint_step_func")
    else:
        print("")
        print("Mmmmm define function is not collect.")
        print("Check the function name as 'sigmoid'")
        print("If you want hint, type this -> hint_sigmoid")

def checkStepFunction():
    chk_num = np.array([-0.5, 0, 1.0])
    result = step_function(chk_num)
    collect_result = collect_step_function(chk_num)
    if all(result == collect_result):
        print("")
        print("Nice!!")
        print("Step function is define collect.")
        print("")
        print("Next activatioin function is Rectified Liner Unit as ReLU.")
        print("Define the 'ReLU', and type checkReLU()")
        print("If you want hint, type this -> hint_ReLU")
    else:
        print("")
        print("Mmmmm define function is not collect.")
        print("Check the function name as 'step_function'")
        print("If you want hint, type this -> hint_step_func")

def checkReLU():
    chk_num = np.array([-0.5, 0, 1.0, 1.4])
    result = ReLU(chk_num)
    collect_result = collect_ReLU(chk_num)
    if all(result == collect_result):
        print("")
        print("That's greate!!!")
        print("ReLU function is collect.")
        print("")
        print("So next step is lerning about computing multidimentional arrays.")
        nextChapter()
    else:
        print("")
        print("Mmmmm define function is not collect.")
        print("Check the function name as 'ReLU'")
        print("If you want hint, type this -> hint_ReLU")


def nextChapter(file_name="ch03_1.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)


