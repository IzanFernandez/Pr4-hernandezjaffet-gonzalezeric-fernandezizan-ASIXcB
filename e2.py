alcada_triangle = int(input("Alçada del triangle (entre 2 i 9):"))

if 2 <= alcada_triangle <= 9:
    print(("1"))
    for i in range(2,alcada_triangle +1):
        if i == alcada_triangle:
            print((str(i) + '') * ((i)))
        else:
            print(str(i) + ' ' * ((i-2)) + str(i))
else:
    print("L'alçada ha de ser entre 2 i 9, ambdós inclosos.")
