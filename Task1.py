number = int(input('Введите число монеток :  '))
char = []

for i in range(number): 
  from random import randint
  char.append(randint(0, 1))
print(char)

num1 = 0 
num2 = 0 
   
for i in range(len(char)):
  if char[i] == 1:
    num1 += 1
  else:
    num2 += 1
   
if num1 > num2:
  print(f"Минииальное число монет которое нужно перевернуть : {num2}")
else:
  print(f"Минииальное число монет которое нужно перевернуть : {num1}")





  
