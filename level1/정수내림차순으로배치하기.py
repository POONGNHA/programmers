n = 142939;
# for i in range(0,len(str(n))):
print(''.join(sorted([str(n)[i] for i in range(0,len(str(n)))],reverse=True)));

# sorted를 사용하면 iterator 기능이 되어 하나씩 튀어나옴