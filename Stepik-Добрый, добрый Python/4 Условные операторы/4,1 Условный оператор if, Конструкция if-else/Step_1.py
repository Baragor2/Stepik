"""
Вводятся два вещественных числа в одну строку через пробел. Вывести на экран наибольшее из чисел.
Задачу решить с помощью условного оператора.
"""


# put your python code here
num1, num2 = map(float, input().split())
if num1 > num2:
    print(num1)
if num2 > num1:
    print(num2)
