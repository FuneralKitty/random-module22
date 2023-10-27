import random

#seed  При запуске программы результат изменяться не будет (нужно указать начальное числовое значение).
# т.е оно всегда будет статичным пока не изменим параметр вызова этой функции и будет влиять на весь рандом
#random.seed(1)


#random рандомное вещественное число от 0 до 1
print(random.random())


#sample перетасовка списка,обязательный параметр k - регулирует длину списка
lst =[1,23,512,123,678]
print(random.sample(lst,4))


#UNIFORM случайное вещественное число в диапазоне
print(random.uniform(1,10))


#randint случайное целое число от а до б
print(random.randint(1,15))


#randrange случайное целое число в промежутке(start,stop,step)
print(random.randrange(1,12,2))


#gauss вещественное число по Гауссу
print(random.gauss(1,2,))


#shuffle перемешивает элементы случайным образом
a = random.shuffle(lst)
print(lst)


#choice возвращает случайный элемент заданной последовательности
print(random.choice(lst))

