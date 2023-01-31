number = int(input('Введите номер билета: '))
if 999999 > number > 99999:
  num1 = int(number / 1000)
  num2 = int (number % 1000)
  
  a = int (num1 / 100)
  b = int (num1 / 10 % 10)
  c = num1 % 10
  sum1 = a + b + c

  a = int (num2 / 100)
  b = int (num2 / 10 % 10)
  c = num2 % 10
  sum2 = a + b + c

  if sum1 == sum2:
    print('Yes')
  else:
    print('No')
else:
  print('Такого билета не существует.')