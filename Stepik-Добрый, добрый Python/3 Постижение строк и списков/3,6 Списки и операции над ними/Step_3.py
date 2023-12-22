'''
Вводятся три целых числа в одну строку через пробел.
Сформируйте список lst, хранящий эти значения в порядке их ввода.
Результат выведите на экран, используя команду:
print(lst)
'''


# put your python code here
num1, num2, num3 = map(int, input().split())
lst = [num1, num2, num3]
print(lst)

