arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

# for i in range(0, len(arr1)):

# print([[x + y for x, y in zip(arr1[0] , arr2[0])], [a + b for a, b in zip(arr1[1], arr2[1])]])

arr3 = list()
for i in range(0, len(arr1)):
    arr3.append([x + y for x, y in zip(arr1[i] , arr2[i])])

# print(arr3)
return arr3
