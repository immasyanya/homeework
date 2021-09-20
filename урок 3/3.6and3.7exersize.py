def int_func():
    x = input('Введите слово/строку с маленьких букв: ')
    for word in x.split():
        i = 0
        for i_s in word:
            if 97 <= ord(i_s) <= 122:
                i += 1
    if i == len(word):
        print(x.title())
    else:
        print('Вводите только английские буквы!')

int_func()