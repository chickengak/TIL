def solution(brown, yellow):
    answer = int((brown+4 + ((-brown-4)**2 - 16*(brown+yellow))**0.5 )/4 )
    return [answer, (yellow//(answer-2))+2]