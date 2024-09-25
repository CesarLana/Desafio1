frutas = ["maça", "pera", "abacaxi"]
print(frutas[0])

numeros = [1, 21, 20, 32, 41, 57, 63, 75, 89, 92]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(pares)


numeros2 = [1, 21, 20, 32, 41, 57, 63, 75, 89, 92]
quadrado = []

for numero1 in numeros2:
        quadrado.append(numero1 ** 2)
    
print(quadrado)

cacau = ["zeca", "windows", "mato", "natal", "agua", "leao", "medico", "tamandua"]
cacau.sort(key=lambda x: len(x))
print(cacau)