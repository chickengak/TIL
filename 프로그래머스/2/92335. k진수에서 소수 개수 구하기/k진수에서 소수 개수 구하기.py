def solution(n, k):
    share=n
    remainder = 0
    transform = ''
    while share:
        share, remainder = divmod(share, k)
        transform += str(remainder) 
    transform = transform[::-1]
    tf_list = transform.split('0')
    cnt = 0
    num = 0
    for tf in list(tf_list):
        try:
            num = int(tf)
            if num == 1:
                continue
        except:
            continue
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            cnt+=1
    return cnt