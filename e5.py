"""
Eric González, Izan Fernandez, Jaffet Hernandez
30/11/2023
M03 UF1 A4
Descripció: Pr4

"""
try:
    primer_numero = int(input("Introueix el primer numero a multiplicar:"))
    segon_numero = int(input("Introdueix el segon numero a multiplicar:"))
    resultat = 0
    for i in range(2):
        resultat += primer_numero
    print(resultat)
except:
    print("No son les dades indicades")
