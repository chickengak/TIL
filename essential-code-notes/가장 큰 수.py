"""
https://school.programmers.co.kr/learn/courses/30/lessons/42746
"""


# My answers
def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    ans = "".join(n for n in numbers)
    if set(ans) == {'0'}:
        return "0"
    return ans
# 처음으로 내가 풀지 못한 문제다. 일단, 아래 코드가 내가 끝까지 풀던 문제였다.
# 둘은 정말 비슷한 원리를 가졌는데 결정적으로 아래는 56, 565를 제대로 구분하지 못 한다. 56556 이랑 56565랑 입력순서에 따라 제각각이다.
# 길이까지 체크했다면 풀순 있었을테지만 많이 복잡해지고 의도했던 방향도 아닌거 같아서 sort 방법에 집중했다.
# sort key만 잘 주면 해결되긴 할거 같아서 정말 2~3일을 고민했는데 결국 풀지 못하고 힌트를 봤다.
# 나는 숫자가 들어오면 첫 숫자로 모두 채운 후 sort 했다. 56을 5655로 만들고 정렬한 것이다. 하지만 565도 5655가 되기 때문에 딱 이 경우를 해결할 수 없었다.
# 다만 이는 숫자를 반복하는것으로 해결할 수 있었다. 56을 5656 으로 565를 565565로 하고 문자열 sort를 하면 앞뒤 순서도 완벽해진다.
# 뒤를 채워서 sort한다는 아이디어까진 좋았는데 약간의 차이때문에 결과가 달라졌다.


def solution(numbers):
    numbers = [str(i) for i in numbers]
    n_list = [[i, n.ljust(4, n[0])] for i, n in enumerate(numbers)]
    ans = "".join(numbers[i[0]] for i in sorted(n_list, key=lambda x:x[1], reverse=True))
    try:
        while ans[0] == "0":
            ans = ans[1:]
    except: pass
    return ans if ans else "0"