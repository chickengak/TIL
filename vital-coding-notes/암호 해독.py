"""
Input: a string, an integer     ( 1 <= cipher <= 1000 , 1 <= code <= len(cipher))
Goal: Pick characters from the string using code as a step
"""


# My answer
def solution(cipher, code):
    return "".join(cipher[i] for i in range(code-1, len(cipher), code))


# Others' answer
def solution(cipher, code):
    return cipher[code-1::code]
# Now I really really mastered it.
