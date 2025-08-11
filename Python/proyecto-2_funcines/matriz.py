matriz = [
    [8,  7,  0],
    [34, 2, -1],
    [5, -5, 12]
]

for i in enumerate(matriz):
    for j in enumerate(i[1]):
        if j[1] % 2 == 0:
            matriz[i[0]][j[0]] = 0
            print(matriz)
        else:
            matriz[i[0]][j[0]] = 1
