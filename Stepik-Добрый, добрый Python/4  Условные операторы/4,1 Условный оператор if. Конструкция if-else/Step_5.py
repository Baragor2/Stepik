'''
Вводится четырехзначное число. Проверить, что оно оканчивается на цифру 7.
Вывести на экран ДА, если это так и НЕТ - в противном случае.
'''


# put your python code here
a = input()
if a[-1] == '7':
    print("ДА")
else:
    print("НЕТ")

