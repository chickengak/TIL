def solution(s1, s2):
    cnt = 0
    for i in s1:
        if i in s2:
            cnt += 1

    return cnt


def solution(s1, s2):
    return len(set(s1)&set(s2));
# 두 배열을 셋으로 만들고 교집합의 수를 구함.
# 집합으로 변형한 것.