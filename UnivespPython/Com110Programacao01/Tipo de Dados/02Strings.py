"""
--------------------------
OPERADORES DE STRING
--------------------------

Problema Prático 2.4
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


"""
-------------------
OPERADOR DE INDEXAÇÃO
---------------------

Problema Prático 2.5
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
