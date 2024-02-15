"""
I: a list containing the string id and the stirng pw. And DB consists of combination of id and pw.
G: Return 'login' for a successful login, 'wrong pw' for an incorrect password, and 'fail' using the provided id_pw through DB.
https://school.programmers.co.kr/learn/courses/30/lessons/120883
"""


# My answer
def solution(id_pw, db):
    for i in db:
        if id_pw[0] == i[0]:
            if id_pw[1] == i[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"


# Others' answer
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"
# This code used dict and := operator.
