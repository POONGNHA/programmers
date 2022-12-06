strings = ["sun", "bed", "car"]
n = 1
dict_with_index = {idx:string for idx,string in enumerate(strings)}
dict_sorted = sorted(dict_with_index.items(), key = lambda idx : idx[1][n:])
print(dict_sorted)