texto = input('Introduce una palabra:\n')
revisadas = ''

for letra in texto:
    if not letra in revisadas:
        print(letra , '=' , texto.count(letra))
        revisadas += letra