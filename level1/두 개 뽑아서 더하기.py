# 문제 설명
# 정수 배열 numbers가 주어집니다. 
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 
# 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 
# solution 함수를 완성해주세요.

# 제한사항
# numbers의 길이는 2 이상 100 이하입니다.
# numbers의 모든 수는 0 이상 100 이하입니다.

# 풀이유추
# iter에 속한 기능인 combination 펑션 사용
# sum(comb(element1, element2))로 result list에 추가하여 풀이

# 변수 선언
# numbers : input :: list
# result : output :: list


# 입출력 예
# numbers	result
# [2,1,3,4,1]	[2,3,4,5,6,7]
# [5,0,2,7]	[2,5,7,9,12]

from itertools import permutations


def solution(numbers):
    result = list(permutations(numbers,2))
    result_set = set(sum(i) for i in result)
    return sorted(list(result_set))

print(solution([2,1,3,4,1]))

# 문제점
# TypeError: Object of type set is not JSON serializable
# VS CODE에서는 문제없이 돌아가는 코드가 프로그램머스에서는 작동이 안되는 일이 발생
# set을 사용해서 그런것 같다
# set을 변수선언해서 해결