"""Problema Prático 2.1

Escreva expressões algébricas Python correspondentes aos seguintes comandos:

(a)A soma dos 5 primeiros inteiros positivos.

(b)A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).

(c)O número de vezes que 73 cabe em 403.

(d)O resto de quando 403 é dividido por 73.

(e)2 à 10a potência.

(f)O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).

(g)O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50."""

##
print("a")
soma = 1 + 2 + 3 + 4 + 5
print(soma)
##
print("b")
sara = 23
mark = 19
fatima = 31
idadeMedia = (sara + mark + fatima)/3
print("A média das idades da Sara, Mark e Fátima é {}".format(idadeMedia))
##
print("c")
print("o Número de vezes que 73 cabe em 403 é {}".format(403 // 73))
##
print("d")
print("O resto da divisão de 403 com 73 é {}".format(403 % 73))
##
print("e")
print("2 à 10 potencia é {}".format(2**10))
##
print("f")
valorAbsoluto = 54 - 57
print("O valor absoluto entre 54 e 57 é {}".format(abs(valorAbsoluto)))
##
preco1 = 34.99
preco2 = 29.95
preco3 = 31.50
print("O menor preço entre : R$ 34,99, R$ 29,95 e R$ 31,50. é {}".format(min(preco1, preco2, preco3)))

##

"""Problema Prático 2.2
Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:

(a)A soma de 2 e 2 é menor que 4.
(b)O valor de 7 // 3 é igual a 1 + 1.
(c)A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
(d)A soma de 2, 4 e 6 é maior que 12.
(e)1387 é divisível por 19.
(f)31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
(g)O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*"""
##
print("a")
print(2+2 < 4)
##
print("b")
print(7 // 3 == 1 + 1)
##
print("c")
print(3**2 + 4**2 == 25)
##
print("d")
print(2 + 4 + 6 > 12)
##
print("e")
print(1381 % 19 == 0)
##
print("f")
print(31 % 2 == 0)
##
print("g")
preco1 = 34.99
preco2 = 29.95
preco3 = 31.50
print(min(preco1, preco2, preco3 < 30,00))

"""Problema Prático 2.3
Escreva instruções Python que correspondem às ações a seguir e execute-as:
(a)Atribua o valor inteiro 3 à variável a.
(b)Atribua 4 à variável b.
(c)Atribua à variável c o valor da expressão a * a + b * b."""
##
print("a")
a = 3

print("b")
b = 4

print("c")
c = a * a + b * b

"""Problema Prático 2.4
Comece executando as instruções de atribuição:

>>> s1 = 'ant'
>>> s2 = 'bat'
>>> s3 = 'cod'

Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
(a)'ant bat cod'
(b)'ant ant ant ant ant ant ant ant ant ant'
(c)'ant bat bat cod cod cod'
(d)'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
(e)'batbatcod batbatcod batbatcod batbatcod batbatcod'"""
##
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
##
print("a")
print(s1, s2, s3)

##
print("b")
print(10 * (s1+" "))
##
print("c")
print(s1, 2*(s2+" "), 3*(s3+" "))
##
print("d")
print(7 * (s1+" "+s2+" "))
##
print("e")
print(5 * (s2 + s2 + s3+" "))

"""Problema Prático 2.5
Comece executando a atribuição:
s = '0123456789'
Agora, escreva expressões usando a string s e o operador de indexação que é avaliado como:
(a)'0'
(b)'1'
(c)'6'
(d)'8'
(e)'9'"""

##
s = '0123456789'

print("a")
print(s[0])
print("b")
print(s[1])
print("c")
print(s[6])
print("d")
print(s[-2])
print("e")
print(s[-1])
##

