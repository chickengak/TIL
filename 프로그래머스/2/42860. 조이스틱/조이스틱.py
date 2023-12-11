import re
def solution(name):
    if (set(name) == {"A",}):
        return 0
    p = re.compile('[' + "A" + ']+').finditer(name)
    left_right_step = len(name)-1
    for i in p:
        x = (len(name)-i.end())*2-1+i.start()  # 역주행 후 정주행.
        y = (0 if i.start()-1<0 else i.start()-1)*2 + (len(name)-i.end()) # 정주행 후 역주행.
        left_right_step = min(x,y,left_right_step)
    up_down_step = 0
    for c in name:  #65~90
        if ord(c) < 79:
            up_down_step += ord(c)-65
        else:
            up_down_step += abs(ord(c)-91)

    return left_right_step+ up_down_step