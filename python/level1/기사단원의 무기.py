# 문제 설명
# 숫자나라 기사단의 각 기사에게는 1번부터 number까지 번호가 지정되어 있습니다. 
# 기사들은 무기점에서 무기를 구매하려고 합니다.
# 각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려 합니다. 
# 단, 이웃나라와의 협약에 의해 공격력의 제한수치를 정하고, 
# 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 
# 협약기관에서 정한 공격력을 가지는 무기를 구매해야 합니다.
# 예를 들어, 15번으로 지정된 기사단원은 
# 15의 약수가 1, 3, 5, 15로 4개 이므로, 
# 공격력이 4인 무기를 구매합니다. 
# 만약, 이웃나라와의 협약으로 정해진 공격력의 제한수치가 3이고 
# 제한수치를 초과한 기사가 사용할 무기의 공격력이 2라면, 
# 15번으로 지정된 기사단원은 무기점에서 공격력이 2인 무기를 구매합니다. 
# 무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요합니다. 
# 그래서 무기점에서 무기를 모두 만들기 위해 
# 필요한 철의 무게를 미리 계산하려 합니다.
# 기사단원의 수를 나타내는 정수 number와 
# 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수 limit와 
# 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 power가 주어졌을 때, 
# 무기점의 주인이 무기를 모두 만들기 위해 
# 필요한 철의 무게를 return 하는 solution 함수를 완성하시오.
# 1 ≤ number ≤ 100,000
# 2 ≤ limit ≤ 100
# 1 ≤ power ≤ limit


# 풀이 유추
# 약수의 갯수를 sqrt로 구함
# 각 숫자마다 약수의 갯수를 list에 넣음
# list 원소 갯수가 limit를 넘기면 power로 바꿈
# list 합을 구해서 result로 return

# 변수
# number, limit power : input : int
# divList : list 
# result : output : list


# 입출력 예
# number	limit	power	result
# 5    	    3       2	    10      : 1 + 2 + 2 + 3 + 2
# 10	    3       2	    21

# 풀이
from math import ceil, sqrt


def solution(number, limit, power):
    result = []
    for i in range(1,number+1): # factorial 수 i
        div_list = []
        if i == 1:
            div_list.append(1)
        else:
            for j in range(1, int(sqrt(i))+1): # 각 숫자의 약수 구하기
                if i % j == 0: # 나머지가 0일때
                    div_list.append(j)
                    div_list.append(i//j)
        if len(set(div_list)) > limit:
            result.append(power)
        else:
            result.append(len(set(div_list)))
    return sum(result)

print(solution(10,3,2))
                