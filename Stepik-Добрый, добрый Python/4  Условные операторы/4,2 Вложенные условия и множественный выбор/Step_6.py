'''
Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число).
По введенным m и n (в одну строку через пробел) определить:

а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату
(в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
'''


# put your python code here
month, day = map(int, input().split())

if 2 <= day <= 27:
    if 1 <= month <= 9 and 11 <= day <= 27:
        print(f'0{month}.{day - 1} 0{month}.{day + 1}')
    elif 1 <= month <= 9 and 2 <= day <= 8:
        print(f'0{month}.0{day - 1} 0{month}.0{day + 1}')
    elif 1 <= month <= 9 and (day == 10 or day == 9):
        print(f'0{month}.0{day - 1} 0{month}.{day + 1}')
    elif 10 <= month <= 12 and 11 <= day <= 27:
        print(f'{month}.{day - 1} {month}.{day + 1}')
    elif 10 <= month <= 12 and 1 <= day <= 8:
        print(f'{month}.0{day - 1} {month}.0{day + 1}')
    elif 10 <= month <= 12 and (day == 10 or day == 9):
        print(f'{month}.0{day - 1} {month}.{day + 1}')

if day == 31:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8:
        print(f'0{month}.{day - 1} 0{month + 1}.0{1}')
    elif month == 10:
        print(f'{month}.{day - 1} {month + 1}.0{1}')

if day == 30:
    if month == 4 or month == 6:
        print(f'0{month}.{day - 1} 0{month + 1}.0{1}')
    if month == 9:
        print(f'0{month}.{day - 1} {month + 1}.0{1}')
    if month == 11:
        print(f'{month}.{day - 1} {month + 1}.0{1}')

if day == 28 and month == 2:
    print(f'0{month}.{day - 1} 0{month + 1}.0{1}')

if day == 1:
    if month == 5 or month == 7:
        print(f'0{month - 1}.{30} 0{month}.0{day + 1}')
    elif month == 10:
        print(f'0{month - 1}.{30} {month}.0{day + 1}')
    elif month == 12:
        print(f'{month - 1}.{30} {month}.0{day + 1}')

if day == 1:
    if month == 2 or month == 4 or month == 6 or month == 8 or month == 9:
        print(f'0{month - 1}.{31} 0{month}.0{day + 1}')
    elif month == 11:
        print(f'{month - 1}.{31} {month}.0{day + 1}')

if day == 1:
    if month == 3:
        print(f'0{month - 1}.{28} 0{month}.0{day + 1}')
