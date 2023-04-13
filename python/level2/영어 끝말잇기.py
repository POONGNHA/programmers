# 문제 설명
# 1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.
# 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
# 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 이전에 등장했던 단어는 사용할 수 없습니다.
# 한 글자인 단어는 인정되지 않습니다.
# 다음은 3명이 끝말잇기를 하는 상황을 나타냅니다.

# tank → kick → know → wheel → land → dream → mother → robot → tank

# 위 끝말잇기는 다음과 같이 진행됩니다.
# 1번 사람이 자신의 첫 번째 차례에 tank를 말합니다.
# 2번 사람이 자신의 첫 번째 차례에 kick을 말합니다.
# 3번 사람이 자신의 첫 번째 차례에 know를 말합니다.
# 1번 사람이 자신의 두 번째 차례에 wheel을 말합니다.
# (계속 진행)
# 끝말잇기를 계속 진행해 나가다 보면, 3번 사람이 자신의 세 번째 차례에 말한 tank 라는 단어는 이전에 등장했던 단어이므로 탈락하게 됩니다.
# 사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.
# 끝말잇기에 참여하는 사람의 수 n은 2 이상 10 이하의 자연수입니다.
# words는 끝말잇기에 사용한 단어들이 순서대로 들어있는 배열이며, 길이는 n 이상 100 이하입니다.
# 단어의 길이는 2 이상 50 이하입니다.
# 모든 단어는 알파벳 소문자로만 이루어져 있습니다.
# 끝말잇기에 사용되는 단어의 뜻(의미)은 신경 쓰지 않으셔도 됩니다.
# 정답은 [ 번호, 차례 ] 형태로 return 해주세요.
# 만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return 해주세요.

# 풀이 유추
# result는 [m번째 사람, 시행횟수]를 리턴한다
# 1. words의 원소의 마지막과 그다음 첫번째 원소의 시작char가 같은지 비교한다.
# 같다면 그 0부터 그 element까지 length를 n으로 나눈 몫+1 을 result[1]에 나머지를 result[0]으로 return 한다.
# 2. set을 만들어서 길이를 비교한 뒤 다르다면 0번째에서부터 count(i)가 2 이상인 원소를 찾아서 return한다.
# 3. 탈락자가 나오지 않는다면 [0,0]을 return 한다

# 변수선언
# input : n, words :: int, list
# set :: 중복비교
# output : result :: list 

def solution(n, words):
    # 중복여부 판정
    if len(set(words)) == len(words):
        # 끝말잇기가 되는지 확인
        stack = []
        for idx in range(0,len(words)):
            stack.append(words[idx])
            if idx != 0 and stack[-2][-1] != words[idx][0] :
                return [idx%n+1, len(words[:idx])//n +1 ]
            # 탈락자가 없으면
        
    # 중복이 있다면
    else :
        stack = []
        for idx in range(0, len(words)):
            stack.append(words[idx])
            if stack.count(words[idx]) >= 2 :
                return [idx%n +1, len(stack)//n ]
    
    return [0,0]

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))