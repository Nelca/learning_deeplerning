import customconsole as cc


class CustomConsole(cc.CustomConsole):
    def check_input(self, ri):
        replaced_ri = ri.replace(" ", "")
        if replaced_ri == "a=np.array([1,2])":
            print("")
            print("Good!!")
            print("")
            print("Then let's display the values of variable 'a'.")
            print("Type this->")
            print("print(a)")
            print("")
        elif replaced_ri == "print(a)":
            self.runsource(ri)
            ri = ""
            print("")
            print("Nice!")
            print("The results are as described above.")
            print("")
            print("Next is check dimention of 'a'")
            print("Type this -> ")
            print("np.ndim(a)")
            print("")
        elif replaced_ri == "np.ndim(a)":
            self.runsource(ri)
            ri = ""
            print("")
            print("That's it!")
            print("The results are as described above.")
            print("")
            print("Next let's display the number of elements of the array.")
            print("Type this ->")
            print("a.shape")
            print("")
        elif replaced_ri == "a.shape":
            self.runsource(ri)
            ri = ""
            print("")
            print("OK!")
            print("This is a sigle dimention array results.")
            print("")
            print("Well, next we define a multidimensional array.")
            print("Type this->")
            print("b = np.array([[1, 2], [3, 4]])")
            print("")
        elif replaced_ri == "b=np.array([[1,2],[3,4]])":
            self.runsource(ri)
            ri = ""
            print("")
            print("Okay!")
            print("So let's check variable 'b'.")
            print("")
            print("Type this->")
            print("print(b)")
            print("np.ndmin(b)")
            print("b.shape")
            print("")
        elif replaced_ri == "b.shape":
            self.runsource(ri)
            ri = ""
            print("")
            print("Gooood!!!")
            print("Next exercise will do the dot product of matrix.")
            print("")
            print("Define the new array as follow.")
            print("c = np.array([[1, 2, 3], [4, 5, 6]])")
            print("")
        elif replaced_ri == "c=np.array([[1,2,3],[4,5,6]])":
            self.runsource(ri)
            ri = ""
            print("")
            print("OK, tht's it.")
            print("Next is dot calcuration.")
            print("")
            print("Type this ->")
            print("np.dot(b, c)")
            print("")
        elif replaced_ri == "np.dot(b,c)":
            self.runsource(ri)
            ri = ""
            print("")
            print("Nice!!!")
            print("This is a dot product of matrix.")
            print("")
            print("Next is check nueral network calculation.")
            print("First of all, redifine 'b' like as follow.")
            print("b = np.array([[1, 2, 3])")
            print("")
            print("Neural network is expressed by the following expression.")
            print("")
            print("A = XW + B")
            print("'X' is first neuron")
            print("'W' is weight")
            print("'B' is biass")
            print("'A' is output")
            print("")
            print("So define NN is this->")
            print("N1 = np.dot(a, c) + b")
            print("")
            print("Above function is ")
            print("'a' is first neuron")
            print("'c' is weight")
            print("'b' is biass")
            print("")
        elif replaced_ri == "N1=np.dot(a,c)+b":
            self.runsource(ri)
            ri = ""
            print("")
            print("That's it.")
            print("Next is output data to activation function.")
            print("")
            print("Activation functions is sigmoid, ReLU.")
            print("now use a sigmoid function.")
            print("")
            print("y = sigmoid(N1)")
            print("")
            print("")
        elif ri == "hint":
            print("")
        return ri

ch03_1_console = CustomConsole(question_file= "./ch03_1_functions.py")
ch03_1_console.interact("### welcome chapter 3-1 !!! ###")

