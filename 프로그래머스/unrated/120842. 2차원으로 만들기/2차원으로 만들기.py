def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        t_l = []
        for j in range(i, i+n):
            t_l.append(num_list[j])
        answer.append(t_l)
    return answer