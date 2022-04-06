#BY THEDMITRYX


import random
import time


reshenie=['Разумеется да', 'Наверное нет', 'Не проверял',
          'Конечно нет', 'Может быть', 'Я не знаю', 'Нет', 'Да',
          'Еще не знаю']


dopinfo=['PyBen думает...', 'PyBen размышляет...',
        'PyBen использует рандомайзер...', 'PyBen придумывает ответ...',
        'PyBen советуется с друзьями...', 'PyBen пытается соврать...',
        'PyBen расшифровывает вопрос...']


print("Привет! Давай познакомимся!")
time.sleep(1)
print("Меня зовут PyBen, а тебя? Напиши свое имя!")
name=input()
time.sleep(1)
print("Приятно познакомиться,", name)
while True:
    time.sleep(1)
    print(" ")
    print("Задай мне любой вопрос.")
    vopros=input()
    print(" ")
    time.sleep(1)
    print(random.choice(dopinfo))
    print(" ")
    time.sleep(2)
    print(random.choice(dopinfo))
    print(" ")
    time.sleep(1)
    print("Ответ:", random.choice(reshenie))


#BY DMITRYX
