'''
Вводится слово. Необходимо первую букву этого слова сделать заглавной, а остальные - малыми.
Результат отобразить на экране.
'''


# put your python code here
s1 = input()
print(s1[0].upper() + s1[1:].lower())

