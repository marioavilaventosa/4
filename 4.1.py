texto = input('Introduce una palabra:\n')

sin_vocales = ''
solo_vocales = ''
vocales_may = ''

for car in texto:
    if not car in "aeiou":
        sin_vocales+=car
        vocales_may+=car
    else:
        solo_vocales+=car
        vocales_may+=car.upper()

print(sin_vocales)
print(solo_vocales)
print(vocales_may)

