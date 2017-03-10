import numpy as np

check_a = np.array([1, 2])
check_b = np.array([[1, 2, 3], [4, 5, 6]])
check_c = np.dot(check_a, check_b)

hint_and_gate = ''
hint_nand_gate = ''
hint_or_gate = ''
hint_xor_gate = ''

print("")
print("*************************************")
print("")
print("This chapter lern about perceptron.")
print("")
print("Basic perceptron petern is and gate.")
print("")
print("Let's define the And gate perceptron as 'AND' function.")
print("")
print("")
print("")
print("hint is type this -> hint_and_gate")
print("")
print("and check the function this -> checkAndGate(1, 2)")
print("")

def collect_AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def collect_NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def collect_OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def collect_XOR(x1, x2):
    s1 = collect_NAND(x1, x2)
    s2 = collect_OR(x1, x2)
    y = collect_AND(s1, s2)
    return y

def checkAndGate(x1, x2):
    chk_result = AND(x1, x2)
    colletct_result = collect_AND(x1, x2)
    result = (chk_result == colletct_result).all
    if result:
        print("")
        print("OK!!")
        print("")
        print("And gate is define.")
        print("")
        print("Next is Nand gate.")
        print("So deifne the 'NAND' function.")
        print("")
        print("hint is type this -> hint_nand_gate")
        print("")
        print("and check the function this -> checkNandGate(1, 2)")
        print("")
    else:
        print("")
        print("Mmmm result is not much.")
        print("")
        print("See results of your define function.")
        viewGateResults(AND)
        print("")
        print("And collect result is this->")
        print("")
        viewGateResults(collect_AND)
        print("")
        print("")
        print("hint is type this -> hint_nand_gate")
        print("")


def checkNandGate(x1, x2):
    chk_result = NAND(x1, x2)
    colletct_result = collect_NAND(x1, x2)
    result = all(chk_result == colletct_result)
    if result:
        print("")
        print("OK!!")
        print("")
        print("Nand gate is define.")
        print("")
        print("Next is OR gate.")
        print("So deifne the 'OR' function.")
        print("")
        print("hint is type this -> hint_or_gate")
        print("")
        print("and check the function this -> checkOrGate(1, 2)")
        print("")
    else:
        print("")
        print("NG")
        print("hint is type this -> hint_nand_gate")
        print("")

def checkOrGate(x1, x2):
    chk_result = OR(x1, x2)
    colletct_result = collect_OR(x1, x2)
    result = all(chk_result == colletct_result)
    if result:
        print("")
        print("Good!!")
        print("")
        print("Next is XOR gate.")
        print("XOR gate needs multi layer perceptron.")
        print("")
        print("Let's define the 'XOR' gate.")
        print("")
        print("XOR gate is combination of ")
        print("")
        print("hint is type this -> hint_xor_gate")
        print("")
        print("and check the function this -> checkXorGate(1, 2)")
        print("")
        print("")
        print("")
        print("")
    else:
        print("")
        print("Oooops result is not collect.")
        print("hint is type this -> hint_xor_gate")
        print("")

def checkXorGate(x1, x2):
    chk_result = XOR(x1, x2)
    colletct_result = collect_XOR(x1, x2)
    result = all(chk_result == colletct_result)
    if result:
        print("")
        print("Nice!!")
        print("")
        print("")
        print("Let's move next chapter--3.")
        print("")
        print("")
    else:
        print("")
        print("NG....")
        print("")

def viewGateResults(gate_function):
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = gate_function(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))

def nextChapter():
    with open("ch03.py") as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)


