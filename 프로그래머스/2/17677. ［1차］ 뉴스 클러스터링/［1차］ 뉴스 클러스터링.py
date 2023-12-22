def transupper(n):
    temp = ord(n)
    if 96 < temp < 123:
        temp -= 32
    if 64 < temp < 91:
        return chr(temp)
    else:
        return '0'

def solution(str1, str2):
    answer = 0
    s1_list = []
    s2_list = []
    is_alphabet = True
    if transupper(str1[0]) == '0':
        is_alphabet = False
        
    for i in range(1, len(str1)):
        transformed = transupper(str1[i])
        if is_alphabet and transformed != '0':
            s1_list.append(str1[i-1:i+1].upper())
            is_alphabet = True
        elif transupper(str1[i]) != '0':
            is_alphabet = True
        elif transupper(str1[i]) == '0':
            is_alphabet = False
            
    is_alphabet = True
    if transupper(str2[0]) == '0':
        is_alphabet = False
    for i in range(1, len(str2)):
        transformed = transupper(str2[i])
        if is_alphabet and transformed != '0':
            s2_list.append(str2[i-1:i+1].upper())
            is_alphabet = True
        elif transupper(str2[i]) != '0':
            is_alphabet = True
        elif transupper(str2[i]) == '0':
            is_alphabet = False
    
    s1_list.sort()
    s2_list.sort()
    
    num = 0; denom = 0;
    s1_idx = 0; s2_idx = 0
    while True:
        if s1_idx == len(s1_list):
            denom += (len(s2_list) - s2_idx)
            break
        if s2_idx == len(s2_list):
            denom += (len(s1_list) - s1_idx)
            break   
        
        if s1_list[s1_idx] == s2_list[s2_idx]:
            print(s1_list[s1_idx])
            num +=1
            s1_idx +=1
            s2_idx +=1
        elif s1_list[s1_idx] > s2_list[s2_idx]:
            s2_idx +=1
        elif s1_list[s1_idx] < s2_list[s2_idx]:
            s1_idx +=1
        denom +=1
            
    return int((1 if denom == 0 else num/denom) *65536)