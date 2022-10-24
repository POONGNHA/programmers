def solution(n, m):

    # 최대공약수(GCD) : 유클리드 호제법 사용
    result1 = set([i for i in range(1, n + 1) if n % i == 0])
    result2 = set([i for i in range(1, m + 1) if m % i == 0])
    GCD = sorted(list(result1.intersection(result2)))[-1]

    # 최소공배수(LCM) : n * m = 최대공약수 * 최소공배수
    LCM = (n * m) // GCD


    return [GCD,LCM]

print(solution(3,12))