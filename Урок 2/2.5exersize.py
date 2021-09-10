ret = [8, 8, 5, 2, 2]
x = float(input('Введите число: '))

ret.append(x)
ret.sort(reverse = True)
print(ret)
# удивительно, но добавляет в конец

"""
# правильный вариант, помогает добавлять значение именно в конец
l = 0
for n in ret:
    if x <= n:
        l += 1
    else:
        break
ret.insert(l, x)
print(ret)            
"""