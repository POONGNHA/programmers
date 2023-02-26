# 짝지어 제거하기
# 문제 설명
# 짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 
# 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 
# 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 
# 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 
# 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 
# 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.
# 예를 들어, 문자열 S = baabaa 라면
# b aa baa → bb aa → aa →
# 의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

# 제한사항
# 문자열의 길이 : 1,000,000이하의 자연수
# 문자열은 모두 소문자로 이루어져 있습니다.

# 풀이유추
# 2개 붙어있는 글자처리
# 1. while문으로 1번째 글자부터
# count로 짝수인것을 확인하고
# 뒤에 글자가 연속해있는지 확인한다.
# 연속이라면 뒤에 2개의 글자를 없애고 그 뒤부터 다시 시작한다.
# 끝나고도 글자가 남아있다면 0을 return한다.

# 변수선언
# input : s :: String
# stack : list
# output : result :: int

# 입출력 예
# s	result
# baabaa	1
# cdcd	0

# 풀이
def solution(s):
    # 원소의 갯수가 짝수인지 체크
    for element in set(list(s)):
        if s.count(element) % 2 != 0:
            return 0
    
    # Stack을 이용해서 풀이
    stack = list()
    for s_element in s:
        stack.append(s_element)
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    
    # s가 텅 비어있다면
    if stack:
        return 0
    else:
        return 1
            
print(solution("baabaa"))

# 개선점
# 테스트케이스 3,4,5번 통과 실패
# 시간 테스트 2,3,4,5번 통과 실패
# 알고리즘 개선이 필요하다.

# 1번째 풀이 ----------------------------
# for element in set(list(s)):
#     if s.count(element) % 2 != 0:
#         return 0

# # 원소 체크
# idx = 0
# while(not(idx == 0 and idx == len(s) or idx == len(s)-1)):
#     s = list(s)
#     if s[idx] == s[idx+1]:
#         s.pop(idx)
#         s.pop(idx)
#         if idx != 0:
#             idx -= 1
#     else:
#         idx += 1
# "".join(s)
# # s가 텅 비어있다면
# if s:
#     return 0
# else:
#     return 1

# Stack을 이용해서 간단하게 풀었다.
