"""
Operadores para Tipos Numéricos

-------------------------------
Operadores para Tipos Numéricos
-------------------------------

Problema Prático 2.8
Em que ordem os operadores nas expressões a seguir são avaliados?
(a)2 + 3 == 4 or a >= 5
(b)lst[1] * -3 < -10 == 0
(c)(lst[1] * -3 < -10) in [0, True]
(d)2 * 3**2
(e)4 / 2 in [1, 2, 3]
"""


"""
---------------
Criando Objetos
---------------

Problema Prático 2.9
Qual é o tipo do objeto ao qual essas expressões são avaliadas?
(a)False + False
(b)2 * 3**2.0
(c)4 // 2 + 4 % 2
(d)2 + 3 == 4 or 5 >= 5"""
##
print("a")
print(type(False + False))
print("b")
print(type(2 * 3**2.0))
print("c")
print(type(4 // 2 + 4 % 2))
print("d")
print(type(2 + 3 == 4 or 5 >= 5))


"""
--------------
BIBLIOTECA PADRÃO PYTHON
-------------------

Problema Prático 2.10
Escreva expressões Python correspondentes ao seguinte:
(a)O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
(b)O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
(c)A área de um disco com raio a
(d)O valor da expressão Booleana que verifica se um ponto com 
coordenadas x e y está dentro de um círculo com centro (a, b) e raio r
"""
##
import math
print("a")
a = float(input("valor do lado a:"))
b = float(input("valor do lado b:"))
c = math.hypot(2, 3)
print(c)
print("b")
d = c > 5
print(d)
print("c")
e = math.pi*a**2
print("d")
print("faltou trigonometria")
