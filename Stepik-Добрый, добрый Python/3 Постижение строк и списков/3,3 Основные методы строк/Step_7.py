'''
Вводится строка (слаг). Замените в этой строке все двойные дефисы (--) и тройные (---) на одинарные (-).
Подумайте, в какой последовательности следует выполнять эти замены.
Результат преобразования выведите на экран.
'''


# put your python code here
s1 = input()
s1 = s1.replace('---', '-')
print(s1.replace('--', '-'))
