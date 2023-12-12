def solution(number, k):
    answer = ""
    searching_start = 0
    target = len(number)-k

    while len(answer) != target:
        maximum = "-1"
        max_list = []
        for i, v in enumerate(number[searching_start:k+1+len(answer)]):
            if v > maximum:
                maximum = v
                max_list = []
            if v == maximum:
                max_list.append(i+searching_start)

        for idx in max_list:
            try:
                if number[k+len(answer)]<= maximum:
                    answer += maximum
                    searching_start = idx+1
                else:
                    break # 다시 큰 수 찾기.
            except:
                pass
    return answer