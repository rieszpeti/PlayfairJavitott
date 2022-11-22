while (True):
    angolAbc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    magyarabc = ['a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l',
                 'm', 'n', 'o', 'ó', 'ö', 'ő', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ü', 'ű',
                 'v', 'w', 'x', 'y', 'z', 'zs']

    # abc = "abcdefghiklmnopqrstuvwxyz"

    angolVMagyar = input("angol vagy magyar abc?")

    kulcsSzo = input('Add meg a kulcsszot:')

    bemenet = []

    if (angolVMagyar == "angol"):
        bemenet = list(kulcsSzo) + angolAbc
        s = 5
        o = 5
    else:
        bemenet = list(kulcsSzo) + magyarabc
        s = 6
        o = 6

    print(bemenet)

    # -----------------------------------------------------------------------------------------------------------------------
    # duplikacio torlese

    bemenet_duplikaltN = list(dict.fromkeys(bemenet))

    # print(bemenet_duplikaltN)

    # -----------------------------------------------------------------------------------------------------------------------
    # matrix feltoltese

    #s = int(input("Add meg a sorok szamat:"))
    #o = int(input("Add meg az oszlopok szamat:"))

    matrix = [[0 for x in range(o)] for y in range(s)]

    lepteto = 0
    for i in range(s):
        for j in range(o):
            matrix[i][j] = bemenet_duplikaltN[lepteto]
            lepteto += 1

    print(f'\n{s}x{o}-os matrix a kodolashoz:\n')

    # matrix kiirasa

    for i in range(s):
        for j in range(o):
            print(matrix[i][j] + ' ', end='')
        print()

    # -----------------------------------------------------------------------------------------------------------------------
    # uzenet elokeszitese

    uzenet = input('\nAdd meg a titkositando uzenetet:')

    titkositandoLista = list(uzenet)

    xIndex = list()

    for i in range(len(titkositandoLista) - 1):
        if titkositandoLista[i] == titkositandoLista[i + 1]:
            titkositandoLista[i] += "x"
            xIndex.append(i + 1)

    szovegLista = ''

    for x in titkositandoLista:
        szovegLista += x

    vegereX = False
    if (int(len(szovegLista) % 2)) == 1:
        szovegLista += "x"
        vegereX = True

    # -----------------------------------------------------------------------------------------------------------------------
    # indexek eltárolása

    kodLokacio = list()

    for i in range(len(szovegLista)):
        for j in range(s):
            for k in range(o):
                if (szovegLista[i] == matrix[j][k]):
                    kodLokacio.append(j)
                    kodLokacio.append(k)

    # lista atalakitasa lista/2 x 2 matrixsza

    kodMatrix = []

    while kodLokacio != []:
        kodMatrix.append(kodLokacio[:2])
        kodLokacio = kodLokacio[2:]

    # -----------------------------------------------------------------------------------------------------------------------
    # szoveg titkositasa

    kodoltSzoveg = list()

    for i in range(0, len(kodMatrix) - 1, 2):
        balX = kodMatrix[i][0]
        balY = kodMatrix[i][1]
        jobbX = kodMatrix[i + 1][0]
        jobbY = kodMatrix[i + 1][1]
        # ha egy sorban van
        if (kodMatrix[i][0] == kodMatrix[i + 1][0]):
            if (balY == o-1):
                kodoltSzoveg.append(matrix[balX][0])
            if (balY < o-1):
                kodoltSzoveg.append(matrix[balX][balY + 1])
            if (jobbY == o-1):
                kodoltSzoveg.append(matrix[jobbX][0])
            if (jobbY < o-1):
                kodoltSzoveg.append(matrix[jobbX][jobbY + 1])

        # ha egy oszlopban van
        elif (kodMatrix[i][1] == kodMatrix[i + 1][1]):
            if (balX == s-1):
                kodoltSzoveg.append(matrix[0][balY])
            if (balX < s-1):
                kodoltSzoveg.append(matrix[balX + 1][balY])
            if (jobbX == s-1):
                kodoltSzoveg.append(matrix[0][jobbY])
            if (jobbX < s-1):
                kodoltSzoveg.append(matrix[jobbX + 1][jobbY])

        # ha kulonbozo sorban van
        else:
            kodoltSzoveg.append(matrix[balX][jobbY])
            kodoltSzoveg.append(matrix[jobbX][balY])

    print(f'A titkositott szoveg: {"".join(kodoltSzoveg)}')

    # -----------------------------------------------------------------------------------------------------------------------
    # kodolt szoveg indexeinek eltarolasa

    deKodLista = list()

    for i in range(len(kodoltSzoveg)):
        for j in range(s):
            for k in range(o):
                if (kodoltSzoveg[i] == matrix[j][k]):
                    deKodLista.append(j)
                    deKodLista.append(k)

    # lista atalakitasa lista/2 x 2 matrixsza

    deKodMatrix = []

    while deKodLista != []:
        deKodMatrix.append(deKodLista[:2])
        deKodLista = deKodLista[2:]

    print(deKodMatrix)

    # -----------------------------------------------------------------------------------------------------------------------
    # szoveg dekodolasa
    deKodoltLista = list()

    for i in range(0, len(deKodMatrix) - 1, 2):
        balX = deKodMatrix[i][0]
        balY = deKodMatrix[i][1]
        jobbX = deKodMatrix[i + 1][0]
        jobbY = deKodMatrix[i + 1][1]

        # ha egy sorban van
        if (deKodMatrix[i][0] == deKodMatrix[i + 1][0]):
            if (balY == 0):
                deKodoltLista.append(matrix[balX][o-1])
            if (balY < o-1 and balY != 0):
                deKodoltLista.append(matrix[balX][balY - 1])
            if (jobbY == 0):
                deKodoltLista.append(matrix[jobbX][o-1])
            if (jobbY < o-1 and jobbY != 0):
                deKodoltLista.append(matrix[jobbX][jobbY - 1])

        # ha egy oszlopban van
        elif (deKodMatrix[i][1] == deKodMatrix[i + 1][1]):
            if (balX == 0):
                deKodoltLista.append(matrix[s-1][balY])
            if (balX <= s-1 and balX != 0):
                deKodoltLista.append(matrix[balX - 1][balY])
            if (jobbX == 0):
                deKodoltLista.append(matrix[s-1][jobbY])
            if (jobbX <= s-1 and jobbX != 0):
                deKodoltLista.append(matrix[jobbX - 1][jobbY])

        # ha kulonbozo sorban van
        else:
            deKodoltLista.append(matrix[balX][jobbY])
            deKodoltLista.append(matrix[jobbX][balY])

    # -----------------------------------------------------------------------------------------------------------------------
    # dekodolt lista szovegge alakitasa

    if (len(xIndex) != 0):
        for i in xIndex:
            deKodoltLista[i] = ""

    if (vegereX == True):
        deKodoltLista = deKodoltLista[:-1]

    print(f'\nA dekodolt szoveg: {"".join(deKodoltLista)}')

    # -----------------------------------------------------------------------------------------------------------------------
    # ha szeretne meg titkositani akkor visszadobja az elejere

    szeretnelMeg = input(
        '\nSzeretnel meg titkositani?\nHa igen akkor ird be, hogy "i", \nha nem akkor azt írd be, hogy "n"?\n')

    if (szeretnelMeg == 'i'):
        continue
    print("Koszi, hogy minket valasztottal.")
    break
