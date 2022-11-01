# 문제 설명
# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.
#
# 제한사항
# 0 < array의 길이 < 100
# 0 ≤ array의 원소 < 1000
# 입출력 예
# array	result
# [1, 2, 3, 3, 3, 4]	3
# [1, 1, 2, 2]	-1
# [1]	1

def solution(array):
    a = list()
    for i in array:
        a.append(array.count(i))
    if max(a) == a.count(max(a)):
        return max(a)
    else:
        return -1


# print(solution([1,1,2,2,3,3]))