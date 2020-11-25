##
'''Problemas
5.23 Escreva a função pagar(), que aceite como entrada um salário horário e o número de horas que um empregado trabalhou
na última semana. A função deverá calcular e retomar o pagamento do empregado.
O trabalho em hora extra deverá ser pago da seguinte forma:
qualquer total de horas além de 40, porém menor ou igual a 60, deverá ser pago a 1,5 vez o salário
horário normal. Qualquer total além de 60 deverá ser pago a duas vezes o salário horário normal. 
'''


def pagar(salario, trabalho):
    if trabalho <= 40:
        pagamento = salario * trabalho
        return pagamento
    elif 40 < trabalho <= 60:
        horaExtra = trabalho - 40
        salario2 = salario * 1.5
        pagamento = (salario * 40) + (salario2 * horaExtra)
        return pagamento
    elif trabalho > 60:
        horaExtra2 = trabalho - 60
        salario2 = salario * 1.5
        salario3 = salario * 2
        pagamento = (salario * 40) + (salario2 * 20) + (salario3 * horaExtra2)
        return pagamento


x = pagar(10, 70)
print(x)
##
# Progreção aritimética

p = int(input('digite o primeiro termo da pa:'))
r = int(input('digite a razãp da pa'))
q = int(input('digite a quantidade de termos da pa'))
l = []
contador = 0
while contador < q:
    l.append(p)
    p += r
    contador += 1
print(l)
## lista e tamanho

num = 1
l = []
while num != 0:
    num = int(input('Digite um número intero'))
    if num != 0:
        l.append(num)
print(l, len(l))
## n numeros aleátorios sem duplicados
from random import randint

try:
    l = []
    num = int(input('digite um numero:'))
    for x in range(num):
        x = randint(10, 50)
        l.append(x)
    print('lista gerada:', l)
    l.reverse()
    print('lista inversa: ', l)
    l.sort()
    print('lista em ordem: ', l)
except:
    print('O numero digitado não é inteiro')
for dublicado in l:
    x = l.count(dublicado)
    if x > 1:
        print(dublicado)
        l.remove(dublicado)
print(l)
## gerdor de matriz
from random import randint
lin = int(input('digite a quantidade de linhas:'))
col = int(input('digite a quantidade de colunas:'))
mat = []
for linha in range(lin):
   mat.append([])
   print('matLinha',mat)
   for coluna in range(col):
       mat[linha].append(randint(0, 20))
       print('matcoluna', mat)
print(mat)
print('-'*10)
for x in mat:
    print(x)
## sequência de fibonacci
n = int(input('digite a quantidade de termos:'))
f =[]
a = 0
b =1
fibos = 0
for fibus in range(n):
    f.append(fibos)
    fibos = a + b
    a = b
    b = fibos
    print(f)


