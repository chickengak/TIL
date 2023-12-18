def dfs(x, acc,n):
    global answer
    if acc+x == n:
        answer +=1
        return
    elif acc+x > n:
        return
    else:
        return dfs(x+1, acc+x, n)
    
def solution(n):
    global answer
    answer = 0
    for i in range(1, n//2+1):
        dfs(i, 0, n)
    return answer+1