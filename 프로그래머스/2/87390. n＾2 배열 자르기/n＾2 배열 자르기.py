def solution(n, left, right):
    share, remainder = divmod(left, n)  # share행 remainder열이 left 위치.
    target_share, target_remainder = divmod(right, n)
    #print(share, remainder,"\t", target_share, target_remainder)
    answer = []

    while share != target_share:
        if share >= remainder:
            answer += [share + 1] * (share - remainder + 1)
        answer += list(range(max(share + 2, remainder + 1), n + 1))
        share += 1
        remainder = 0

    #if target_share >= target_remainder:
    if answer:
        answer += [share + 1] * min(share+1,target_remainder+1)
    else:
        #remainder = 0
        answer += [share + 1] * (share - 0 + 1)
        answer += list(range(max(share + 2, 0 + 1), n + 1))
        answer = answer[remainder:target_remainder+1]
        return answer
    if target_share <= target_remainder:
        answer += list(range(remainder +1 if share ==0 and target_share==0 else max(share + 2, remainder + 1), target_remainder + 2))
    return answer