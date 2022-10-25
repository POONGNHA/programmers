def solution(arr):
    answer = []
    for i in range(0,len(arr)-1): # 0~7
        if arr[i] != arr[i+1]: # 0,1 이 같으면
            answer.append(i)
    return answer

print(solution([1,1,3,3,0,1,1]))
