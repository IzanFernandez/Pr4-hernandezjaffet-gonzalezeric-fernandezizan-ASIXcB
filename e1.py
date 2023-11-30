"""
Eric González, Izan Fernandez, Jaffet Hernandez
29/11/2023
M03 UF1 A4
Descripció: Pr4

"""
numeros = input("Introduir 10 numeros sencers: ").split()

positius = 0
negatius = 0
zeros = 0
for num in numeros:
    num = int(num)
    if num > 0:
        positius += 1
    if num < 0:
        negatius += 1
    if num == 0:
        zeros += 1
print("numeros positius:", positius)
print("numeros negatius:", negatius)
print("numeros zeros:", zeros)
