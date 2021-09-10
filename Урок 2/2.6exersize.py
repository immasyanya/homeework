from typing import Tuple

struct: tuple[str, str, str, str] = ('Название','Цена','Количество','Ед.')
i = input('Введите количество вводимых товаров: ')
k = 0

arr = []
while k < int(i):
    arr.append((k+1,{struct[0]:input(f'Введите название {k+1} товара: '),struct[1]:input(f'Введите цену {k+1} товара: '),struct[2]:input(f'Введите количество {k+1} товара: '),struct[3]:input(f'Введите единицы измерения {k+1} товара: ')}))
    k += 1
print(arr)

result=[]
for t in range(4):
    temp = []
    for i in range(len(arr)):
        temp.append(arr[i][1][struct[t]])
    result.append({struct[t]:temp})

print(result)

"""
goods = []
features = {}
analytics = {[], [], [], []}
num = 0
while True:
    if input('').upper() = 'Q':
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        pro = input(f'"{f}": ')  #
        f_copy[f] = int(pro) if f == '' or f == '' else pro  #
        analytics[f].append(f_copy[f])  #
    goods.append((num, f_copy))  #
    print(f'\n  \n {goods}') 
    print(f'\n  \n {"*" * 30}')
    for key, value in analytics.item():
        print(f'{key:>30}: {value}')
    print("*" * 30)    
"""