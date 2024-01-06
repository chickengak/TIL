"""
https://school.programmers.co.kr/learn/courses/30/lessons/17687
"""


# My answer
def solution(n, t, m, p):
    answer = '0'
    dic = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    start = 1
    while len(answer) < t*m:
        temp = ''
        share = start
        while True:
            share, remainder = divmod(share, n)
            temp += dic[remainder]
            if share == 0:
                break
        answer += temp[::-1]
        start +=1
    return answer[p-1::m][:t]
# ㅋㅋㅋ 나중에 내가 코드 리뷰하다가 리뷰가 막혀서 넣음. 코드는 잘 만듬.
