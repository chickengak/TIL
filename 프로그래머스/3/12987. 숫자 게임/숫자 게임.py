def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    idx = 0
    for b in B:
        try:
            while A[idx] >= b:
                idx += 1
            answer +=1
            idx +=1
        except IndexError:
            break
            
    return answer