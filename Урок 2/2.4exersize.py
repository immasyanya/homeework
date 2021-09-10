x = input('Введите строку: ')

t = list(x.split(' '))
i = 1

for el in t:
    print(i, el[:10])
    i += 1