def digit_reverse(n):
    return list(map(int, reversed(str(n))));

# reversed()는 리턴값이 비어있기 때문에 list(reversed(a))식으로 처리해주었다.
# map은 (1,2) 가 있는데 1에 함수, 2에 원하는 값을 넣는다.
# n = 12345 일때
# str(n) = "12345"

# Q. 어떻게 string을 list로 바꾸었지???
# A. reverse와 reversed의 차이를 알면 해결됨.
# reverse는 말그대로 list를 역순으로 배열해주는 것이고
# reversed는 iterator를 통해서 string을 각각 list로 하나씩 뱉어준다.
# 즉 12345를 reversed를 하면 [5, 4, 3, 2, 1 ]이런 식으로 하나씩 뱉어준다는 것이다.
# (실제로는 list가 만들어진건 아니어서 list()함수를 사용해야함