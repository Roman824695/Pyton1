number = int(input('Введите трехзначное число: '))
if 999 > number > 99:
  a = int (number / 100)
  b = int (number / 10 % 10)
  c = number % 10
  sum = a + b + c
  print(f"Сумма цифр числа {number}  =  {sum}")
else:
  print('Число не трехзначное')