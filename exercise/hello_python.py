import numpy

print("hello python")
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
        print("and type this->checkNumpy() ")

def checkNumpy():
    try:
        if np :
            print("Good !! Now numpy is avaiabble.")
            print("So let's do next step is")
            print("type this-> a = np.array([1, 2])")
            print("and type this-> b = np.array([[1, 2, 3], [4, 5, 6]])")
            print("and type this->checkArray(a, b) ")
    except NameError:
        print("Ooops numpy is not imported.")
        print("Re type this-> import numpy as np")
        print("and type this->checkNumpy() ")

def checkArray(a, b):
    check_a = np.array([1, 2])
    check_b = np.array([[1, 2, 3], [4, 5, 6]])
    if (all(a == check_a) and all(b == check_b)):
        print("Nice!")
        print("So, next step is-> c = np.dot(a, b)")
        print("and -> checkResult(c)")
    else:
        print("Ooops somethin went wrong")
        print("Check this-> a = np.array([1, 2])")
        print("and check this-> b = np.array([[1, 2, 3], [4, 5, 6]])")
        print("Or do this-> print(a)")
        print("at last retype checkArray(a, b)")

def checkResult(c):
    if (all(c == check_c)):
        print("Yeah!! that's great.")
    else :
        print("Mmmmm something went wrong")
        print("The result is")
        print(c)
        print("So, check and modify.")
        print("and -> checkResult(c)")

#code.InteractiveConsole(globals()).interact()
