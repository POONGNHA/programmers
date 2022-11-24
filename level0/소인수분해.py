# 문제 설명
# 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다.
# 따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
# 2 ≤ n ≤ 10,000

# 풀이유추
# 아리스토텔레스의 체 사용


# 테스트케이스    b
# n	result
# 12	[2, 3]
# 17	[17]
# 420	[2, 3, 5, 7]

import copy

def solution(n):
    n_list = [i for i in range(2,n+1)]
    result = []
    while(True):
        compare_list = copy.deepcopy(n_list) # comparelist가 복사된다. comparelist는 소수도 다 지워버림
        if not compare_list: #compare_list가 비어있다면 중지
            return result
        else:
            result.append(min(compare_list)) #
            for i in compare_list:
                if i % max(result) == 0:
                    n_list.remove(i)
