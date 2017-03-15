import numpy as np

w = np.array([[1, 2], [3, 4]])

def collect_identity_function(x):
    return x

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

def nextChapter(file_name="ch03_2.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)


printInitialMessage()

