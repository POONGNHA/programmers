# 문제 설명
# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 
# 두 직선이 평행이 되는 경우가 있으면 
# 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.
# 0 ≤ dots의 원소 ≤ 100
# dots의 길이 = 4
# dots의 원소의 길이 = 2
# dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
# 서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
# 두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
# 임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.

# 풀이 유추
# 기울기라는것은 dy/dx 로 표현할 수 있다
# dot 원소 길이는 4로 고정이 되어있기 때문에,
# 1과2, 1과3, 1과4의 기울기를 3번 계산한후에
# 기울기가 같다면 1을 return 아니라면 0을 return

# 변수 선언
# input : dots : array
# degree : float
# return : int 

# 입출력 예
# dots	result
# [[1, 4], [9, 2], [3, 8], [11, 6]]	1
# [[3, 5], [4, 1], [2, 4], [5, 10]]	0

# 프로그래밍 순서
# [1,2] [3,4]의 기울기
# [1,3] [2,4]의 기울기
# [1,4] [2,3]의 기울기
# 하나라도 평행이면 1 return
# 아니라면 0 return

# 풀이
def solution(dots):
    def degree(array1,array2):
        return (array1[1]-array2[1]) / (array1[0] - array2[0])
    if degree(dots[0],dots[1]) == degree(dots[2],dots[3]) or degree(dots[0],dots[2]) == degree(dots[1],dots[3]) or degree(dots[0],dots[3]) == degree(dots[1],dots[2]):
        return 1
    return 0

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))