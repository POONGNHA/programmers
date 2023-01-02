# 문제 설명
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 
# 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. 
# "z"는 1만큼 밀면 "a"가 됩니다. 
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, 
# solution을 완성해 보세요.

# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.

# 풀이 유추
# ascii 97~122번까지가 알파벳의 모음 chr(), ord() 함수 사용
# 대소문자 구분 처리 -> ord()로 index를 뽑고, n만큼 더해준다. 
# 65~91번까지가 대문자, 97~122번까지가 소문자 알파벳으로 이루어져있다.
# 상식 : 알파벳은 26글자로 이루어져있다.


# 변수 선언
# input : s, n : String, int
# sList : list
# output : result : String


# 입출력 예
# s	n	result
# "AB"	1	"BC"
# "z"	1	"a"
# "a B z"	4	"e F d"

# 풀이
def solution(s,n):
    sList = list(s)
    result = ""
    for i in sList:
        if ord(i) == 32 :
            result += " "
        elif ord(i) < 92 :
            result += chr( 65 + ((ord(i)+n)%65)%26 )
        elif ord(i) > 96 :
            result += chr( 97 + ((ord(i)+n)%97)%26 )
    return result
    
    
print(solution("AB"	,1))