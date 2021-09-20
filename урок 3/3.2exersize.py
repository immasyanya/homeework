def information(name, surname, year, city, email, phone):
    print(f'Ваши данные: {name}, {surname}, {year}, {city}, {email}, {phone}')


information(input('Введите ваше имя: '), input('Введите вашу фамилию: '), input('Введите ваш год рождения: '),
            input('Введите ваш город: '), input('Введите ваш email: '), input('Введите ваш номер телефона: '))
