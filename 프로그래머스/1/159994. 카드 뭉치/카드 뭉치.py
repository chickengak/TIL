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