# 문제 설명
# 철수와 영희는 선생님으로부터 숫자가 하나씩 적힌 카드들을 절반씩 나눠서 가진 후,
# 다음 두 조건 중 하나를 만족하는 가장 큰 양의 정수 a의 값을 구하려고 합니다.
# 1. 철수가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고
# 영희가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a
# 2. 영희가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고,
# 철수가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a
# 예를 들어, 카드들에 10, 5, 20, 17이 적혀 있는 경우에 대해 생각해 봅시다.
# 만약, 철수가 [10, 17]이 적힌 카드를 갖고, 영희가 [5, 20]이 적힌 카드를 갖는다면
# 두 조건 중 하나를 만족하는 양의 정수 a는 존재하지 않습니다.
# 하지만, 철수가 [10, 20]이 적힌 카드를 갖고, 영희가 [5, 17]이 적힌 카드를 갖는다면,
# 철수가 가진 카드들의 숫자는 모두 10으로 나눌 수 있고, 영희가 가진 카드들의 숫자는 모두 10으로 나눌 수 없습니다.
# 따라서 철수와 영희는 각각 [10, 20]이 적힌 카드, [5, 17]이 적힌 카드로 나눠 가졌다면
# 조건에 해당하는 양의 정수 a는 10이 됩니다.
# 철수가 가진 카드에 적힌 숫자들을 나타내는 정수 배열 arrayA와
# 영희가 가진 카드에 적힌 숫자들을 나타내는 정수 배열 arrayB가 주어졌을 때,
# 주어진 조건을 만족하는 가장 큰 양의 정수 a를 return하도록 solution 함수를 완성해 주세요.
# 만약, 조건을 만족하는 a가 없다면, 0을 return 해 주세요.

# 제한조건
# 1 ≤ arrayA의 길이 = arrayB의 길이 ≤ 500,000
# 1 ≤ arrayA의 원소, arrayB의 원소 ≤ 100,000,000
# arrayA와 arrayB에는 중복된 원소가 있을 수 있습니다.

# 풀이유추
# 1. 입력배열A의 약수들이 원소가 되는 리스트를 만든다.
# 2. 입력배열A의 가장 작은 숫자를 제외한 나머지 원소들을 1에서 만든 배열의 가장 큰 숫자가 나눌 수 있고,
# 입력배열B의 원소들을 나눌수 없는지 확인한다.
# 3. 큰숫자부터 제일 작은 숫자까지 1의 배열의 원소들을 다 찾아보고, 빈 배열이 된다면 0을 리턴한다.
# 4. 빈 배열이 아니라면 B까지 똑같이 실행한 후에 더 큰수를 return한다.

# 변수 선언
# input : arrayA, B
# div_A, B : 약수의 집합
# fit_divA, B : 조건에 fit한 divisor라면 이 배열에 집어넣음
# max_a, b = 제일 큰 숫자
# output :

# 테스트 케이스
# arrayA	arrayB	result
# [10, 17]	[5, 20]	0
# [10, 20]	[5, 17]	10
# [14, 35, 119]	[18, 30, 102]	7

# 나의 풀이
import copy
from math import sqrt

def solution(arrayA, arrayB):
    # arrayA = [14, 35, 119]
    # arrayB = [18, 30, 102]
    # 1. 약수를 담은 리스트를 만든다.
    div_A = list()
    div_B = list()
    fit_divA = list()
    fit_divB = list()
    # 약수 구하기
    for i in range(1, int(sqrt(min(arrayA)))):
        if min(arrayA) % i == 0:
            div_A.append(i)
            div_A.append(min(arrayA) // i)
    # 2. 가장 작은 원소를 제외한 다른 원소들을 div_a의 제일 큰 숫자가 나눌수 있어야한다.
    # 큰 원소부터 / 1 빼주기
    div_A.sort(reverse=True)
    div_A.pop()
    # 입력배열 A의 제일 작은 원소의 약수들이 arrayA의 나머지 원소들의 약수가 되는가?
    # 입력배열 B는 약수로 나누었을때 나누어지지 않는가?
    fit_divA = copy.deepcopy(div_A)
    for m in div_A:
        passFlag = True
        for j in arrayA:
            if j % m != 0:
                fit_divA.remove(m)
                passFlag = False
                break
        if passFlag:
            for k in arrayB:
                if k % m == 0:
                    fit_divA.remove(m)
                    break
    # B도 똑같이 구해준다
    for i in range(1, int(sqrt(min(arrayB)))):
        if min(arrayB) % i == 0:
            div_B.append(i)
            div_B.append(min(arrayB) // i)
    div_B.sort(reverse=True)
    div_B.pop()
    fit_divB = copy.deepcopy(div_B)
    for m in div_B:
        passFlag = True
        for j in arrayB:
            if j % m != 0:
                fit_divB.remove(m)
                passFlag = False
                break
        if passFlag:
            for k in arrayA:
                if k % m == 0:
                    fit_divB.remove(m)
                    break
    # fit_div 리스트 2개를 합쳐서 제일 큰 값을 리턴하고, 없다면 0을 리턴
    if not fit_divA + fit_divB:
        return 0
    else:
        return max(fit_divA + fit_divB)

# 틀린부분
# 나머지는 //가 아니고 %임 (매일 착각함)
# 시간복잡도 처리 필요 => 약수문제는 제곱근을 이용해서 풀자
# for문의 횟수를 지정하는 변수는 그 for문 내에서 수정하지 말자
# copy.deepcopy와 shallow copy를 구분하자
# 약수를 구하는 문제에서는 자기 자신의 숫자와 1의 취급을 항상 생각하자
#