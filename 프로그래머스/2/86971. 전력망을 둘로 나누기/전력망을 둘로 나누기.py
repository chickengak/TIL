def solution(n, wires):
    wd = {}
    for n1, n2 in wires:
        try: wd[n1].append(n2)
        except: wd[n1] = [n2]

        try: wd[n2].append(n1)
        except: wd[n2] = [n1]
        
    answer = n
    for n1, n2 in wires:
        wd[n1].remove(n2)
        wd[n2].remove(n1)
        visited = set()
        next_visit = {1, }
        while len(next_visit):
            for nxt in list(next_visit):
                visited.add(nxt)
                next_visit.update(set(wd[nxt]))
            next_visit = next_visit - visited
        if len(visited) == n//2 or (n-len(visited)) == n//2:
            return abs(len(visited)- (n-len(visited)))
        else:
            answer = min(abs(len(visited)- (n-len(visited))), answer)
        wd[n1].append(n2)
        wd[n2].append(n1)
    return answer