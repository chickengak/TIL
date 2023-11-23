def solution(A, B):
    leng = len(A)
    for i in range(leng):
        if (A[leng - i:] + A[0:leng - i]) == B:
            return i
    return -1
