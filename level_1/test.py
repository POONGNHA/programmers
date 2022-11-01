def solution(array):
    a = list()
    b = list()
    for i in array:
        a.append(array.count(i))
    for j in a:
        if j == max(a):
            b.append(array[a.index(j)])
    if set(b) == 1:
        return max(a)
    else:
        return -1





    # if
    #     return max(a)
    # else:
    #     return -1


print(solution([1, 2, 3, 3, 3, 4]))