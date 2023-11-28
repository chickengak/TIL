def solution(s, skip, index):
    my_list = list(chr(i) for i in range(97, 123))
    for c in skip:
        my_list.remove(c)
    length = len(my_list)
    return "".join(my_list[(my_list.index(c)+index) % length] for c in s)