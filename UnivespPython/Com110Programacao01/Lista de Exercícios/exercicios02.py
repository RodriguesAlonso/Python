##
# a)Efetuar a leitura de dois valores numéricos inteiros representados pelas variáveis A e B e
# apresentar o resultado da diferença do maior valor pelo menor valor.

def diferencaMaior():
    a = int(input("Digite o valor de A:"))
    b = int(input("Digite o valor de B:"))
    if a > b:
        resultado = a - b
        print("A diferença de {} e {} é {}".format(a, b, resultado))
    else:
        resultado = b - a
        print("A diferença de {} e {} é {}".format(b, a, resultado))


##
# b) Efetuar a leitura de um valor numérico inteiro positivo ou negativo representado pela variável N e
# apresentar o valor lido como sendo positivo.
# Dica: se o valor lido for menor que zero, ele deve ser multiplicado por –1.


def numPositivo():
    num = int(input("Digite um valor inteiro: "))
    if num < 0:
        print("O valor positivo é {}".format(num * -1))
    else:
        print("O valor positivo é {}".format(num))


##
# c) Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno
# representadas pelas variáveis N1, N2, N3 e N4.
# Calcular a média aritmética (variável MD) desse aluno e
# apresentar a mensagem “Aprovado” se a média obtida for maior ou igual a 5;
# caso contrário, apresentar a mensagem “Reprovado”.
# Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.


def boletim():
    n1 = float(input("Digite a note 01"))
    n2 = float(input("Digite a note 02"))
    n3 = float(input("Digite a note 03"))
    n4 = float(input("Digite a note 04"))
    md = (n1 + n2 + n3 + n4) / 4
    if md >= 5:
        print("A média do aluno é {} então foi aprovado".format(md))
    else:
        print("A média do aluno é {} então foi reprovado".format(md))


##
# d) Ler os valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1, N2, N3 e N4.
# Calcular a média aritmética (variável MD1) desse aluno e
# apresentar a mensagem “Aprovado” se a média obtida for maior ou igual a 7;
# caso contrário, o programa deve solicitar a quinta nota (nota de exame, representada pela variável NE) do aluno e
# calcular uma nova média aritmética (variável MD2) entre a nota de exame e a primeira média aritmética.
# Se o valor da nova média for maior ou igual a cinco, apresentar a mensagem “Aprovado em exame”;
# caso contrário, apresentar a mensagem “Reprovado”.
# Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.


def boletim02():
    n1 = float(input("Digite a note 01"))
    n2 = float(input("Digite a note 02"))
    n3 = float(input("Digite a note 03"))
    n4 = float(input("Digite a note 04"))
    md1 = (n1 + n2 + n3 + n4) / 4
    if md1 >= 7:
        print("média {}, o aluno foi APROVADO".format(md1))
    elif md1 < 7:
        ne = float(input("Insira a nota do exame:"))
        md2 = (md1 + ne) / 2
        if md2 >= 5:
            print("A média do aluno em exame é {}, aprovado".format(md2))
        else:
            print("REPROVADO")


##
# e) Efetuar a leitura de três valores numéricos (representados pelas variáveis A, B e C) e
# processar o cálculo da equação completa de segundo grau, utilizando a fórmula de Bhaskara
# (considerar para a solução do problema todas as possíveis condições para delta:
# delta < 0 – não há solução real, delta > 0 – há duas soluções reais e diferentes e delta = 0 – uma solução real).
# lembre-se de que é completa a equação de segundo grau que possui todos os coeficientes A, B e C diferentes de zero.
# O programa deve apresentar respostas para todas as condições estabelecidas para delta.


def bhaskara():
    a = int(input("Digite o valor de A:"))
    b = int(input("Digite o valor de B:"))
    c = int(input("Digite o valor de C:"))

    if a != 0 and b != 0 and c != 0:
        delta = b ** 2 - (4 * a * c)
        print("DELTA: ", delta)
        if delta == 0:
            r1 = (-b + delta) / (a * 2)
            print("Só existe uma solução real: {}".format(r1))
        elif delta < 0:
            print("nenhuma solução real")
        elif delta > 0:
            r1 = (-b + delta) / (2 * a)
            r2 = (-b - delta) / (2 * a)
            print("Existe duas soluções reais: r1:{} e r2:{}".format(r1, r2))
    else:
        print("Os valores A, B e C devem ser diferentes de zero para ser uma equação de segundo grau completa")


##
# f)Ler três valores inteiros representados pelas variáveis A, B e C e
# apresentar os valores lidos dispostos em ordem crescente.
# Dica: utilizar tomada de decisão sequencial e as ideias trabalhadas nos exercícios “g” (propriedade distributiva) e
# “f” (troca de valores) do Capítulo 3.


def ordenarCrescente():
    a = int(input("Digite o valor de A:"))
    b = int(input("Digite o valor de B:"))
    c = int(input("Digite o valor de C:"))
    if a > b and a > c:
        if b > c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b > c and b > a:
        if c > a:
            print(b, c, a)
        else:
            print(b, a, c)
    else:
        if a > b:
            print(c, a, b)
        else:
            print(c, b, a)


##
# g) Fazer a leitura de quatro valores numéricos inteiros representados pelas variáveis A, B, C e D.
# Apresentar apenas os valores que sejam divisíveis por 2 e 3.

def divide2e3(x):
    if x % 2 == 0 and x % 3 == 0:
        y = True
    else:
        y = False
    return y


def apenasDiv3():
    a = int(input("Digite o valor de A:"))
    b = int(input("Digite o valor de B:"))
    c = int(input("Digite o valor de C:"))
    d = int(input("Digite o valor de D:"))

    a1 = divide2e3(a)
    if a1 == True:
        print("O valor A:{}".format(a))
    b1 = divide2e3(b)
    if b1 == True:
        print("O valor B:{}".format(b))
    c1 = divide2e3(c)
    if c1 == True:
        print("O valor C:{}".format(c))
    d1 = divide2e3(d)
    if d1 == True:
        print("O valor D:{}".format(d))
    else:
        print("nenhum valor é divisivel por 2 e 3")


##
# h) Efetuar a leitura de quatro valores numéricos inteiros representados pelas variáveis A, B, C e D.
# Apresentar apenas os valores que sejam divisíveis por 2 ou 3.


def divide2ou3(x):
    if x % 2 == 0 or x % 3 == 0:
        y = True
    else:
        y = False
    return y


def divisivel2ou3():
    a = int(input("Digite o valor de A:"))
    b = int(input("Digite o valor de B:"))
    c = int(input("Digite o valor de C:"))
    d = int(input("Digite o valor de D:"))

    a1 = divide2ou3(a)
    if a1 == True:
        print("O valor A:{}".format(a))
    b1 = divide2ou3(b)
    if b1 == True:
        print("O valor B:{}".format(b))
    c1 = divide2ou3(c)
    if c1 == True:
        print("O valor C:{}".format(c))
    d1 = divide2ou3(d)
    if d1 == True:
        print("O valor D:{}".format(d))
    else:
        print("nenhum valor é divisivel por 2 ou 3")


##
# i) Ler cinco valores numéricos inteiros (variáveis A, B, C, D e E),
# identificar e apresentar o maior e o menor valores informados.
# Não execute a ordenação dos valores como no exercício “f”.

def maior(x, y):
    if x > y:
        return x
    else:
        return y


def menor(x, y):
    if x < y:
        return x
    else:
        return y


def maiormenor():
    a = int(input("Digite o valor de A:"))
    b = int(input("Digite o valor de B:"))
    c = int(input("Digite o valor de C:"))
    d = int(input("Digite o valor de D:"))
    e = int(input("Digite o valor de E:"))

    m1 = maior(a,b)
    m2 = maior(c,d)
    m3 = maior(a,b)

    m4 = maior(m1, m2)
    m5 = maior(m3, e)

    maiorNumero = maior(m4, m5)

    m1 = menor(a, b)
    m2 = menor(c, d)
    m3 = menor(a, b)

    m4 = menor(m1, m2)
    m5 = menor(m3, e)

    menorNumero = menor(m4, m5)

    print("O maior número é {} e o menor é {}.".format(maiorNumero, menorNumero))


##
# j)Ler um valor numérico inteiro e apresentar uma mensagem informando se o valor fornecido é par ou ímpar.

def parImpar():
    a = int(input("Digite um calor inteiro:"))
    if a % 2 == 0:
        print("O número {} é par".format(a))
    else:
        print("O número {} é ímpar.".format(a))


##
# k Efetuar a leitura de um valor numérico inteiro que esteja na faixa de valores de 1 até 9.
# O programa deve apresentar a mensagem “O valor está na faixa permitida”, caso o valor informado esteja entre 1 e 9.
# Se o valor estiver fora da faixa, o programa deve apresentar a mensagem “O valor está fora da faixa permitida”.

def umAnove():
    num = int(input("Digite um valor inteiro ente 1 até 9:"))
    if num > 9 or num < 1:
        print("O valor está fora da faixa permitida")
    else:
        print("O valor está na faixa permitida")




##
# l)Fazer a leitura de um valor numérico inteiro qualquer e apresentá-lo caso não seja maior que 3.
# Dica: para a solução deste problem, utilize apenas o operador lógico de negação.

def maior3():
    n = int(input("Digite um valor inteiro menor que 3:"))
    if n <=3:
        print(n)


# #
# m) Efetuar a leitura de um nome (variável NOME) e o sexo (variável SEXO) de uma pessoa e
# apresentar como saída uma das seguintes mensagens:
# “Ilmo. Sr.”, caso seja informado o sexo masculino (utilizar como valor o caractere “M”), ou
# “Ilma. Sra.”, caso seja informado o sexo feminino (utilizar como valor o caractere “F”).
# Após a mensagem de saudação, apresentar o nome informado.
# O programa deve, após a entrada do sexo, verificar primeiramente se o sexo fornecido é realmente válido
# , ou seja, se é igual a “M” ou a “F”.
# Não sendo essa condição verdadeira, o programa deve apresentar a mensagem “Sexo informado inválido”

def nome():
    nome = input("Digite sue nome:")
    sexo = input("digite seu sexo M ou F")
    if sexo != "m" and sexo != "f":
        print("sexo inválido ")
    if sexo == "m":
        print("Ilmo. Sr.{}".format(nome))
    elif sexo =="f":
        print("Ilmo. Sra.{}".format(nome))


##
# n) Efetuar a leitura de três valores inteiros desconhecidos representados pelas variáveis A, B e C.
# Somar os valores fornecidos e apresentar o resultado somente se for maior ou igual a 100.

def somaValor100():
    a = int(input("Digite o valor de A:"))
    b = int(input("Digite o valor de B:"))
    c = int(input("Digite o valor de C:"))
    soma = a + b +c
    if soma >= 100:
        print(soma)
    else:
        print("Soma menor que 100")



##
# o)Ler um número inteiro qualquer e multiplicá-lo por dois.
# Apresentar o resultado da multiplicação somente se o resultado for maior que 30.

def maior30():
    num = int(input("digite uma valor inteiro:"))
    resultado = num*2
    if resultado > 30:
        print(resultado)
    else:
        print("resultado não é maior que 30")

maior30()