n = 12345;
a = list();
NumStr = str(n);
for i in range(0, len(NumStr)):
    a.append(int(NumStr[i]));
print(list(reversed(a)));