def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))

# 리스트를 하나 더 만들어서 그 리스트에 처리함 이게 더 효율적인듯