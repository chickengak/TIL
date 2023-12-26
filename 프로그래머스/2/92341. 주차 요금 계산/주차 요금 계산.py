def timediff(enter, out):
    out = out.split(':')
    enter = enter.split(':')
    return (int(out[0])*60+int(out[1])) - (int(enter[0])*60+int(enter[1]))

def calcfee(fees, time):
    if time <= fees[0]:
        return fees[1]
    else:
        share, remain = divmod(time-fees[0], fees[2])
        return fees[1] + ((share + (1 if remain >0 else 0))*fees[3])

def solution(fees, records):
    rsplit = [record.split() for record in records]
    dic = dict()
    for r in rsplit:
        try:
            dic[r[1]].append(r[0])
        except:
            dic[r[1]] = [r[0]]
    answer = []
    for key, value in dic.items():
        total = 0
        if len(value)%2:   #홀수 일 때
            total += timediff(value[-1],'23:59')
            value.pop()
        while value:
            out_time = value.pop()
            enter_time = value.pop()
            total += timediff(enter_time,out_time)
        answer.append([key, calcfee(fees, total)])
    answer.sort(key=lambda x:x[0])
    return [ans[1] for ans in answer]