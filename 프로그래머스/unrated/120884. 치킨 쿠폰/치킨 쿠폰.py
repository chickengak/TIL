def solution(chicken):
    free_chicken = 0
    share = chicken
    remainder = 0
    while share:
        share, t = divmod(share, 10)
        free_chicken += share
        remainder += t
        if remainder > 9:
            free_chicken += 1
            remainder -= 9
    return free_chicken