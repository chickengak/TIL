def solution(x, y, n):
    answer = 0
    cur_set = {x}
    while y not in cur_set:
        next_set = set()
        while cur_set:
            num = cur_set.pop()
            calc_list = [num+n, num*2, num*3]
            next_set.update([calc for calc in calc_list if calc <= y])
        cur_set = next_set
        if not cur_set or min(cur_set) > y:
            return -1
        answer +=1
    return answer