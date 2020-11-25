"""
-------------------
OPERADORES DE LISTA
-------------------

Problema Prático 2.6
Primeiro, execute a atribuição
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
Agora, escreva duas expressões Python que são avaliadas,
respectivamente, como a primeiro e a última palavras em palavras, na ordem do dicionário."""

##
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
palavras.sort()
print(palavras[0])
print(palavras[-1])

"""
----------------
MÉTODOS DE LISTA
----------------

Problema Prático 2.7
Dada a lista de notas de trabalho de casa dos alunos
>>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
escreva:
(a)Uma expressão que avalia para o número de 7 notas.
(b)Uma instrução que muda a última nota para 4.
(c)Uma expressão que avalia para a nota mais alta.
(d)Uma instrução que classifica as notas da lista.
(e)Uma expressão que avalia para a média das notas."""
##
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas)
print("a")
print(7 in notas)
print("b")
notas[-1] = 4
print(notas)
print("c")
print(max(notas))
print("d")
notas.sort()
print(notas)
print("e")
print(sum(notas)/len(notas))


