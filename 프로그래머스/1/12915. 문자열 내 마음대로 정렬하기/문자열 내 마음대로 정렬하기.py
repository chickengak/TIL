def solution(strings, n):
    # return sorted(strings, key=lambda x: (x[n], x[a] for a in range(len(x))))
    new_strs = []
    for i, v in enumerate(strings):
        new_strs.append([i, v[n]+v[:n]+v[n+1:]])
    new_strs.sort( key=lambda x: x[1])
    
    return [strings[i[0]] for i in new_strs]