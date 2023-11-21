def solution(arr, height):
    cnt = sum(1 for i in arr if i > height)
    return cnt