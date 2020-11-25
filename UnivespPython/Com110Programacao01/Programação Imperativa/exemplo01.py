'''def fat (x):
    n = 0
    fat = 1
    while fat <= x:
        n += 1
        fat *= n
        print('{}! = {}'.format(n, fat))
    print(n - 1)


def primo(x):
    i = 2
    while i < x:
        if x % i == 0:
            break
        i += 1
    resposta = x == i
    return resposta
'''


'''
prova semana 06
##
for a in range(2, 50):
    if primo(a):
        print(a)
        continue
##
list = ['a', 1, 'b', 2]

d = dict()
for i in range(len(list) - 1):
    print(i)
    d[list[i]] = list[i + 1]
    print(d[list[i]])

print(d['b'])
##
list = [1, 2, [3, 4]]

for i in list:
    print(i)
##
for i in range(1, 5):
     print(i)
##
list = [-1, 2, -3, 4]
aux = 0
    for i in list:
        aux += i
print(aux)
##
list = [1, -2, -3, 4]
aux = 0
    for i in list:
         if i % 2 == 0:
             aux += i
print(aux)'''


'''def simetrica(m):
    linhas = len(m)
    colunas = len(m[0])
    for l in range(linhas):
        for c in range(l + 1, colunas):
            if m[l][c] != m[c][l]:
                return False
    return True'''


'''def transposta(m):
    tamanho = len(m)
    m0 = []
    mfinal = []
    i = 0
    
    while i < tamanho:
        for matriz in range(tamanho):
            m0.append(m[matriz][i])
        i += 1
        mfinal.append(m0)
        m0 = []
    print(mfinal)
    for x in mfinal:
        print(x)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposta(mat)'''


