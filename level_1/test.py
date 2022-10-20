def solution(n, m):
    result1 = set([i for i in range(1, n + 1) if n % i == 0])
    result2 = set([i for i in range(1, m + 1) if m % i == 0])
    result_final1 = max(list(result1.intersection(result2)))

    result3 = [i for i in range()]

    return [result_final1]


print(solution(3, 12))