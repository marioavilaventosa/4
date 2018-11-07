import random
palabras = ['cerillas', 'patrulla', 'papel', 'azor', 'alerones', 'conversar', 'sollozo', 'manzana']
palabra = palabras[random.randint(0,7)]
print(palabra)
fallos = 5
adivinado = '_ ' * len(palabra)
cuenta = 0
aciertos = len(palabra)

print('Quedan' , fallos , 'fallos')
print(adivinado)
while fallos != 0: 
    if aciertos == 0:
        print('Has adivinado la palabra')
        break
    letra = input('Escribe una letra: ')
    while letra in '0123456789':
        print('No escribas un numero')
        letra = input('Escribe una letra: ')
    for car in palabra:
        cuenta += 1 
        adivinado = adivinado.split()
        if car == letra:          
            adivinado[cuenta-1] = letra
            aciertos -=1
        adivinado = ' '.join(adivinado)
    if not letra in palabra:
        fallos -= 1
    cuenta = 0
    print('Quedan' , fallos , 'fallos')
    print(adivinado)
if fallos == 0:
    print('Has perdido')