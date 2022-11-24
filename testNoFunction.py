# def solution(n):
import copy

n = 12
n_list = [i for i in range(2,n+1)]
result = []

while(True):
    compare_list = copy.deepcopy(n_list) # comparelist가 복사된다. comparelist는 소수도 다 지워버림
    if not compare_list: #compare_list가 비어있다면 중지
        break
    else:
        result.append(min(compare_list)) #
        for i in compare_list:
            if i % max(result) == 0:
                n_list.remove(i)