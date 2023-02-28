# 3진법 뒤집기
# 문제 설명
# 자연수 n이 매개변수로 주어집니다. 
# n을 3진법 상에서 앞뒤로 뒤집은 후, 
# 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.

# 풀이유추
# 0,1,2로 표현.
# 3으로 나누어서 결과를 출력하면 될듯
# 저번에 2진법을 풀었을때와 동일한 문제

# 변수선언
# input : n :: int 
# cnt : int
# temp_str : str
# output : result : int

# 입출력 예
# n	result
# 45	7
# 125	229

# 풀이
def solution(n):
    cnt = 0
    temp_str = ""
    while(n < (3**cnt)):
        cnt += 1
    for i in range(cnt,0,-1):
        n = 
        
        temp_str += str(n % (3 ** i))
        
        