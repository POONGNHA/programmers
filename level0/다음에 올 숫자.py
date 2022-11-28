# 문제 설명
# 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.
# 2 < common의 길이 < 1,000
# -1,000 < common의 원소 < 2,000
# 등차수열 혹은 등비수열이 아닌 경우는 없습니다.
# 공비가 0인 경우는 없습니다.

# 풀이 유추
# input이 등차인지 등비인지를 먼저 파악한다.
# input의 최소len은 3
# 등비인지를 판별하고, 아니라면 등차수열로 판별하도록
# 등차는 a1, a1+k, (a1+k)+k
# 등비는 a1 + a1*k ...

# 테스트케이스
# common	result
# [1, 2, 3, 4]	5
# [2, 4, 8]	16

def solution(common):
    if 0 in common:
        return common[-1] + (common[-1] - common[-2])
    else:
        if common[-1] / common[-2] == common[-2] / common[-3]:
            return common[-1] * (common[-1] // common[-2])
        else:
            return common[-1] + (common[-1] - common[-2])


print(solution([1,2,3,4]))

#실패케이스
# list의 값중에 0이 원소로 포함되어있으면 나눗셈 과정에서 오류가 난다.
# 0이 포함되는 문제라면 0의 처리를 우선적으로 해주어야 오류가 없다.