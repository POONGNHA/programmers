# 2016년
# 문제 설명
# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 
# 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
# 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT
# 입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.
# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. 
# (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

# 풀이 유추
# 1~12월까지 dict생성
# key는 달, value는 일수를 적음
# a월 b일까지의 일수를 계산하고 남은 날짜에 7로 나누어 나머지를 리턴함.

# 변수 선언
# input : a b :: int
# remainDay_dict : dict 
# DayOfTheWeek_dict : dict
# output : result :: String

# 입출력 예
# a	b	result
# 5	24	"TUE"

# 풀이
def solution(a,b):
    result = 0
    DayOfTheWeek_dict = {3:"SUN",4:"MON",5:"TUE",6:"WED",7:"THU",1:"FRI",2:"SAT"}
    remainDay_dict = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    for month in range(1,a): 
        result += remainDay_dict[month]
    return DayOfTheWeek_dict[(result + b) % 7]

print(solution(5,24))