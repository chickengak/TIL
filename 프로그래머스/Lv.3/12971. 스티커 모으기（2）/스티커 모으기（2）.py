def solution(stickers):
    if len(stickers) < 3:
        return max(stickers)
    sticker = stickers[:-1] + [0]
    dp = sticker[:]
    for idx in range(2, len(sticker)-1):
        dp[idx] = max(dp[idx-1], dp[idx-2]+sticker[idx], dp[idx-3]+sticker[idx])
    answer = dp[-2]

    sticker = stickers[1:] + [0]
    dp = sticker[:]
    for idx in range(2, len(sticker)-1):
        dp[idx] = max(dp[idx-1], dp[idx-2]+sticker[idx], dp[idx-3]+sticker[idx])
    answer = max(dp[-2], answer)

    return answer