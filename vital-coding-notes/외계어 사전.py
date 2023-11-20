"""
I
G
"""


# My answer
def solution(spell, dic):
    for i in dic:
        for j in spell:
            if j in i:
                continue
            else:
                break
        else:
            return 1
    return 2


# Others' answer
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
#good use of set

