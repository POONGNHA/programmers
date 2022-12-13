# 문자열 밀기
# 문제 설명
# 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 
# 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 
# 이것을 문자열을 민다고 정의한다면 
# 문자열 A와 B가 매개변수로 주어질 때, 
# A를 밀어서 B가 될 수 있다면 몇 번 밀어야 하는지 횟수를 return하고 
# 밀어서 B가 될 수 없으면 -1을 return 하도록 
# solution 함수를 완성해보세요.
# 0 < A의 길이 = B의 길이 < 100
# A, B는 알파벳 소문자로 이루어져 있습니다.

# 풀이유추
# 미는것은 slice를 이용해서 밀면 되고
# 판별은 글자수의 len만큼 반복시행했을때 없으면 -1 return 하면 될듯

# 변수선언
# input : A, B: String :
# tempStr : String
# output : result

# 입출력 예
# A	B	result
# "hello"	"ohell"	1
# "apple"	"elppa"	-1

# 풀이
def solution(A,B):
    for i in range(0,len(A)+1):
        if A == B:
            return 0
        tempStr = ""
        tempStr = A[-1]
        tempStr += A[:-1]
        if tempStr == B:
            return i + 1
        A = tempStr
    return -1

print(solution("hello","elloh"))

# 개선점
# A과 B와 같을때를 생각하지 못했다.