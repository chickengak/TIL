def solution(lottos, win_nums):
    answer = []
    match = 0
    zeros = 0
    for lotto in lottos:
        if lotto == 0:
            zeros +=1
        elif lotto in win_nums:
            match +=1
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    return [dic[match+zeros], dic[match]]