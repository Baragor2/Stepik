'''
Вводятся три строчки стихотворения (каждая с новой строки).
Сохранить его в виде вложенного списка с разбивкой по строкам и словам (слова разделяются пробелом).
Результирующий список lst вывести на экран командой:
print(lst)
'''


# put your python code here
lst1 = list(input().split())
lst2 = list(input().split())
lst3 = list(input().split())
lst = lst1, lst2, lst3
print(list(lst))

