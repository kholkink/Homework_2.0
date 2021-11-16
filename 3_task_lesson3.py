from random import randint
def get_jokes(iter):
	nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
	adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
	adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
	mass = []
	for i in range(iter):
		noun = nouns[randint(0, 4)]
		adv = adverbs[randint(0, 4)]
		adj = adjectives[randint(0, 4)]
		mass.append(noun + " " + adv + " " + adj)
	return mass
print(get_jokes(2))
