def solution(array):
    a = list()
    for i in array:
        a.append(array.count(i))
    if max(a) == a.count(max(a)):
        return max(a)
    else:
        return -1
