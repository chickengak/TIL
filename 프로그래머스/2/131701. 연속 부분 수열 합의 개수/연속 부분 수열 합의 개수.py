def solution(elements):
    comb_sum = set(elements)
    elements = elements*2
    for i in range(len(elements)//2):
        for n in range(2, len(elements)//2, 1):
            comb_sum.add(sum(elements[i:i+n]))
    
    return len(comb_sum)+1