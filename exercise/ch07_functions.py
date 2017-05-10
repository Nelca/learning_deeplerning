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

hint_conv_forward = """
Convolution forward function is as follow.

def forward(self, x):
    FN, C, FH, FW = self.W.shape
    N, C, H, W = x.shape
    out_h = 1 + int((H + 2*self.pad - FH) / self.stride)
    out_w = 1 + int((W + 2*self.pad - FW) / self.stride)

    col = im2col(x, FH, FW, self.stride, self.pad)
    col_W = self.W.reshape(FN, -1).T

    out = np.dot(col, col_W) + self.b
    out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

    self.x = x
    self.col = col
    self.col_W = col_W

    return out

So, define the function and check your answer as follow.

Convolution.forward = forward

checkConvForward()
"""
hint_conv_backward = """
convolution backward is as follow.

def backward(self, dout):
    FN, C, FH, FW = self.W.shape
    dout = dout.transpose(0,2,3,1).reshape(-1, FN)

    self.db = np.sum(dout, axis=0)
    self.dW = np.dot(self.col.T, dout)
    self.dW = self.dW.transpose(1, 0).reshape(FN, C, FH, FW)

    dcol = np.dot(dout, self.col_W.T)
    dx = col2im(dcol, self.x.shape, FH, FW, self.stride, self.pad)

    return dx

Define the answer as follow.
Convolution.backward = yourAnswerFunction

And check the answer as follow.
checkConvBackward()
"""

hint_pooling_forward = """
pooling forward is as follow.

def forward(self, x):
    N, C, H, W = x.shape
    out_h = int(1 + (H - self.pool_h) / self.stride)
    out_w = int(1 + (W - self.pool_w) / self.stride)

    col = im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
    col = col.reshape(-1, self.pool_h*self.pool_w)

    arg_max = np.argmax(col, axis=1)
    out = np.max(col, axis=1)
    out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

    self.x = x
    self.arg_max = arg_max

    return out

So, define the function and subsutitute as follow.
Pooling.forward = forward

And check your answer as follow.
checkPoolingForward()
"""

hint_pooling_backward = """
pooling backward is as follow.

def backward(self, dout):
    dout = dout.transpose(0, 2, 3, 1)
    
    pool_size = self.pool_h * self.pool_w
    dmax = np.zeros((dout.size, pool_size))
    dmax[np.arange(self.arg_max.size), self.arg_max.flatten()] = dout.flatten()
    dmax = dmax.reshape(dout.shape + (pool_size,)) 
    
    dcol = dmax.reshape(dmax.shape[0] * dmax.shape[1] * dmax.shape[2], -1)
    dx = col2im(dcol, self.x.shape, self.pool_h, self.pool_w, self.stride, self.pad)
    
    return dx

So, define the function and subsutitute as follow.
Pooling.backward = backward

And check your answer as follow.
checkPoolingBackward()
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


class AnsConvolution:
    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad
        
        # 中間データ（backward時に使用）
        self.x = None   
        self.col = None
        self.col_W = None
        
        # 重み・バイアスパラメータの勾配
        self.dW = None
        self.db = None

    def forward(self, x):
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape
        out_h = 1 + int((H + 2*self.pad - FH) / self.stride)
        out_w = 1 + int((W + 2*self.pad - FW) / self.stride)

        col = im2col(x, FH, FW, self.stride, self.pad)
        col_W = self.W.reshape(FN, -1).T

        out = np.dot(col, col_W) + self.b
        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        self.x = x
        self.col = col
        self.col_W = col_W

        return out

    def backward(self, dout):
        FN, C, FH, FW = self.W.shape
        dout = dout.transpose(0,2,3,1).reshape(-1, FN)

        self.db = np.sum(dout, axis=0)
        self.dW = np.dot(self.col.T, dout)
        self.dW = self.dW.transpose(1, 0).reshape(FN, C, FH, FW)

        dcol = np.dot(dout, self.col_W.T)
        dx = col2im(dcol, self.x.shape, FH, FW, self.stride, self.pad)

        return dx


class Convolution:
    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad
        
        # 中間データ（backward時に使用）
        self.x = None   
        self.col = None
        self.col_W = None
        
        # 重み・バイアスパラメータの勾配
        self.dW = None
        self.db = None

class AnsPooling:
    def __init__(self, pool_h, pool_w, stride=1, pad=0):
        self.pool_h = pool_h
        self.pool_w = pool_w
        self.stride = stride
        self.pad = pad
        
        self.x = None
        self.arg_max = None

    def forward(self, x):
        N, C, H, W = x.shape
        out_h = int(1 + (H - self.pool_h) / self.stride)
        out_w = int(1 + (W - self.pool_w) / self.stride)

        col = im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
        col = col.reshape(-1, self.pool_h*self.pool_w)

        arg_max = np.argmax(col, axis=1)
        out = np.max(col, axis=1)
        out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

        self.x = x
        self.arg_max = arg_max

        return out

    def backward(self, dout):
        dout = dout.transpose(0, 2, 3, 1)
        
        pool_size = self.pool_h * self.pool_w
        dmax = np.zeros((dout.size, pool_size))
        dmax[np.arange(self.arg_max.size), self.arg_max.flatten()] = dout.flatten()
        dmax = dmax.reshape(dout.shape + (pool_size,)) 
        
        dcol = dmax.reshape(dmax.shape[0] * dmax.shape[1] * dmax.shape[2], -1)
        dx = col2im(dcol, self.x.shape, self.pool_h, self.pool_w, self.stride, self.pad)
        
        return dx

class Pooling:
    def __init__(self, pool_h, pool_w, stride=1, pad=0):
        self.pool_h = pool_h
        self.pool_w = pool_w
        self.stride = stride
        self.pad = pad
        
        self.x = None
        self.arg_max = None


#############################################


##########   answer check functions   ##############

def checkIm2col(skip=False):
    chk_1 = ans_im2col_1==question_1
    chk_2 = (ans_im2col_2==question_2).all
    chk_3 = (ans_im2col_3==question_3).all
    chk_4 = ans_im2col_4==question_4
    if  (chk_1 and chk_2 and chk_3 and chk_4) or skip:
        print("Very good!!!")
        print("Next is convolution(Conv) layer.")
        print("First of conv layer is define forward function.")
        print("So, let's define forward as follos.")
        print("")
        print("Convolution.forward = yourAnswerFunction")
        print("")
        print("And check your answer as follow.")
        print("checkConvForward()")
    else:
        print("Mmm... your answer is incorrect.")
        print("Check the hint as follow.")
        print("")
        print("hint_im2col")
        print("")
        print("And check your answer as follow.")
        print("checkIm2col()")

def checkConvForward(skip=False):
    chk_1 = (Convolution.forward(input_data)==AnsConvolution.forward(input_data)).all
    if chk_1 or skip :
        print("Greate!!!!")
        print("Your answer is correct!!!")
        print("")
        print("Next step is define convolution backward.")
        print("")
        print("Convolution.backward = yourAnswerFunction")
        print("")
        print("And check your answer as follow.")
        print("checkConvBackward()")
    else:
        print("Oops, your answer seems to be wrong.")
        print("If you need hint, type this.")
        print("")
        print("hint_conv_forward")
        print("")
        print("And check your answer as follow.")
        print("checkConvForward()")


def checkConvBackward(skip=False):
    dout = 10
    chk_1 = (Convolution.backward(dout)==AnsConvolution.backward(dout)).all
    if chk_1 or skip :
        print("Greate!!!!")
        print("Your answer is correct!!!")
        print("")
        print("Next step is define the pooling forward.")
        print("Like as follow.")
        print("")
        print("Pooling.forward = yourDefinedFunction")
        print("")
        print("And check your answer as follow.")
        print("checkPoolingForward()")
    else:
        print("Oops, your answer seems to be wrong.")
        print("If you need hint, type this.")
        print("")
        print("hint_conv_backward")
        print("")
        print("And check your answer as follow.")
        print("checkConvBackward()")

def checkPoolingForward():
    chk_1 = (Pooling.forward(input_data)==AnsPooling.forward(input_data).all
    if chk_1:
        print("Cool!!")
        print("Next is pooling backward.")
        print("")
        print("Pooling.backward = yourDefinedFunction")
        print("")
        print("And check your answer as follow.")
        print("checkPoolingBackward()")
    else:
        print("Mmmm.. your answer is incorrect.")
        print("Check the hint as follow")
        print("")
        print("hint_pooling_forward")
        print("")
        print("And check your answer as follow.")
        print("checkPoolingForward()")

def checkPoolingBackward(skip=False):
    dout = 10
    chk_1 = (Pooling.backward(dout)==AnsPooling.backward(dout)).all
    if chk_1 or skip :
        print("Greate!!!!")
        print("Your answer is correct!!!")
        print("")
        print("Next step is implementation of CNN.")
        print("")
        nextChapter()
    else:
        print("Oops, your answer seems to be wrong.")
        print("If you need hint, type this.")
        print("")
        print("hint_pooling_backward")
        print("")
        print("And check your answer as follow.")
        print("checkPoolingBackward()")


#############################################


##########   nest chapter function   ##############
def nextChapter(file_name="ch07_2.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

#############################################

