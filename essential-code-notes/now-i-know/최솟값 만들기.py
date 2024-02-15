"""

https://school.programmers.co.kr/learn/courses/30/lessons/12941
"""

# My answer
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    return sum([A[i]*B[i] for i in range(len(A))])
# .sort() method, indexing, list comprehension. The fastest code.
