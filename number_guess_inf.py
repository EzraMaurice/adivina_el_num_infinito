import random
num = random.randint(1,100)
print(num)
count = 1
while True:
    player = int(input('ingresa un numero del 1-100: '))
    if player == num:
        print('adivinaste!')
        print(f'adivinaste en {count} intentos')
        break
    else:
        print('intenta denuevo')
        count += 1