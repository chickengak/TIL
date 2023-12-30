def solution(begin, target, words):
    answer = 0
    start_list = [begin]
    
    if target not in words:
        return 0
    
    for _ in range(len(words)):
        able_list = []
        for start in start_list:
            for word in words:
                dif = 0
                for idx in range(len(start)):
                    if start[idx] != word[idx]:
                        dif +=1
                if dif == 1:
                    able_list.append(word)
        if target in able_list:
            return answer +1
        elif len(able_list):
            answer +=1
            start_list = able_list
        else:
            return 0
        
    return answer