def some_generator(src):
	for i in range(0, len(src)):
		if src[i] not in src[:i-1] and src[i] not in src[i+1:]:
			if i+1 == len(src):
				yield src[i]
			else:
				if src[i] != src[i+1] and src[i] != src[i-1]:
					yield src[i]
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = some_generator(src)
for i in result:
	print(i)