def solution(x, n):
    if x == 0:
        return [0 for i in range(n)]
    else:
        return [i for i in range(x, x + x * (n), x)]
