import numpy

check_a = numpy.array([1, 2])
check_b = numpy.array([[1, 2, 3], [4, 5, 6]])
check_c = numpy.dot(check_a, check_b)

print("hello.")
print("let's type-> hello()")

def hello(name=""):
    if name == "":
        print("Hello someone!!")
        print("So next step is type this-> hello(\"your name\")")
    else:
        print("Hello " + name + " !!")
        print("OK. Next step")
        print("Type this->")
        print("import numpy as np")

def checkArray(a, b):
    reslt_a = all(a == check_a)
    reslt_b = (b == check_b).all
    if (reslt_a and reslt_b):
        print("")
        print("Nice!")
        print("Variables is collect.")
        print("")
        print("So let's calc array.")
        print("")
        print("type this ")
        print("b")
    else:
        print("Ooops somethin went wrong")
        print("Check this->")
        print("a = np.array([1, 2])")
        print("b = np.array([[1, 2, 3], [4, 5, 6]])")



def nextChapter():
    with open("ch02.py") as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

