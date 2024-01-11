def solution(numbers):
    answer = []
    for number in numbers:
        binnumber = '0'+bin(number)[2:]
        if binnumber[-1] == '0':
            answer.append(number + 1)
            continue
        for idx in range(len(binnumber)-2, -1, -1):
            if binnumber[idx] == '0':
                answer.append(int('0b'+binnumber[:idx]+'10'+binnumber[idx+2:], 2))
                break
    return answer