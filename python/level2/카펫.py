# 풀이유추
# brown = 2 * x + (y-2)*2
# yellow = (x-2) * (y-2)
# brown + yellow = x*y
# brown과 yellow가 주어지면 두 수를 더한 약수짝을 구하고
# 상단 2개의 식에 대입하여 맞는지 확인한다.

# 3보다는 x,y가 커야한다.

# 변수선언
# yellow, brown : int :: input
# return : list :: output

# 나의 풀이
from math import sqrt


def solution(brown, yellow):
    sum_color = brown + yellow
    measure_list = []
    #sum_color의 약수 구하기
    for measure in range(3, int(sqrt(sum_color))+1):
        #나머지가 0일때
        if sum_color%measure == 0 :
            quotient = sum_color//measure
            measure_list.append([quotient,measure])
    # 2개의 식에 부합하는지 확인
    for xyList in measure_list:
        x = max(xyList)
        y = min(xyList)
        if brown == 2 * x + (y-2)*2 and yellow == (x-2) * (y-2):
            return xyList
            
print(solution(24,24))