import numpy

print("hello.")
print("let's type-> hello()")

check_a = numpy.array([1, 2])
check_b = numpy.array([[1, 2, 3], [4, 5, 6]])
check_c = numpy.dot(check_a, check_b)

def hello(name=""):
    if name == "":
        print("Hello someone!!")
        print("So next step is type this-> hello(\"your name\")")
    else:
        print("Hello " + name + " !!")
        print("OK. Next step")
        print("Type this-> import numpy as np")

def checkNumpy():
    try:
        if np :
            print("Good !! Now numpy is avaiabble.")
            print("So let's do next step.")
            print("Type is ->")
            print("a = np.array([1, 2])")
            print("b = np.array([[1, 2, 3], [4, 5, 6]])")
            print("checkArray(a, b) ")
    except NameError:
        print("Ooops numpy is not imported.")
        print("Re type this-> import numpy as np")
        print("and type this->checkNumpy() ")

def checkArray(a, b):
    reslt_a = all(a == check_a)
    reslt_b = (b == check_b).all
    if (reslt_a and reslt_b):
        print("Nice!")
        print("")
        print("So, let's confrim numpy.")
        print("")
        print("Type this -> print(a)")
        print("")
        print("So, next step is-> c = np.dot(a, b)")
        print("and -> checkResult(c)")
    else:
        print("Ooops somethin went wrong")
        print("Check this-> a = np.array([1, 2])")
        print("and check this-> b = np.array([[1, 2, 3], [4, 5, 6]])")
        print("Or do this-> print(a)")

def checkResult(c):
    if (all(c == check_c)):
        print("Yeah!! that's great.")
        print("This exercise is end. next is ch03.py")
        with open("ch03_functions.py") as ch03_f:
            ch03_code = ch03_f.read()
            exec(ch03_code)
    else :
        print("Mmmmm something went wrong")
        print("The result is")
        print(c)
        print("So, check and modify.")
        print("and -> checkResult(c)")


