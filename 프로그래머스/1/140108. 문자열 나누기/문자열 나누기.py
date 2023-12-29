def solution(s):
    answer = 0
    synch = 0
    asynch = 0
    compare = ''
    for i in range(len(s)):
        if not compare:
            compare = s[i]
            synch +=1
        elif compare == s[i]:
            synch +=1
        else:
            asynch += 1
            if synch == asynch:
                answer +=1
                synch = 0
                asynch = 0
                compare = ''
    return answer+1 if synch else answer