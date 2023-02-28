# 문제 설명
# 선분 3개가 평행하게 놓여 있습니다.
# 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는
# 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를
# return 하도록 solution 함수를 완성해보세요.
# lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.
# 선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.
# lines의 길이 = 3
# lines의 원소의 길이 = 2
# 모든 선분은 길이가 1 이상입니다.
# lines의 원소는 [a, b] 형태이며, a, b는 각각 선분의 양 끝점 입니다.
# -100 ≤ a < b ≤ 100

# 풀이유추
# 3가지 경우가 존재한다. 만남이 없을경우, 교집합이 1개인경우, 교집합이 2개인경우
# 1. 만남이 없을 경우 : 제일 작은 start를 가진 원소의 end가 다른 원소의 start보다 크지 않고,
# 두번째로 작은 start를 가진 원소의 end가 다른 원소의 strat보다 작아야한다.
# 2. 교집합이 1개인 경우 : 2선분이 겹치는 경우와 3선분이 겹치는 경우가 존재한다.
# 선분 2개가 겹치는 경우는 겹치는 선분이 다른 선분 2개를 포함하는 경우와 다 포함하지 못하는경우가 있고,
# 3선분이 겹치는 경우는
# 교집합이 2개인 경우에는 2개의 선분이 하나의 선분에 걸쳐서 교집합이 만들어지는 경우

# 프로그래밍 순서
# input을 1의 길이를 가지는 단위로 쪼개서, 중복되는 원소의 갯수를 return
# return값이 범위가 아니므로, 숫자 한개만 저장한다.

# 변수 이름
# input : lines
# linesDiv1_list :: 1로 쪼갠 수들을 원소로 갖는 list : 범위를 저장하지 않고, 시작점을 기준으로만 저장한다.
# output : set(lineDiv1_list)와 lineDiv1_list의 갯수 차이를 return

# 테스트케이스
# lines	result
# [[0, 1], [2, 5], [3, 9]]	2
# [[-1, 1], [1, 3], [3, 9]]	0
# [[0, 5], [3, 9], [1, 10]]	8
# [0,1,2,3,4, 3,4,5,6,7,8, 1,2,3,4,5,6,7,8,9]

# 나의 풀이
def solution(lines):
    lineDiv1_list = list()
    for element_list in lines:
        for i in range(element_list[0], element_list[1]):
            if lineDiv1_list.count(i) < 2:
                lineDiv1_list.append(i)
    return len(lineDiv1_list) - len(set(lineDiv1_list))
    # return lineDiv1_list) : [0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # return set(lineDiv1_list) : {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(solution([[0, 5], [3, 9], [1, 10]]))

# 틀린점
# 2개 겹칠때는 생각을 안함