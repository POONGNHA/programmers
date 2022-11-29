# 문제 설명
# 머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 구슬은 모두 다르게 생겼습니다.
# 머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때,
# balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.
# 1 ≤ balls ≤ 30
# 1 ≤ share ≤ 30
# 구슬을 고르는 순서는 고려하지 않습니다.
# share ≤ balls
# 서로 다른 n개 중 m개를 뽑는 경우의 수 공식 = n!/(n-m)!*m!


# 풀이 유추
# 공식을 사용해서 return


# testcase
# balls	share	result
# 3	2	3
# 5	3	10

# sol 1
# def solution(balls, share):
#     n = 1
#     m = 1
#     for i in range(1,balls+1):
#         n *= i
#     for j in range(1,share+1):
#         m *= j
#     return n/((balls-share)*m)

# sol 2
import math


def solution(balls, share):
    return math.factorial(balls) / (math.factorial(balls - share) * math.factorial(share))




print(solution(3,2))

