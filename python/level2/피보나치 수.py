# 문제 설명
# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 
# 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 와 같이 이어집니다.
# 2 이상의 n이 입력되었을 때, 
# n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, 
# solution을 완성해 주세요.
# n은 2 이상 100,000 이하인 자연수입니다.

# 풀이유추
# 재귀함수의 대표적인 문제
# 재귀함수로 풀이

# 변수선언
# input : n :: int
# output :: int

# 입출력 예
# n	return
# 3	2
# 5	5

# 풀이
def solution(n):
    n_list = [0,1]
    for i in range(len(n_list),n+1):
        n_list.append((n_list[i-1] + n_list[i-2])%1234567)
    return n_list[-1]

print(solution(5))


# 개선점
# 테스트 케이스 6번까지는 통과
# def solution(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return solution(n-1) + solution(n-2)
#
# 시간을 줄이기 위해서는 값을 저장시켜두는게 빠르지 않을까?
# 결과적으로 맞았다. 재귀함수를 하면 시간이 너무 많이 걸리고, 
# list의 형식으로 저장해서 계산하는 방법이 최적해를 도출해낸다.