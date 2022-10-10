n = 482;
a = list();
for i in range(10, 0, -1):
    if n - (10 ** (i - 1)) >= 0:
        num = n // 10 ** (i - 1);
        NumStr = str(num);
        a.append(int(NumStr[-1]));
print(sum(a));
