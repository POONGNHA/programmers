def digit_reverse(n):
    return list(map(int, reversed(str(n))));

# reversed()는 리턴값이 비어있기 때문에 list(reversed(a))식으로 처리해주었다.
# map은 (1,2) 가 있는데 1에 함수, 2에 원하는 값을 넣는다.
# n = 12345 일때
# str(n) = "12345"
#