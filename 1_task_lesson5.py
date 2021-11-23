def odd_nums(n):
	for i in range(1, n+1, 2):
		yield i
odd_num_1 = odd_nums(15)
print(next(odd_num_1))
print(next(odd_num_1))
print(next(odd_num_1))
print(next(odd_num_1))
print(next(odd_num_1))
print(next(odd_num_1))
print(next(odd_num_1))
print(next(odd_num_1))
print(next(odd_num_1))
print(next(odd_num_1))