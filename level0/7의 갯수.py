# 문제 설명
# 머쓱이는 행운의 숫자 7을 가장 좋아합니다.
# 정수 배열 array가 매개변수로 주어질 때,
# 7이 총 몇 개 있는지 return 하도록
# solution 함수를 완성해보세요.
# 1 ≤ array의 길이 ≤ 100
# 0 ≤ array의 원소 ≤ 100,000

# 풀이 유추
# str로 바꿔서 풀이

#테스트 케이스
# array	result
# [7, 77, 17]	4
# [10, 29]	0

# 풀이
def solution(array):
    return str(array).count('7')
print(solution([7, 77, 17]))
