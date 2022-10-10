def sum_digit(number):
    if number < 10:             # 계산 다 끝나면 마지막에 숫자 넘기기
        return number;
    return (number % 10) + sum_digit(number // 10)
    # 10으로 나눈 나머지 + 10으로 된 몫(재귀)
    # 결과적으로 나머지(즉 1의자리) + 그다음 나머지(10의자리) + 그다음..... 마지막까지 가면 그냥 +number

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));