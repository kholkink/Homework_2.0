def num_translate_adv(str_num):
	if str_num.lower() == 'один' and str_num[0] == "О":
		return 'One'
	elif str_num.lower() == 'один' and str_num[0] == 'о':
		return 'one'
	else:
		pass
	if str_num.lower() == 'два' and str_num[0] == "Д":
		return 'Two'
	elif str_num.lower() == 'два' and str_num[0] == 'д':
		return 'two'
	else:
		pass
	if str_num.lower() == 'три' and str_num[0] == "Т":
		return 'Three'
	elif str_num.lower() == 'три' and str_num[0] == 'т':
		return 'three'
	else:
		pass
	if str_num.lower() == 'четыре' and str_num[0] == "Ч":
		return 'Four'
	elif str_num.lower() == 'четыре' and str_num[0] == 'Ч':
		return 'four'
	else:
		pass
	if str_num.lower() == 'пять' and str_num[0] == "П":
		return 'Пять'
	elif str_num.lower() == 'пять' and str_num[0] == 'п':
		return 'пять'
	else:
		pass
	if str_num.lower() == 'шесть' and str_num[0] == "Ш":
		return 'Six'
	elif str_num.lower() == 'шесть' and str_num[0] == 'ш':
		return 'six'
	else:
		pass
	if str_num.lower() == 'семь' and str_num[0] == "С":
		return 'Seven'
	elif str_num.lower() == 'семь' and str_num[0] == 'с':
		return 'seven'
	else:
		pass
	if str_num.lower() == 'восемь' and str_num[0] == "В":
		return 'Eigth'
	elif str_num.lower() == 'восемь' and str_num[0] == 'в':
		return 'eigth'
	else:
		pass
	if str_num.lower() == 'девять' and str_num[0] == "Д":
		return 'Nine'
	elif str_num.lower() == 'девять' and str_num[0] == 'д':
		return 'nine'
	else:
		pass
print(num_translate_adv('Девять'))
