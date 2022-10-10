num = 6
cnt = 0;
for i in range(1,501):
    if num % 2 == 0:
        num = num / 2;
    elif num % 2 == 1:
        num = num * 3 + 1;

    if i == 500:
        print(-1);
    elif num == 1 :
        print(i);
        break;