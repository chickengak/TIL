def solution(word):
    words = ["A", "E", "I", "O", "U"]
    nums = [781, 156, 31, 6, 1]
    answer = 0
    for i in range(len(word)):
        answer += (words.index(word[i])) * nums[i]
    return answer + len(word)
