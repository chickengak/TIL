def solution(string):
    s = ""
    for i in string:
        if i in "aeiou":
            continue
        else:
            s += i
    return s
