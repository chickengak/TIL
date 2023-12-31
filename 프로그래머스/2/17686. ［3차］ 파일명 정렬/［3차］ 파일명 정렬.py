def solution(files):
    answer = []
    splitted_list = []
    
    for idx, value in enumerate(files):
        head = ''
        head_continue = True
        number = ''
        #tail = ''
        value = value.lower()
        for i in range(len(value)):
            if head_continue and ((96 < ord(value[i]) < 123) or value[i] == ' ' or value[i] == '.' or value[i] == '-'):
                head += value[i]
            elif (47 < ord(value[i]) < 58) and (len(number) < 6):
                head_continue = False
                number += value[i]
            else:
                #tail = value[i:]
                break
        number = int(number) if number else 0
        splitted_list.append([idx, head, number])
    
    return [files[file[0]] for file in sorted(splitted_list, key = lambda x: (x[1], x[2], x[0]))]