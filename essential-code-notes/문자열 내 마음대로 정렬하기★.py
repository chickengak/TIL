"""
https://school.programmers.co.kr/learn/courses/30/lessons/12915
"""


# My answer
def solution1(strings, n):
    # return sorted(strings, key=lambda x: (x[n], x[a] for a in range(len(x))))
    new_strs = []
    for i, v in enumerate(strings):
        new_strs.append([i, v[n] + v[:n] + v[n + 1:]])
    new_strs.sort(key=lambda x: x[1])

    return [strings[i[0]] for i in new_strs]
# 0.031sec.


# Others' answer
def solution2(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
# 0.014sec.


def solution3(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])
# 0.015sec.


import time

start = time.time()
for i in range(10000):
    solution1(["sun", "bed", "car"],1)
    solution1(["abce", "abcd", "cdx"],2)
end = time.time()

print(f"{end - start} sec")
