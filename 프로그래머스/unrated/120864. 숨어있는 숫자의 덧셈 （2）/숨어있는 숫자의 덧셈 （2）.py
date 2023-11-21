def solution(my_string):
    temp = []
    check = False
    for i in my_string:
        if i.isdigit():
            if check:
                temp[-1] = temp[-1] + i
            else:
                temp.append(i)
                check = True
        else:
            check = False
    return  sum(int(i) for i in temp)