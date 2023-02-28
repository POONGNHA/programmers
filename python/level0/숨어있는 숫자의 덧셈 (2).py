# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다.
# my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
# 1 ≤ my_string의 길이 ≤ 1,000
# 1 ≤ my_string 안의 자연수 ≤ 1000
# 연속된 수는 하나의 숫자로 간주합니다.
# 000123과 같이 0이 선행하는 경우는 없습니다.
# 문자열에 자연수가 없는 경우 0을 return 해주세요.

# 풀이유추
# 문자열 안에 숫자만 추출해야 최선
# 어떻게 숫자만 알아볼것인가? isdigit 함수 사용
# 붙어있는 숫자는 어떻게 처리할것인가?

# 테스트케이스
#  my_string	result
# "aAb1B2cC34oOp"	37
# "1a2b3c4d123Z"	133

#풀이
def solution(my_string):
    list_str = list(my_string)
    result = ""
    for i in list_str:
        if i.isdigit():
            result += i
        else:
            result += " "
    return sum(map(int,result.strip().split()))

print(solution("aAb1B2cC34oOp"))

