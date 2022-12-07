# 문제 설명
# 가위는 2 바위는 0 보는 5로 표현합니다.
# 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때,
# rsp에 저장된 가위 바위 보를 모두 이기는 경우를
# 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.
# 0 < rsp의 길이 ≤ 100
# rsp와 길이가 같은 문자열을 return 합니다.
# rsp는 숫자 0, 2, 5로 이루어져 있습니다.

# 풀이유추
# rsp를 list로 받음
# 0 2 5
# 5 0 2
# dict 생성
# key값을 받으면 value 값을 result str에 붙여서 리턴

# 변수선언
# input : string : rsp
# rsp_list : list : tranform rsp to list
# trans_dic : dictionary : { 0 : 5 , 2 : 0, 5 : 2 }
# result_str : string :

# 테스트케이스
# rsp	result
# "2"	"0"
# "205"	"052"

def solution(rsp):
    rsp_list = list(rsp)
    trans_dic = { "0" : '5' , '2' : '0', '5' : '2' }
    result_str = ""
    for i in rsp_list:
        result_str += trans_dic[i]
    return result_str