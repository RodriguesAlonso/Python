'''Exercícios propostos
1. Faça X = 0.0 e Y = 18. Verifique o tipo de dado que o Python atribuiu a cada
um. Faça Z = X + Y e verifique o resultado calculado e armazenado em Z.
Verifique com qual tipo de dado foi criado o objeto Z.
2. Atribua um valor qualquer a um objeto a (minúsculo). Utilize o comando type
ou o comando print com o objeto A (maiúsculo). Relate o que aconteceu.
3. No IDL E, faça A = "Questão 3", B = 25 e C = 3.9. Utilize o comando type para
verificar qual é o tipo de dado dos objetos A, B e C.
4. Reproduza em um programa todos os casos de operações aritméticas do
Quadro 2.1, para A = 14 e B = 5, e compare os valores obtidos por você com
os valores esperados constantes do quadro.
5. Escreva a sequência de comandos necessária para o cálculo da área de um
triângulo de base 9 e altura 6.
6. Refaça o exercício 5 alterando-o de modo que a base e a altura do triângulo
sejam lidas do teclado. Considere-as números reais. '''

##
print('=1=' * 3)
x, y = 0.0, 18
print(x, y)
print(type(x)), print(type(y))
print('=Fim=' * 3)
##
'''print('=2='*3)
a = input('digite um valor qualquer')
print(A)
print('=Fim='*3)'''
##
print('=3=' * 3)
a, b, c = 'questão 3 ', 25, 3.9
print(type(a)), print(type(b)), print(type(c))
print('=Fim=' * 3)
##
print('=4=' * 3)
a, b = 14, 5
soma = a + b
sub = a - b
mult = a * b
div = a / b
print('soma {}\nsub {}\nmult {}\ndiv {}'.format(soma, sub, mult, div))

print('=Fim=' * 3)
##
print('=5=' * 3)
base = 9
altura = 6
area = base * altura / 2
print('Area do triangulo {}'.format(area))
print('=Fim=' * 3)
##
print('=6=' * 3)
base = eval(input('digite a base do triangulo:'))
altura = eval(input('digite a altura do triangulo:'))
area = base * altura / 2
print('Area do triangulo {}'.format(area))
print('=Fim=' * 3)

'''
4. Escreva um programa que leia um número inteiro do teclado e diga se esse 
número é positivo ou negativo. 
5. Escreva um programa que leia um número inteiro do teclado e diga 
se esse número é par ou ímpar. Para saber se um número é par, 
deve-se verificar se o resto de sua divisão por 2 é igual a zero. Para calcular 
o resto da divisão de um número por outro deve-se utilizar o operador 0/0. 
Por exemplo: ao escrever a expressão em negrito a seguir e supondo que A 
e B tenham conteúdo inteiro.  '''
##
print('_4_' * 3)
num = int(input('digite um número inteiro'))
if num > 0:
    print('número positivo')
elif num < 0:
    print('número negativo')
else:
    print('número é zero')
print('_FIM_' * 3)
##
print('_5_' * 3)
num = int(input('digite um número inteiro'))
if num % 2 == 0:
    print('número par')
else:
    print('número é impar')
print('_FIM_' * 3)


 


##
# 16. Escreva um programa que leia um número inteiro N e, em seguida, leia N
# números reais, separando o menor e o maior, apresentando-os na tela.
n = int(input('digite um numero inteiro:'))
lista = []
for num in range(n):
    x = eval(input('digite um número real'))
    lista.append(x)
lista.sort()
print(lista)
##
# 17. Reescreva um programa do exercício 16 ignorando os números negativos
# fornecidos pelo usuário.
n = int(input('digite um numero inteiro:'))
lista = []
for num in range(n):
    x = eval(input('digite um número real'))
    if x > 0:
        lista.append(x)
lista.sort()
print(lista)
##
# 18. Elabore um programa que efetue a leitura de valores positivos inteiros até que
# zero ou um valor negativo seja informado. Ao final, devem ser apresentados
# o maior e menor valores informados pelo usuário, a quantidade de valores,
# a soma e a média de todos.
num = 1
lista = []
while num > 0:
    num = int(input('digite um numero inteiro positivo:'))
    if num > 0:
        lista.append(num)
        lista.sort()
print(lista[0])
print(lista[-1])
##
# 19. Escreva um programa que contenha um laço que será executado enquanto
# o número digitado for diferente de zero. Para cada número digitado pelo
# usuário. mostrar na tela apenas os que forem divisíveis por 2 e por 3.
num = 1
while num != 0:
    num = eval(input('digite um número'))
    if num % 2 == 0 and num % 3:
        print(num)
print('FIM')

##
# 20. Elabore um programa que apresente o somatório dos valores pares existentes
# na faixa entre 1 e N, em que N é um número digitado pelo usuário e
# que deve ser no mínimo 100 (obrigatório garantir esse requisito).
n = 0
while n < 99:
    n = int(input('digite um número inteiro maior que 99'))
for soma in range(n):
    soma += soma
    if soma % 2 == 0:
        soma += soma
        print(soma)

