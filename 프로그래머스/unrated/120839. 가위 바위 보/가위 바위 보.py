def solution(rsp):
    win = {"0":"5", "2":"0", "5":"2"}
    answer = ''
    for i in rsp:
        answer += win[i]
    return answer