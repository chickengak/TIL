def cnt7(n):
    share, remainder = divmod(n, 10)
    if share > 0:
        return 1 + cnt7(share) if remainder == 7 else cnt7(share)
    else:
        return 1 if remainder == 7 else 0

def solution(array):
    return sum(cnt7(i) for i in array)