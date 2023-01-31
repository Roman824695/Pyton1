crans = int(input('Введите общее число журавликов: '))

petya = int(crans / 6)
sergey = petya
katya = (petya + sergey) * 2
you = crans - (katya + petya + sergey)
print(f"{sergey} {katya} {petya} вы сделали {you}")

