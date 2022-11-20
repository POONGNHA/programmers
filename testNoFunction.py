# def solution(arrayA, arrayB):
import copy
from math import sqrt

arrayA = [14, 35, 119]
arrayB = [18, 30, 102]
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
    print(0)
else:
    print(max(fit_divA + fit_divB))
