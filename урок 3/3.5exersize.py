def my_sum():
    n = 0

    while True:
        t = input('Введите числа или "Е", если хотите завершить  ').split()
        for i in t:
            if i.lower() == 'E':
                return n
            else:
                try:
                    n += int(i)
                except ValueError:
                    print('Для выхода из программы нажмите "E"')
        print(n)

my_sum()