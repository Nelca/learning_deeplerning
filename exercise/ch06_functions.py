

def checrAffineBackward(skip=False):
    chk_num = 6
    chk_ans = affine_layer.backward(chk_num)
    chk_correct_ans = ans_affine_layer.backward(chk_num)
    if (chk_ans==chk_correct_ans).all or skip:
        print("")
        print("Very good!!!")
        print("Next is two layer net.")
        nextChapter()
        
    else:
        print("Mmm... your answer is incorrect.")
        print("If you want a hint type this -> ")
        print("hint_affine_backward")
        print("")
        print("And check your answe as follow.")
        print("checkReLUBackward()")


def nextChapter(file_name="ch07.py"):
    with open(file_name) as next_chapter:
        next_code = next_chapter.read()
        exec(next_code)

