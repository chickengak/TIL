def solution(money):
    return [money // 5500, money % 5500]


def solution(money):
    return divmod(money, 5500)
# 이건 튜플로 리턴됨.