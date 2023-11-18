def solution(num_list):
    a = [0, 0]
    for i in num_list:
        if i%2: a[1] +=1
        else: a[0] += 1
    return a