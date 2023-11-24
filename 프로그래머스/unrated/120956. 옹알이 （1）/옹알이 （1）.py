def solution(babbling):
    bab = ("aya", "ye", "ma", "woo")
    cnt = 0
    for b in babbling:
        for i in bab:
            b = b.replace(i, "-")
        b = b.replace("-", "")
        if not b:
            cnt += 1
    return cnt