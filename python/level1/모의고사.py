# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 
# 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# 가장 많은 문제를 맞힌 사람이 누구인지 
# 배열에 담아 return 하도록 solution 함수를 작성해주세요.
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, 
# return하는 값을 오름차순 정렬해주세요.

# 풀이 유추
# 1번 수포자 : [1, 2, 3, 4, 5] 5개
# 2번 수포자 : [2, 1, 2, 3, 2, 4, 2, 5] 8개
# 3번 수포자 : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 10개
# answers를 받으면 answer의 길이보다 크게 수포자들의 답변을 더함
# [:]로 answers의 길이와 같게 수포자들의 답변의 길이를 맞춤
# 수포자들의 답변을 answers와 비교해서 같으면 1로, 다르면 0으로 바꿈
# return list에 append로 제일 높은 배열의 합을 가진 수포자를 추가해주고 return한다

# 변수선언
# input : answers : list
# student1 = [1, 2, 3, 4, 5]
# student2 : [2, 1, 2, 3, 2, 4, 2, 5]
# student3 : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
# stu1_len : list
# stu2_len : list
# stu3_len : list
# stu1_score : int
# stu2_score : int
# stu3_score : int
# output : result : list

# 입출력 예
# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

# 풀이
def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    temp1 = []
    temp2 = []
    temp3 = []
    stu1_score = 0
    stu2_score = 0
    stu3_score = 0
    resultList = []
    
    for i in range(0,(len(answers)//len(student1))+1):
        temp1 += student1
    for i in range(0,(len(answers)//len(student2))+1):
        temp2 += student2
    for i in range(0,(len(answers)//len(student3))+1):
        temp3 += student3

    stu1_len = temp1[:len(answers)]
    stu2_len = temp2[:len(answers)]
    stu3_len = temp3[:len(answers)]
    
    for i in range(0,len(answers)):
        if answers[i] == stu1_len[i]:
            stu1_score += 1
        if answers[i] == stu2_len[i]:
            stu2_score += 1
        if answers[i] == stu3_len[i]:
            stu3_score += 1
    
    if max([stu1_score, stu2_score, stu3_score]) == stu1_score:
        resultList.append(1)
    if max([stu1_score, stu2_score, stu3_score]) == stu2_score:
        resultList.append(2)
    if max([stu1_score, stu2_score, stu3_score]) == stu3_score:
        resultList.append(3)
    return resultList
    
print(solution([1,3,2,4,2]))