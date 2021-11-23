from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
def gen1(tutors, klasses):
     for i in zip_longest(tutors, klasses):
        if i[0] is not None:
            yield i
gen = gen1(tutors, klasses)
for i in gen:
    print(i)
