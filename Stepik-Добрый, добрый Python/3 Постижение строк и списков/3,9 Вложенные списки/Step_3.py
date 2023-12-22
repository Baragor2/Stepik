'''
Вводится  матрица чисел из трех строк. В каждой строке числа разделяются пробелом.
Необходимо вывести на экран последний столбец этой матрицы в виде строки из трех чисел через пробел.
'''


# put your python code here
lst = []
lst.append(input().split())
lst.append(input().split())
lst.append(input().split())
print(lst[0][-1], lst[1][-1], lst[2][-1])