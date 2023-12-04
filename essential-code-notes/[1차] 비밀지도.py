"""
2018 KAKAO BLIND RECRUITMENT
https://school.programmers.co.kr/learn/courses/30/lessons/17681
"""


# My answer
def solution1(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = bin(arr1[i]|arr2[i])[2:].zfill(n)
        answer.append(temp.replace("1", "#").replace("0", " "))
    return answer
#0.021 sec. Nice use of bit operator |. And also .zfill(). And also .replace().replace()


# Other's answer
def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
# 0.025 sec. Nice use of rjust.


def line(n, x):
    return ''.join(' #'[int(i)] for i in f'{x:016b}'[-n:])

def solution3(n, *maps):
    return [line(n, a | b) for a, b in zip(*maps)]
# 0.093 sec. Interesting use.

