# 네오와 프로도가 숫자놀이를 하고 있습니다. 
# 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
# s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

# 숫자	영단어
# 0	zero
# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine

# 1 ≤ s의 길이 ≤ 50
# s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
# return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

# 풀이 유추
# String의 0번째 인덱스부터 차례대로 isnumeric을 사용해서 맞으면 변환, 틀리면 넘기고 숫자면 isdigit으로 넘긴다.
# result(String)에 추가한다음에 int로 형변환한다.

# 변수 선언
# input : s :: String
# output : result :: int


# 입출력 예
# s	result
# "one4seveneight"	1478
# "23four5six7"	234567
# "2three45sixseven"	234567
# "123"	123


# 풀이


def solution(s):
    numberDict = {}
    numberDict["zero"] = "0"
    numberDict["one"] = "1"
    numberDict["two"] = "2"
    numberDict["three"] = "3"
    numberDict["four"] = "4"
    numberDict["five"] = "5"
    numberDict["six"] = "6"
    numberDict["seven"] = "7"
    numberDict["eight"] = "8"
    numberDict["nine"] = "9"
    result = ""
    
    while(s):
        if s[0].isdigit():
            result += s[0]
            s = s[1:]
        else:
            for i in range(3,len(s)+1):
                if s[:i] in numberDict:
                    result += numberDict[s[:i]]
                    s = s[i:]
                    break
    return int(result)
                    
print(solution("one4seveneight"))