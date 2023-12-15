"""

"""


# My answer
def solution(number, k):
    answer = ""
    searching_start = 0
    target = len(number)-k

    while len(answer) != target:
        maximum = "-1"
        max_list = []
        for i, v in enumerate(number[searching_start:k+1+len(answer)]):
            if v > maximum:
                maximum = v
                max_list = []
            if v == maximum:
                max_list.append(i+searching_start)

        for idx in max_list:
            try:
                if number[k+len(answer)]<= maximum:
                    answer += maximum
                    searching_start = idx+1
                else:
                    break # 다시 큰 수 찾기.
            except:
                pass
    return answer


# Other's answer
def solution(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    return ''.join(st[:len(st) - k])
# 나보다 빠른데 심지어 두배 빠름. 디버깅 필요.

