"""
Eric González, Izan Fernandez, Jaffet Hernandez
30/11/2023
M03 UF1 A4
Descripció: Pr4

"""
BLANC = "⬜"
NEGRE = "⬛"

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print(BLANC, end=" ")
        else:
            print(NEGRE, end=" ")
    print()