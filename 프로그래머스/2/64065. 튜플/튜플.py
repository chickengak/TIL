def solution(s):
    mylist = [ set(ss.split(',')) for ss in s[2:len(s) - 2].split('},{')]
    mylist.sort(key=len)
    answer = []
    temp = mylist.pop()
    for _ in range(len(mylist)):
        p = mylist.pop()
        answer.append(int((temp - p).pop()))
        temp = p
    answer.append(int(temp.pop()))
    answer.reverse()
    return answer