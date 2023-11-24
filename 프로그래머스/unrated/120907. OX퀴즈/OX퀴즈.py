def solution(quiz):
    ans = []
    for q in quiz:
        q_spl = []
        for i in q.split():
            try:
                q_spl.append(int(i))
            except:
                q_spl.append(i)
        sum = q_spl[0]
        for i in range(1, len(q_spl), 2):
            if q_spl[i] == "+":
                sum += q_spl[i+1]
            elif q_spl[i] == "-":
                sum -= q_spl[i+1]
            else:
                if sum == q_spl[i+1]:
                    ans.append("O")
                else:
                    ans.append("X")
    return ans