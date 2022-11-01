def solution(a, b, n):
    for _ in range(5):
        result = 0
        result += (n // a) * b + n % a
    return result

print(solution(2,1,20))