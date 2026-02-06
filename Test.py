from functools import reduce
all_the_same = [1]
result = reduce(lambda x, y: x == y, all_the_same)
print(result)