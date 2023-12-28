def solution(land):
    
    for row in range(len(land)-1):
        temp = [[i,v] for i, v in enumerate(land[row])]
        temp.sort(key = lambda x: x[1], reverse = True)
        for i in range(4):
            if temp[0][0] != i:
                land[row+1][i] += temp[0][1]
            else:
                land[row+1][i] += temp[1][1]
        
    
    return max(land[-1])