import math
def solution(n1,d1,n2,d2):
    t1, t2 = (n1 * d2 + n2 * d1), (d1 * d2)
    gcd = math.gcd(t1, t2)
    return [int(t1/gcd), int(t2/gcd)]
