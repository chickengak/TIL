def solution(s):
    res = ""
    check = True
    for c in s:
        if c == " ":
            res += c
            check = True
        elif check:
            res += c.upper()
            check = False
        else:
            res += c.lower()
    return res