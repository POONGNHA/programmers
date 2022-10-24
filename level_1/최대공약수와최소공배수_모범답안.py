def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)     # 큰수 찾을때 다음부터 이걸로 찾아야겠다. c가 큰수, d가 작은수
    t = 1
    while t > 0:
        t = c % d                   # 나누어떨어지면 t가 0이 되어버림 즉 거기서 식이 끝나는거
        c, d = d, t

    answer = [c, int(a * b / c)]

    return answer


#참고로 GCD는 from fractions import gcd 하면 바로 쓸수있다.