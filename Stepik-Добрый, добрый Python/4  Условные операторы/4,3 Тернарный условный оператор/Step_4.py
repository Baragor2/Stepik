'''
Вводится целое число 0 или 1. Необходимо преобразовать их в строки: 0 - в "False", 1 - в "True".
Реализовать это с помощью тернарного условного оператора. Результат отобразить на экране.
'''


# put your python code here
num = int(input())
msg = 'True' if num == 1 else 'False'
print(msg)
