number = int(input('Введите число N:  '))

x = 1
y = 1
print (x)
while x < number:
    x = 2 ** y
    y += 1
    if x < number:
        print(x)