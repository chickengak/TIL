def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = bin(arr1[i]|arr2[i])[2:].zfill(n)
        answer.append(temp.replace("1", "#").replace("0", " "))
    return answer