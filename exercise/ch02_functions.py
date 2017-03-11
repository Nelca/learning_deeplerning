import numpy as np

hint_and_gate = ''
hint_nand_gate = ''
hint_or_gate = ''
hint_xor_gate = ''

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

def printInitialMessage():
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
    print("and check the function this -> checkAndGate()")
    print("")

def checkAndGate():
    chk_result = getGateResults(AND)
    colletct_result = getGateResults(collect_AND)
    if chk_result == colletct_result:
        print("")
        print("OK!!")
        print("")
        print("And gate is define as above.")
        print("")
        viewGateResults(AND)
        print("")
        print("Next is Nand gate.")
        print("So deifne the 'NAND' function.")
        print("")
        print("hint is type this -> hint_nand_gate")
        print("")
        print("and check the function this -> checkNandGate()")
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


def checkNandGate():
    chk_result = getGateResults(NAND)
    colletct_result = getGateResults(collect_NAND)
    if chk_result == colletct_result:
        print("")
        print("OK!!")
        print("")
        print("Nand gate is define as above.")
        print("")
        viewGateResults(NAND)
        print("")
        print("Next is OR gate.")
        print("So deifne the 'OR' function.")
        print("")
        print("hint is type this -> hint_or_gate")
        print("")
        print("and check the function this -> checkOrGate()")
        print("")
    else:
        print("")
        print("NG...")
        print("hint is type this -> hint_nand_gate")
        print("")
        print("See results of your define function.")
        viewGateResults(NAND)
        print("")
        print("And collect result is this->")
        print("")
        viewGateResults(collect_NAND)
        print("")
        print("")

def checkOrGate():
    chk_result = getGateResults(OR)
    colletct_result = getGateResults(collect_OR)
    if chk_result == colletct_result:
        print("")
        print("Good!!")
        print("")
        print("OR gate is define as above.")
        print("")
        viewGateResults(OR)
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
        print("and check the function this -> checkXorGate()")
        print("")
        print("")
    else:
        print("")
        print("Oooops result is not collect.")
        print("hint is type this -> hint_xor_gate")
        print("")
        print("See results of your define function.")
        viewGateResults(OR)
        print("")
        print("And collect result is this->")
        print("")
        viewGateResults(collect_OR)
        print("")
         print("")

def checkXorGate():
    chk_result = getGateResults(XOR)
    colletct_result = getGateResults(collect_XOR)
    if chk_result == colletct_result:
        print("")
        print("Nice!!")
        print("")
        print("XOR gate is define as above.")
        print("")
        viewGateResults(XOR)
        print("")
        print("Let's move next chapter--3.")
        print("")
        nextChapter()
        print("")
    else:
        print("")
        print("NG....")
        print("")
        print("See results of your define function.")
        viewGateResults(XOR)
        print("")
        print("And collect result is this->")
        print("")
        viewGateResults(collect_XOR)
        print("")
        print("")

def getGateResults(gate_function):
    results = {}
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = gate_function(xs[0], xs[1])
        results[str(xs)] = y
    return results

def viewGateResults(gate_function):
    results = getGateResults(gate_function)
    for k, v in results.items():
        print(k + " -> " + str(v))

def nextChapter():
    with open("ch03.py") as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

printInitialMessage()

