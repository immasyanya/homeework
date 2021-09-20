def division(x, y):
    try:
        z = int(x) / int(y)
    except ZeroDivisionError:
        return 'Деление на ноль не  существует!'
    return round(z, 2)

print(division(input('Введите делимое: '), input('Введите делитель: ')))
