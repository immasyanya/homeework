def my_func_1(x,y):
    n = 1
    if y == 0:
        return n
    else:
        while y < 0:
            n = n * x
            y += 1
        return round(1 / n, 3)
def my_func_2(x_1,y_1):
    return round(x_1 ** y_1, 3)

print(my_func_1(int(input('Введите положительное число: ')), int(input('Введите отрицательное число: '))))

print(my_func_2(int(input('Введите положительное число: ')), int(input('Введите отрицательное число: '))))