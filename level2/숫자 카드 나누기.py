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
# 제일 작은 수의 약수를 찾는다.
# 그 약수로 그 배열의 원소들을 일일히 나누어 보았을때 나머지가 0이어야 한다.
# 그 수로 또다른 배열의 원소들을 나누었을 때 나머지가 0 이외의 것이어야만 한다.
# 두 배열에 똑같이 시행하여 약수를 찾는다.
# 나온 약수중 제일 큰 수를 반환한다.
# 찾을 수 없다면 0을 선언한다.

# 변수 선언
# input : arr1, arr2
# arrayA_minNumber_divisor, arrayB_minNumber_divisor : 제일 작은 수의 약수들을 담는다.
# divisor_collectionA, B : 공통약수이며, 나눌 수 없는 약수들을 담는다.
# output : no declaration

# 테스트 케이스
# arrayA	arrayB	result
# [10, 17]	[5, 20]	0
# [10, 20]	[5, 17]	10
# [14, 35, 119]	[18, 30, 102]	7

# 프로그래밍 순서
# 주어진 배열에서 가장 작은 수를 찾고,
# 그것의 약수를 하나의 배열에 담는다.
# 그 배열의 원소들을 input Array의 다른 요소들로 나누어 나머지가 0이 되는지 확인한다.
# 그 배열에서 가장 큰 값을 리턴한다.
# 배열이 비었다면 0을 리턴한다.

# 나의 풀이

    # 가장 작은수의 약수를 배열에 담는다.
from math import sqrt

def solution(arrayA, arrayB):
# arrayA = [14, 35, 119]
# arrayB = [18, 30, 102]
    arrayA_minNumber_divisor = []
    for i in range(1, int(sqrt(min(arrayA)))):
        if min(arrayA) % i == 0:
            arrayA_minNumber_divisor.append(i)
            arrayA_minNumber_divisor.append(min(arrayA) // i)
    arrayB_minNumber_divisor = []
    for i in range(1,  int(sqrt(min(arrayB)))):
        if min(arrayB) % i == 0:
            arrayB_minNumber_divisor.append(i)
            arrayB_minNumber_divisor.append(min(arrayB) // i)
    # A입력배열의 원소들이 나누어 지는지 확인한다.
    for inputElementA in arrayA :
        if inputElementA != min(arrayA):
            for divisors in arrayA_minNumber_divisor :
                if inputElementA % divisors != 0:
                    arrayA_minNumber_divisor.remove(divisors)
    # 다른 입력배열을 나누지 못하는지 확인한다.
    for inputElementB in arrayB :
        for divisors in arrayA_minNumber_divisor :
            if inputElementB % divisors == 0 and divisors != 1:
                return 0
    # B입력배열의 원소들이 나누어 지는지 확인한다.
        for inputElement in arrayB :
            if inputElement != min(arrayB):
                for divisors in arrayB_minNumber_divisor :
                    if inputElement % divisors != 0 :
                        arrayB_minNumber_divisor.remove(divisors)
    # 다른 입력배열을 나누지 못하는지 확인한다.
    for inputElement in arrayA :
        for divisors in arrayB_minNumber_divisor :
            if inputElement % divisors == 0 and divisors != 1:
                return 0
    # 2개의 약수의 리스트를 합해서 비어있다면 0을 리턴하고, 아니라면 최대값을 출력한다.
    if (arrayB_minNumber_divisor + arrayB_minNumber_divisor) == 0:
        return 0
    else:
        return max(arrayA_minNumber_divisor + arrayB_minNumber_divisor)


# 틀린부분
# input array에서 제일 작은 자기자신의 수를 빼는것을 빼먹음
# 또다른 입력배열을 나누면 그대로 0을 리턴해야하는것을 빼먹음
# if문에서 그냥 []을 처리할때 +를 사용하면 되는 것이었음
# 나머지는 //가 아니고 %임
# 시간복잡도 처리 필요
# 약수를 최적으로 구하는 법 : 루트 N까지 약수를 구한다음,그 약수들로 N을 나누어주고 그 몫을 추가해주면
# 그것이 약수가 된다.