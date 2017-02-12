import numpy as np
import sys
import subprocess

def get_lines(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout= subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        line = proc.stdout.readline()
        if line:
            yield line
        if not line and proc.poll() is not None:
            break


if __name__ == '__main__':
    for line in get_lines(cmd='pwd'):
        print(line)
        #sys.stdout.write(line)
        sys.stdout.write('stdout write test')


print("")
print("")
print("")
print("Hello. This section is lerning activation function.")
print("")
print("First of all, let's  define a test function.")
print("Be careful whith indentation.")
print("type this ")
print("")
print("def testFunction() :")
print("    print (\"Greate!\")")
print("")
print("You can now define the function.")

def sigmoid(x):
    return 1 / (1 + np.exp(-x))    



