def solution(answers):
    answer = [0,0,0]
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        ans = answers[i]
        if ans == a[i%5]:
            answer[0] +=1
        if ans == b[i%8]:
            answer[1] +=1
        if ans == c[i%10]:
            answer[2] +=1
    
    return [i+1 for i in range(len(answer)) if max(answer) == answer[i]]