n = int(input('Введите ширину шоколадки в дольках : '))
m = int(input('Введите длину шоколадки в дольках : '))
k = int(input('Введите сколько вы хотите получить долек шоколада : '))
if n < m:
    num = n * n 
else:
    num = m * m
if k == num:
    print('YES')
else:
    print('NO')