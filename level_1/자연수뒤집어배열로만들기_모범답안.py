def digit_reverse(n):
    return list(map(int, reversed(str(n))))

# reversed()는 리턴값이 비어있기 때문에 list(reversed(a))식으로 처리해주었다.