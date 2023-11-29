def solution(n):
    remain_l = []
    share = n
    while share:
        share, remainder = divmod(share, 3)
        remain_l.append(remainder)
    return sum([ v * (3**i) for i, v in enumerate(remain_l[::-1])])