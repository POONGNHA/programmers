# 문제 설명
# 스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.
# 이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 
# 숫자만을 입력하려고 합니다.
# 맨 처음 왼손 엄지손가락은 * 
# 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 
# 엄지손가락을 사용하는 규칙은 다음과 같습니다.

# 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 
# 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 
# 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
# 4-1. 만약 두 엄지손가락의 거리가 같다면, 
# 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
# 순서대로 누를 번호가 담긴 배열 numbers, 
# 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
# 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 
# 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
# numbers 배열의 크기는 1 이상 1,000 이하입니다.
# numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
# hand는 "left" 또는 "right" 입니다.
# "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
# 왼손 엄지손가락을 사용한 경우는 L, 
# 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 
# 문자열 형태로 return 해주세요.

# 풀이 유추
# 1,4,7과 3,6,9는 바로 L과 R출력
# 2,5,8,0은 가까운 손가락을 사용한다는 제한이 있다.
# 가까운 손가락이란 조건을 만족시키려면 왼손과 오른손의 위치를 가늠해야한다.
# 번호별로 x,y위치를 저장시킨 dict를 생성
# position_L, position_R이라는 변수에 최근위치 저장
# abs 함수를 사용해서 거리를 계산하고 거리가 같으면 ~잡이를 기준으로 판단

# 변수선언
# input : numbers, hand 
# Num_dict : dict : key = 번호 : value = 좌표 list [x,y]
# positionL, positionR : 왼손과 오른손 번호 저장
# output : result

# 테스트케이스
# numbers	hand	result
# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"

def solution(nubmers, hand):
    #변수선언
    #하드코딩 dict
    NumGridDict = {0:[1,0],1:[0,3],2:[1,3],3:[2,3],4:[0,2],5:[1,2],6:[2,2],7:[0,1],8:[1,1],9:[2,1]}
    positionL = [0,0]
    positionR = [2,0]
    resultStr = ""
    
    # 버튼을 눌렀을때
    for i in nubmers:
        if i % 3 == 1:
            positionL = NumGridDict[i]
            resultStr += "L"
        elif i % 3 == 0 and i != 0:
            positionR = NumGridDict[i]
            resultStr += "R"
        elif i % 3 == 2 or i == 0:
            if abs(positionL[0] - NumGridDict[i][0]) + abs(positionL[1] - NumGridDict[i][1]) > abs(positionR[0] - NumGridDict[i][0]) + abs(positionR[1] - NumGridDict[i][1]):
                positionR = NumGridDict[i]  
                resultStr += "R"
            elif abs(positionL[0] - NumGridDict[i][0]) + abs(positionL[1] - NumGridDict[i][1]) < abs(positionR[0] - NumGridDict[i][0]) + abs(positionR[1] - NumGridDict[i][1]):
                positionL = NumGridDict[i]
                resultStr += "L"
            else:
                if hand == "right":
                    positionR = NumGridDict[i]  
                    resultStr += "R"
                else:
                    positionL = NumGridDict[i]
                    resultStr += "L"
    return resultStr

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))                    
                
# 개선점
# 문제의 *과 #도 처음의 dict에 다 넣어버리면 더 좋았을것같다.                