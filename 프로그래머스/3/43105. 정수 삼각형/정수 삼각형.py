def solution(triangle):
    answer = 0
    tri = [triangle[0]]
    for i in range(len(triangle)):
        row = []
        for j in range(i+1):
            a = tri[max(i-1,0)][max(j-1,0)]+triangle[i][j]
            b = tri[max(i-1,0)][min(j,i-1)]+triangle[i][j]
            row.append(max(a,b))
        if len(row) == 1:
            pass
        else:
            tri.append(row)
        
    return max(tri[-1])