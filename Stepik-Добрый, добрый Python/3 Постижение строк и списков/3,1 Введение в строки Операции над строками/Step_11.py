'''
С клавиатуры вводятся две буквы (в одну строку через пробел). Вывести на экран следующую строку:
"Коды: <буква1> = <код буквы1>, <буква2> = <код буквы2>"
'''


# put your python code here
letter1, letter2 = input().split()
print(f'Коды: {letter1} = {ord(letter1)}, {letter2} = {ord(letter2)}')