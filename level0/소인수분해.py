# 문제 설명
# 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다.
# 따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
# 2 ≤ n ≤ 10,000

# 풀이유추
# 아리스토텔레스의 체 사용


# 테스트케이스    b
# n	result
# 12	[2, 3]
# 17	[17]
# 420	[2, 3, 5, 7]

#내풀이
from math import sqrt

div = []
result = []
def solution(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            div.append(i)
            div.append(n//i)

    if not div:
        return [n]
    else:
        div.sort()
        while(True):
            if not div:
                break
            else:
                if n % min(div) == 0:
                    result.append(min(div))
                    n = n // min(div)
                else:
                    div.remove(min(div))
    return list(set(result))


print(solution(623))