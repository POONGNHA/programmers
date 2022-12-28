# 숫자 짝꿍
# 문제 설명
# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 
# 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다
# (단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). 
# X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. 
# X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

# 예를 들어, X = 3403이고 Y = 13203이라면, 
# X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 
# 다른 예시로 X = 5525이고 Y = 1255이면 
# X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다
# (X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
# 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.

# 3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
# X, Y는 0으로 시작하지 않습니다.
# X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.

# 풀이 유추
# X,Y를 list로 만들고
# count()를 사용해서 확인해서 없다면 -1 리턴
# 겹치는 숫자를 return list에 추가
# reverse sort하고 string으로 형변환해서 return

# 변수선언
# X, Y : input : String
# X_list, Y_list : list
# result_list : list
# output : String

# 입출력 예
# X	Y	result
# "100"	"2345"	"-1"
# "100"	"203045"	"0"
# "100"	"123450"	"10"
# "12321"	"42531"	"321"
# "5525"	"1255"	"552"

# sol
def solution(X,Y):
    X_list = list(X)
    Y_list = list(Y)
    result_list = []
    
    for i in X_list:
        for j in range(0,len(Y_list)):
            if i == Y_list[j]:
                result_list.append(i)
                Y_list.pop(j)
                break
    if not result_list:
        return "-1"
    if sum(map(int,result_list)) == 0:
        return "0"
    else:
        result_list.sort(reverse=True)
        return "".join(result_list)
        
print(solution("100","203045"))
            
            
# 개선점
# 1. 한번 센 숫자는 제외시켜야 했는데 하지 않았다.
# 2. 0만 들어가있는 list를 구분하는 조건식은 무엇인가?
# 3. return type은 숫자로 써져있어도 String이다
# 4. TestCase의 시간초과 발생
# 어차피 숫자는 1~9까지만 존재하니까, 
# 2중 for문을 사용하는것보다
# count()로 하나씩 넣는게 훨씬 빠를듯
