def solution(N, stages):
    state = [0] * (N + 2)
    for stage in stages:
        state[stage] += 1
    acc_state = [0] * (N + 1)
    acc_state.append(state[-1])
    for i in range(len(state) - 2, -1, -1):
        acc_state[i] = acc_state[i + 1] + state[i]
    res = []
    for i in range(1, len(state)-1):
        res.append((i,0 if acc_state[i]==0 else state[i]/acc_state[i]))
    res.sort(key = lambda x: (-x[1], x[0]))
    return [r[0] for r in res]