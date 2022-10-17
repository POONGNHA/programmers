
# 1
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

# 2
def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]




arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

print([x for x in zip(arr1, arr2)])                         # [([1, 2], [3, 4]), ([2, 3], [5, 6])]
print(*[x for x in zip(arr1, arr2)])                        # ([1, 2], [3, 4]) ([2, 3], [5, 6])
print([list(map(sum, zip(*x))) for x in zip(arr1, arr2)])   # [[4, 6], [7, 9]]