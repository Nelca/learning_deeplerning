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
        print("Type this-> import numpy as np")





