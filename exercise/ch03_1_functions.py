import numpy as np

def printInitialMessage():
    print("")
    print("*******************************")
    print("")
    print("This section lerning about computing multidimentional arrays.")
    print("")
    print("First step is define numpy array as follows.")
    print("")
    print("a = np.array([1, 2, 3, 4])")
    print("")

def nextChapter(file_name="ch03_2.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)


printInitialMessage()

