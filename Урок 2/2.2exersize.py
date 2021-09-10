x = list(input('Введите числа списка через пробел: ').split())
print('Введенный список: ', x)
el = 0

while el < len(x):
    if len(x) % 2 != 0:
        if el == len(x) - 1:
            break
    x[el], x[el + 1] = x[el + 1], x[el]
    el = el + 2

print('Измененный список: ', x)

"""
for i in range(1,len(x), 2): # помогает спастись от ошибки при нечетном количестве
    x[i - 1], x[i] = x[i], x[i - 1]
print(x)

или

i = len(x) if len(x) % 2 != 0 else len(x) - 1
x[: i: 2], x[1 : i: 2] = x[1 : i: 2], x[: i: 2]
print(x)

for i in range(1, len(x), 2):
    x.insert(i - 1, x.pop(i)) # pop потому что не просто удаляет значение, но и запоминает его
print(x)    
"""