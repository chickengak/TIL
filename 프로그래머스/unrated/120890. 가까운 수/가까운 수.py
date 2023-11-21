def solution(array, n):
    array.sort()
    a_dif = [abs(i-n) for i in array]
    minimum = min(a_dif)
    return array[a_dif.index(minimum)]