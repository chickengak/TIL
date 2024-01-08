def solution(number):
    if number >= 500000:
        print(-1)
        return
    elif 0 <= number <= 9:
        print(number)
        return
    cnt = 9
    num = 9
    while cnt != number and num < 9876543211:
        num +=1
        string = str(num)
        for i in range(len(string)-1):
            if string[i] <= string[i+1]:
                length = len(string)-1-i
                temp = 10**length
                remain = num %temp
                num = num - remain +temp-1
                break
        else:
            cnt +=1

    if cnt == number:
        print(num)
    else:
        print(-1)


tcases = int(input())
solution(tcases)

