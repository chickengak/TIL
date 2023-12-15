"""
https://school.programmers.co.kr/learn/courses/30/lessons/159994
"""


# My answer
def solution(cards1, cards2, goal):
    cards1_idx = 0; cards1_idx_max = len(cards1) - 1; card1_bool = True
    cards2_idx = 0; cards2_idx_max = len(cards2) - 1; card2_bool = True

    for g in goal:
        if g == cards1[cards1_idx] and card1_bool:
            if cards1_idx == cards1_idx_max:
                card1_bool = False
                continue
            cards1_idx += 1
        elif g == cards2[cards2_idx] and card2_bool:
            if cards2_idx == cards2_idx_max:
                card2_bool = False
                continue
            cards2_idx += 1
        else:
            return "No"
    else:
        return "Yes"
# 내 코드와 아래코드의 아이디어는 같다. 다만, card1_bool과 card2_bool을 추가하려다가 코드가 길어졌다.
# 내가 부올린을 추가한 이유는, index가 초과될 경우 if 조건문에서 인덱싱을 할 때, g == cards1[cards1_idx] 여기에서 인덱스 초과 오류가 발생했기 때문이다.
# 허나 아래처럼, 인덱싱을 and 뒤로 놓고 인덱스가 초과했는지 안했는지를 and 앞에 놓으면 and 앞에 조건문만 보고 False가 되기 때문에 인덱스 초과 오류가 발생하지 않았다.
# 아주 유용하게 쓰일 수 있는 팁을 배울 수 있었다.


def solution(cards1, cards2, goal):
    idx1,idx2=0,0
    for word in goal:
        if len(cards1)>idx1 and cards1[idx1]==word:
            idx1+=1
        elif len(cards2)>idx2 and cards2[idx2]==word:
            idx2+=1
        else:
            return "No"
    return "Yes"