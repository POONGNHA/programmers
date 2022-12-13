# 약수의 개수와 덧셈
# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 1 ≤ left ≤ right ≤ 1,000
# 입출력 예
# left	right	result
# 13	17	43
# 24	27	52


# 재귀함수로 풀어보려다 실패
# def solution(left, right):
#     if left > right:
#         return
#     else:
#         if len(set([i for i in range(1, left // 2) if left // i == 0])) % 2 == 0:
#             return left + solution(left + 1, right)
#         else:
#             return -left + solution(left + 1, right)


def solution(left, right):
    result = []
    for i in range(left, right + 1):
        if len(set([j for j in range(1, i + 1 // 2) if i % j == 0])) % 2 == 1:
            result.append(i)
        elif len(set([j for j in range(1, i + 1 // 2) if i % j == 0])) % 2 == 0:
            result.append(-i)
    return sum(result)


print(solution(13, 17))
