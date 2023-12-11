def solution(n, lost, reserve):
    my_list = [1 for i in range(n+2)]
    for r in reserve:
        my_list[r] = 2
    lost.sort()
    intersection = set(lost)&set(reserve)
    for l in list(intersection):
        if my_list[l]==2:
            my_list[l]=1
            continue
    for l in list(set(lost)-intersection):
        if my_list[l-1]==2:
            my_list[l-1] = 1
            continue
        if my_list[l+1]==2:
            my_list[l+1] = 1
            continue
        my_list[l] = 0
    return n - my_list.count(0)