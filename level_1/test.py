# def solution(ingredient):
#     answer = 0
#     return answer




def solution(ingredient):
    burger = [1, 2, 3, 1]
    cnt = 0
    flag = True
    # 버거를 만들고 가운데가 빠지면 앞에거랑 다시 버거를 만들수 있어야함

    if len(ingredient) < 4 :
        return 0
    else:
        while flag:
            flag = False
            for i in range(0, len(ingredient)-3):
                if ingredient[i:i+4] == burger: # 0, 1, 2, 3,
                    del ingredient[i:i+4]
                    flag = True
                    cnt += 1
                    break
    return cnt

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
