'''
Вводятся три целых числа в одну строку через пробел. Необходимо определить наименьшее среди них и вывести его на экран.
Реализовать программу, используя условный оператор, без использования функции min.
'''


# put your python code here
num1, num2, num3 = map(int, input().split())
if num1 < num2:
    if num1 < num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 < num3:
        print(num2)
    else:
        print(num3)
