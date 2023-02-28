def solution(x):
    totalSum = 0;
    for i in range(0,len(str(x))):
        totalSum += int(str(x)[i]);
    if x % totalSum == 0:
        return True;
    else:
        return False;