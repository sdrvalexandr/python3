import random
import math
    
def fillArray() -> list:
    number = int(input('Введите длину массива: '))
    min = int(input('Введите минимальное число рандомайзера: '))
    max = int(input('Введите максимальное число рандомайзера: '))
    list = []
    for i in range(number):
        list.append(random.randint(min, max))
    print('array: ',list)
    return list

def fillDecimalArray() -> list:
    number = int(input('Введите длину массива: '))
    min = int(input('Введите минимальное число рандомайзера: '))
    max = int(input('Введите максимальное число рандомайзера: '))
    list = []
    for i in range(number):
        list.append(round(random.uniform(min, max), 2))
    print('array: ',list)
    return list

def ex1(array):
    sum = 0
    for i in range(len(array)):
        if i % 2 != 0:
            sum = sum + array[i]
    print('SUM: ', sum)

def ex2(array):
    list = []
    lenghtArray = len(array)
    i = 0
    j = lenghtArray
    while i < lenghtArray/2 and lenghtArray - 1 > lenghtArray/2:
        j = j - 1
        sum = array[i] * array[j]
        list.append(sum)
        i += 1
    print('SUM: ', list)

def ex3(array):
    list = []
    for i in range(len(array)):
        a = array[i] % 1
        list.append(round(array[i] % 1, 2))
    print('LIST: ',list)
    print('max', max(list))
    print('min', min(list))
    print('Разница между максимальным и минимальным значением дробной части: ', round(max(list)-min(list),2))
    
def ex4(number):
    numberb = ''
    while number > 0:
        numberb = str(number % 2) + numberb
        number = number // 2
    print(numberb)

def ex5(number):
    list = []
    for i in range(number):
        if i == 0 or i == 1:
            list.append(i)
        else:
            list.append((i-1)+(i-2))
    print('LIST: ',list)

def fib(number):
    list = []
    list3 = []
    list4 = []
    sqrt5 = math.sqrt(5)
    for i in range(number):
        phibo = (sqrt5 + 1) / 2
        a = phibo ** i /sqrt5 + 0.5
        list.append(int(a))
        list3.append(int(-a))
    list4 = list + list3
    list4.sort()
    print(list4)


print('1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')
ex1(fillArray())
print('2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')
ex2(fillArray())
print('3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части')
ex3(fillDecimalArray())
print('4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.')
number = int(input('Введите число: '))
ex4(number)
print('5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов')
number = int(input('Введите число: '))
fib(number)