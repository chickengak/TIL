def solution(my_string):
    ans = my_string[0]
    for i in my_string[1:]:
            if i not in ans:
                ans += i
    return ans