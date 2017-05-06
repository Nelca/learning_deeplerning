import numpy as np

##########   questions and hints   ##############
view_im2col = """
def im2col(input_data, filter_h, filter_w, stride=1, pad=0):
    N, C, H, W = question_1
    out_h = (H + 2*pad - filter_h)//stride + 1
    out_w = (W + 2*pad - filter_w)//stride + 1

    img = question_2
    col = question_3

    for y in range(filter_h):
        y_max = question_4
        for x in range(filter_w):
            x_max = x + stride*out_w
            col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]

    col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N*out_h*out_w, -1)
    return col
"""

hint_im2col = """
im2col answers is as follow.

question_1 = input_data.shape
question_2 = np.pad(input_data, [(0,0), (0,0), (pad, pad), (pad, pad)], 'constant')
question_3 = np.zeros((N, C, filter_h, filter_w, out_h, out_w))
question_4 = y + stride*out_h

So, define these answers and check as follow.
checkIm2col()
"""
#############################################

##########   inital message   ##############
print("*****************************")
print("")
print("This chpater is Convolutional neural network(CNN).")
print("Lerning set is")
print("")
print("1.define im2col function.")
print("2.define convolution layer")
print("3.define pooling layer")
print("4.implementation of CNN")
print("")
print("So, first step is im2col.")
print("Let's fill in your answer im2col as follow.")
print("")
print(view_im2col)
print("")
print("And check your answer as follow.")
print("checkIm2col()")
#############################################


##########   answers   ##############

input_data = np.random.rand(10, 1, 28, 28)
pad = 1
N = 10
C = 1
filter_h = 5
filter_w = 5
out_h = 28
out_w = 28
stride = 1
y = 3
ans_im2col_1 = input_data.shape
ans_im2col_2 = np.pad(input_data, [(0,0), (0,0), (pad, pad), (pad, pad)], 'constant')
ans_im2col_3 = np.zeros((N, C, filter_h, filter_w, out_h, out_w))
ans_im2col_4 = y + stride*out_h


#############################################


##########   answer check functions   ##############

def checkIm2col(skip=False):
    chk_1 = ans_im2col_1==question_1
    chk_2 = (ans_im2col_2==question_2).all
    chk_3 = (ans_im2col_3==question_3).all
    chk_4 = ans_im2col_4==question_4
    if  (chk_1 and chk_2 and chk_3 and chk_4) or skip:
        print("Very good!!!")
        print("")
    else:
        print("Mmm... your answer is incorrect.")
        print("")

#############################################


##########   nest chapter function   ##############
def nextChapter(file_name="ch08.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

#############################################

