# def solution(ingredient):
#     answer = 0
#     return answer




def solution(ingredient):
    burger = [1, 2, 3, 1]
    cnt = 0
    if len(ingredient) < 4 :
        return 0
    else:
        for i in range(0, len(ingredient)-3):
            if ingredient[i:i+4] == burger: # 0, 1, 2, 3,
                cnt += 1
        return cnt

print(solution([1,2,3,1]))
