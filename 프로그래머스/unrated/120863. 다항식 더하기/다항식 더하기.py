def solution(polynomial):
    x = 0
    integer = 0
    for i in polynomial.split(" + "):
        if i[-1] == "x":
            try:
                x += int(i[:-1])
            except:
                x += 1
        else:
            integer += int(i)
            
    ans = ""
    if x != 0:
        if x == 1:
            ans += "x"
        else:
            ans += str(x) + "x"
    if ans and integer != 0:
        ans += " + "
    if integer != 0:
        ans += str(integer)
    return ans