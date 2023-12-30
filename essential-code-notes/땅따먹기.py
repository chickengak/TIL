"""
https://school.programmers.co.kr/learn/courses/30/lessons/12913
"""

# My answer
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


# Other's answer
def solution(land):
    n = len(land)

    # dp[i][j] = i행 j열에서 점수의 최대값
    dp = [[0,0,0,0]] + land
    for i in range(1, n+1):
        dp[i][0] += max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
        dp[i][1] += max(dp[i-1][0], dp[i-1][2], dp[i-1][3])
        dp[i][2] += max(dp[i-1][0], dp[i-1][1], dp[i-1][3])
        dp[i][3] += max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

    return max(dp[n])
# 풀이 방식은 같은데 구현에서 차이가 있다.
# 난 max를 안쓰려고 기를 썼는데 어차피 4개니까 빡코딩해서 max찾는게 가장 현명했다.
