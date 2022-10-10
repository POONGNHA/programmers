n = 142939;
# for i in range(0,len(str(n))):

print(''.join(sorted([str(n)[i] for i in range(0,len(str(n)))],reverse=True)));