#from itertools import *

def solution(elements):
    comb_sum = set(elements)
    elements = elements*2
    for i in range(len(elements)//2):
        for n in range(2, len(elements)//2, 1):
            comb_sum.add(sum(elements[i:i+n]))
    
    return len(comb_sum)+1
    
    # comb_sum = set(elements)
    # comb_sum.add(sum(elements))
    # combs = []
    # for n in range(2, len(elements), 1):
    #     combs += set(combinations(elements, n))
    # for comb in combs:
    #     comb_sum.add(sum(comb))
    # return sorted(comb_sum)