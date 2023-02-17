# 문제 설명
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다.
# 예를 들어
# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 
# 문자열 s가 올바른 괄호이면 true를 return 하고, 
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

# 풀이 유추
# find() 함수를 사용하면 되지 않을까
# 기본적으로 ()를 찾으면 없애서 최종적으로 ""가 되어야 true를 반환할수 있다.

# 변수선언
# input : s :: String
# output : answer :: String

# 입출력 예
# s	answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false

# 풀이
def solution(s):
    while("()" in s):
        s = s.replace("()","")
    if s:
        return False
    else:
        return True
    

print(solution("(())()"))

# 개선점
# def solution(s):
#     while("()" in s):
#         s = s.replace("()","")
#     if s:
#         return False
#     else:
#         return True
# 효율성테스트에서 실패로 나왔다.
# 더 효율적으로 구하는 방법이 있을까?
