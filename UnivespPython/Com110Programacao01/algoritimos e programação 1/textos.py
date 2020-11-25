##
t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]


def soma2d(t1, t2):
    linhas = len(t1)
    colunas = len(t1[0])
    for i in range(linhas):
        for j in range(colunas):
            t[i][j] = t1[i][j] + t2[i][j]
    for linha in t:
        print(linha)

