# 문제 설명
# Finn은 요즘 수학공부에 빠져 있습니다. 
# 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 
# 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15
# 자연수 n이 매개변수로 주어질 때, 
# 연속된 자연수들로 n을 표현하는 방법의 수를 
# return하는 solution를 완성해주세요.
# n은 10,000 이하의 자연수 입니다.

# 풀이 유추
# 일단 절반+1 의 숫자까지만 세도 된다. 연속된 더하기라는것이 절반까지 성립하는것은 홀수일때만
# DP를 사용해서 1부터 순간순간의 최적해를 구하면 답이 나올것같다.

# 변수선언
# input : n :: int
# output : result :: int

# 입출력 예
# n	result
# 15	4

# 풀이
from math import ceil


def solution(n):
    result = 0
    for num in range(1,ceil(n//2)):
        sum_num = 0
        for factorial_num in range(1,num+1):
            if sum_num == n:
                result += 1
            if sum_num > n:
                break
            else:
                sum_num += factorial_num
    return result

print(solution(15))