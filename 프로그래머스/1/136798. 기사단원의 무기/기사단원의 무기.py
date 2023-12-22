def solution(number, limit, power):
    weapon_list = []    
    for n in range(1, number+1):
        temp = set()
        for s in range(1, int(n**0.5)+1):
            if n % s == 0:
                temp.add(s)
                temp.add(n//s)
        weapon_list.append(len(temp))
            
    return sum([ power if w > limit else w for w in weapon_list])