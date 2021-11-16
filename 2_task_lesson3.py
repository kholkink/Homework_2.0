def thesaurus_adv(*args):
	dictionary = {}
	surename_letter = 0
	dictionary_test = {}
	mass = []
	num = 0
	for i in args:
		for j in enumerate(i):
			if j[1] == " ":
				surename_letter = i[j[0]+1]
				if dictionary_test.get(surename_letter) == None:
					mass.append([i])
					dictionary_test[surename_letter] = 0 + num
					num += 1
				else:
					mass[dictionary_test[surename_letter]].append(i)
	for i in enumerate(dictionary_test):
		dictionary[i[1]] = mass[i[0]]
	return dictionary



print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))