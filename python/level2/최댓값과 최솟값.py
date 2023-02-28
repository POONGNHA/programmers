# 문제 설명
# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
# str에 나타나는 숫자 중 최소값과 최대값을 찾아 
# 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
# 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, 
# "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
# s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

# 풀이 유추
# list(string)형태로 나누고 
# 최소최대 리턴
# !음수일때 내장함수 min() max()가 동작하지 않는다!

# 변수
# s : String : input
# MMlist (min max list) : List 


# 테스트 케이스
# s	return
# "1 2 3 4"	"1 4"
# "-1 -2 -3 -4"	"-4 -1"
# "-1 -1"	"-1 -1"

def solution(s):
    MMList = s.split(" ")
    CompareMinusList = []
    for i in MMList:
        CompareMinusList.append(int(i))
    return str(min(CompareMinusList))+ " " + str(max(CompareMinusList))

print(solution("-1 -2 -3 -4"))

# 막힌 부분
# 음수일때 min과 max 내장함수가 작동하지 않는다.

# 개선할점
# map을 사용해서 map(int,s.spint()) 이런식으로 하면 코드가 훨씬 간결했을것이다.