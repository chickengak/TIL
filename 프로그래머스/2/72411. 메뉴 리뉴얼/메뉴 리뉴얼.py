from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    for num in course:
        counter = defaultdict(lambda: 0)
        for order in orders:
            if len(order) >= num:
                for comb in list(combinations(order, num)):
                    counter["".join(sorted(comb))] += 1
        res = []
        maximum = 2
        for k, v in counter.items():
            if v > maximum:
                maximum = v
                res = [k]
            elif v == maximum:
                res.append(k)
        answer += res

    return sorted(answer)