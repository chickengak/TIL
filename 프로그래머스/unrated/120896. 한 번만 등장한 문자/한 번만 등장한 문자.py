def solution(s):
    return "".join(sorted(i for i in set(s) if s.count(i) == 1))