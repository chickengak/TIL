def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key = lambda x: (x*4)[:4], reverse=True)
    ans = "".join(n for n in numbers)
    if set(ans) == {'0'}:
        return "0"
    return ans
    
    
    # numbers = [str(i) for i in numbers]
    # n_list = [[i, n.ljust(4, n[0])] for i, n in enumerate(numbers)]
    # ans = "".join(numbers[i[0]] for i in sorted(n_list, key=lambda x:x[1], reverse=True))
    # try:
    #     while ans[0] == "0":
    #         ans = ans[1:]
    # except: pass
    # return ans if ans else "0"