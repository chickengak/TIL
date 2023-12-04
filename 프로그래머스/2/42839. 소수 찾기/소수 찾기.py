from itertools import permutations

def solution(numbers):
    n_list = list(numbers)
    cases = set()
    for i in range(1, len(numbers) + 1):
        for permu in list(permutations(n_list, i)):
            temp = ""
            for p in permu:
                temp += p
            cases.add(int(temp))
    cnt = 0
    for case in cases:
        if case == 0 or case==1:
            continue
        for i in range(2, int(case**0.5)+1):
            if case%i == 0:
                break
        else:
            cnt +=1
    return cnt