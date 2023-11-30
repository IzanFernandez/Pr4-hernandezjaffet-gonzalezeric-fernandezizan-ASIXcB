"""
Eric González, Izan Fernandez, Jaffet Hernandez
29/11/2023
M03 UF1 A4
Descripció: Pr4

"""
try:
    numeros = int(input("Introdueix un nombre: "))
    suma_parells = 0
    suma_senars = 0

    for num in range(numeros):
        if num % 2 == 0:
            suma_parells += num
        else:
            suma_senars += num

    print("La suma de parells és:", suma_parells)
    print("La suma de senars és:", suma_senars)
except:
    print("No son les dades correctes")
