import numpy as np

hint_ms_error = ""

chk_y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
chk_t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x 

def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y
 
def collect_mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

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

def nextChapter(file_name="ch05.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)


