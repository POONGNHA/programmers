# [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]





# arr3 = [1, 2]
# arr4 = [2, 3]
# print(*[x for x in zip(arr1,arr2)])      # result = [(1, 2), (2, 3)]
# print([a+b for a,b in zip(arr3,arr4)])  # result = [3, 5]
# print([[x+y for x, y in zip(a,b)] for a, b in zip(arr1,arr2)])

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

print([x for x in zip(arr1, arr2)])                         # [([1, 2], [3, 4]), ([2, 3], [5, 6])]
print(*[x for x in zip(arr1, arr2)])                        # ([1, 2], [3, 4]) ([2, 3], [5, 6])
print([list(map(sum, zip(*x))) for x in zip(arr1, arr2)])   # [[4, 6], [7, 9]]