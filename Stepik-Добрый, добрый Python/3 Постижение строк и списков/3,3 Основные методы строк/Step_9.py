'''
Вводится строка, состоящая из слов, разделенных пробелом.
Необходимо подсчитать число слов в этой строке и результат (число) отобразить на экране.
'''


# put your python code here
s1 = input()
s1 = s1.rstrip().lstrip()
print(s1.count(' ') + 1)
