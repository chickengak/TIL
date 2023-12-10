def dfs(numbers, idx, target, total):
    global answer
    if idx == len(numbers):
        if total == target:
            answer +=1
        return
    else:
        dfs(numbers, idx + 1, target, total+numbers[idx])
        dfs(numbers, idx + 1, target, total-numbers[idx])
    return

def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, 0,target, 0)
    return answer