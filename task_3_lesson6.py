import csv
from itertools import zip_longest
with open('hobby.csv', encoding="utf-8") as hobby:
	hobbies = csv.reader(hobby, delimiter=',', quotechar='|')
	mass_hobby = []
	for line in hobbies:
		for el in line:
			mass_hobby.append(el)
with open('users.csv', encoding="utf-8") as users:
	users = csv.reader(users, delimiter=',', quotechar='|')
	mass_users = []
	for line in users:
		for el in line:
			mass_users.append(el)
full_mass = []
with open('result.txt', 'w', encoding="utf-8") as result:
	for user, hobby in zip_longest(mass_users, mass_hobby):
		if user == None:
			print(1)
			break
		else:
			if hobby == None:
				result.write(user + " ")
				result.write('None' + '\n')
			else:
				result.write(user + " ")
				result.write(hobby + '\n')
			full_mass.append((user, hobby))


print(full_mass)
