s = int(input('Ввидите сумму чисел : '))
p = int(input('Ввидите произведение чисел : '))
x = 0
y = 0

while x + y != s or x * y != p:
  
  if x < 1000:
    x += 1
  else:
    x = 0
    y += 1 

print(x, y)

      