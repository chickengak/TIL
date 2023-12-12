def solution(people, limit):
    full_boats = 0
    people.sort()
    left=0; right = len(people)-1
    while right >= left:
        if (people[left]+people[right]) <= limit:
            full_boats +=1
            left +=1
            right -=1
        else:
            full_boats +=1
            right -=1
    return full_boats
        
    
    
    
    
    
    
    
    
    
    

#     boats = []
#     full_boats = 0
#     limiteq = 0
#     for p in sorted(people, reverse=True):
#         for i, b in enumerate(boats):
#             if b == p:
#                 boats.pop(i)
#                 full_boats +=1
#                 break
#             elif b > p:
#                 boats[i] = b-p
#                 break
#         else:
#             if p != limit:
#                 boats.append(limit-p)
#             else:
#                 limiteq += 1
    
#     return full_boats+limiteq+len(boats)