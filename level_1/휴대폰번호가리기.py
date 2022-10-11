def solution(phone_number):
    result = list();
    for i in range(0,len(phone_number)-4):
        result.append("*");
    return ''.join(str(i) for i in (result + list(map(int,phone_number))[-4:]))