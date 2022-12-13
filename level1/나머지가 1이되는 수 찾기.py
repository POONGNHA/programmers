def solution(n):
    return [i for i in range(1,n) if n % i == 1][0]