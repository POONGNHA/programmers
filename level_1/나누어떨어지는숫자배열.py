def solution(arr, divisor):
    result = list();
    for i in range(0,len(arr)) :
        if arr[i] % divisor == 0:
            result.append(arr[i])
    if result == [] :
        return [-1]
    else :
        return sorted(result)