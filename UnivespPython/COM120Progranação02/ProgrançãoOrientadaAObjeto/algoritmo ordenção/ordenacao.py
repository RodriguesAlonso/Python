from random import sample


def geralista(tamanho=10, alcance=10):
    from random import randrange
    listag = []
    for x in range(tamanho):
        listag.append(randrange(0, alcance))
    return listag


def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v) - i - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
    print(v)


def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1
        while j >= 0 and x < v[j]:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = x


def intercala(v, ini, meio, fim):
    l = v[ini:meio + 1]
    r = v[meio + 1:fim + 1]
    l.append(999)
    r.append(999)
    i = 0
    j = 0
    for k in range(ini, fim+1):
        if l[i] <= r[j]:
            v[k] = l[i]
            i += 1
        else:
            v[k] = r[j]
            j += 1


def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini+fim)//2
        merge_sort(v, ini, meio)
        merge_sort(v, meio + 1, fim)
        intercala(v, ini, meio, fim)


def quick_sort(v, ini, fim):
    meio = (ini + fim)//2
    pivo = v[meio]
    i = ini
    j = fim
    while i < j:
        while v[i] < pivo:
            i += 1
        while v[j] > pivo:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1
    if j > ini:
        quick_sort(v, ini, j)
    if i < fim:
        quick_sort(v, i, fim)


def busca_binaria(l, x, ini, fim):
    meio = (ini+fim)//2
    if ini > fim:
        return 'elemento não encontrado'

    if x == l[meio]:
        return meio
    if x < l[meio]:
        return busca_binaria(l, x, ini, meio - 1)
    if x > l[meio]:
        return busca_binaria(l, x, meio + 2, fim)



x = sample(range(100), 10)
x.sort()
print(x)

