def solution(a, b, n):
    cola_possession = 0
    while n // a >= 1:
        z = (n // a)
        x = n % a
        cola_possession += (n // a) * b
        n = (n // a) * b + n % a # n = 3일때 오류
    return cola_possession

print(solution(2,1,20))