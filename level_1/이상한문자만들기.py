# 문제 설명
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
# 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# 각 단어의 짝수번째 알파벳은 대문자로,
# 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수,
# solution을 완성하세요.
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

#풀이유추
# split, upper, lower 사용
# s를

# 테스트케이스
# s	return
# "try hello world"	"TrY HeLlO WoRlD"

def solution(s):
    list_spl = s.split()
    result_str = ""
    for i in list_spl:
        for j in range(0, len(i)):
            if j % 2 == 0 or j == 0:
                result_str += i[j].upper()
            else:
                result_str += i[j].lower()
        result_str += " "
    return result_str



print(solution("try hello world"))

