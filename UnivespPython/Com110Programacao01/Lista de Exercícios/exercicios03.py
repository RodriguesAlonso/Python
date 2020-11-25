##
# a) Elaborar um programa que apresente como resultado
# os quadrados armazenados na memória dos números inteiros existentes na faixa de valores de 15 a 200.


def quadrado200():
    cont = 15
    colunas = 0
    lista = []
    while cont <= 200:
        while colunas < 5:
            y = cont**2
            lista.append(y)
            cont += 1
            colunas += 1
        print(lista)
        lista.append("\n teste\nteste")
        lista.clear()
        colunas = 0


##
# b) Elaborar um programa que mostre os resultados da tabuada de um número qualquer,
# a qual deve ser apresentada de acordo com sua forma tradicional.


def tabuada():
    x = int(input("digite o numero da tabuada:"))
    cont = 0
    while cont <= 10:
        calculo = x*cont
        print(x, " X ", cont, "=", calculo)
        cont += 1


##
# c) Construir um programa que apresente a soma dos cem primeiros números naturais (1 + 2 + 3 +...+ 98 + 99 + 100).


def soma100():
    i = 0
    soma = 0
    while i <= 100:
        soma += i
        i += 1
    print(soma)


##
# d) Elaborar um programa que apresente o somatório dos valores pares existentes na faixa de 1 até 500.

def soma500par():
    i = 0
    soma = 0
    while i <= 500:
        if i % 2 == 0:
            soma += i
        i += 1
    print(soma)


##
# e) Elaborar um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20.
# Sugestão: para verificar se o valor numérico é ímpar, dentro do laço de repetição, fazer a verificação lógica
# dessa condição com a instrução se/fim_se dentro do próprio laço, perguntando se o valor numérico do contador é ímpar
# (se o resto do número dividido por 2 é diferente de zero);
# sendo, mostre-o; não sendo, passe para o próximo valor numérico.

def soma20impar():
    i = 0
    soma = 0
    while i <= 20:
        if i % 2 != 0:
            soma += i
        i += 1
    print(soma)

##
# f) Construir um programa que apresente todos os valores numéricos divisíveis por 4 e menores que 200.
# Sugestão: a variável que controla o contador do laço deve ser iniciada com valor 1.


def div4emenor200():
    i = 1
    while i < 200:
        if i % 4 == 0:
            print(i)
        i += 1

##
# g) Elaborar um programa que apresente os resultados das potências do valor de base 3,
# elevado a um expoente que varie do valor 0 até o valor 15.
# O programa deve apresentar os valores 1, 3, 9. 27, ..., 14.348.907.
# Sugestão: leve em consideração as definições matemáticas do cálculo de potência,
# em que qualquer valor numérico diferente de zero elevado a zero é 1, etodo valor numérico elevado a 1 é ele próprio.
# Não use o operador aritmético de exponenciação apresentado no Capítulo 3; resolva o problema com a técnica de laço.


def potenciaBase3():
    i = 0
    lista = []
    while i <= 15:
        lista.append(3**i)
        i += 1
    print(lista)

##
# h) Escrever um programa que apresente como resultado a potência de uma base qualquer elevada a um expoente qualquer,
# ou seja, de BE, em que B é o valor da base e E o valor do expoente.
# Considere apenas a entrada de valores inteiros e positivos, ou seja,de valores naturais.
# Sugestão: não utilize o formato “base ↑ expoente”, pois é uma solução muito trivial.
# Use a técnica de laço, em que o valor da base deve ser multiplicado o número de vezes determinado no expoente.


def expoente():
    b = int(input("Digite a base:"))
    e = int(input("Digite o expoente:"))
    i = e
    while i > 0:
        resultado = b * b
        i -= 1
    print("{} elevado a {} é : {}".format(b, e, resultado))

##
# i) Escrever um programa que apresente os valores da sequência numérica de Fibonacci até o décimo quinto termo.
# A sequência de Fibonacci é formada pelos valores numéricos
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, ... etc.,
# obtendo-se o próximo termo a partir da soma do termo atual com o anterior sucessivamente
# até o infinito se a sequência não for interrompida, sendo determinada a partir da
# fórmula Fn para este exercício as variáveis ATUAL, ANTERIOR e PRÓXIMO. = Fn-1 + Fn-2 . Utilize


def fibonacci():
    i = 1
    a = 0
    b = 1

    fibonacciLista = []
    while i <= 15:
        soma = a + b
        fibonacciLista.append(soma)
        a = b
        b = soma
        i += 1
    print(fibonacciLista)

##
# j) Elaborar um programa que apresente os valores de conversão de graus Celsius em graus Fahrenheit,
# de dez em dez graus, iniciando a contagem em dez graus Celsius e finalizando em cem graus Celsius.
# O programa deve apresentar os valores das duas temperaturas.


def celciusFahrenheit():
    c = 0
    while c <= 100:
        f = c * 9 / 5 + 32
        print("a temperatyra {}  Celsius é {} Fahrenheit".format(c, f))
        c += 10


##
# k) Escrever um programa que calcule e apresente o somatório do número de grãos de trigo
# que se pode obter em um tabuleiro de xadrez, obedecendo à seguinte regra:
# colocar um grão de trigo no primeiro quadro, e nos quadros seguintes, o dobro do quadro anterior. Ou seja,
# no primeiro quadro coloca-se um grão, no segundo quadro colocam-se dois grãos (neste momento têm-se três grãos),
# no terceiro quadro colocam-se quatro grãos (tendo neste momento sete grãos),
# no quarto quadro colocam-se oito grãos (tendo-se, então, 15 grãos), até atingir o sexagésimo quarto quadro18 .


def trigoXadrez():
    t = 1
    q = 64
    while q > 0:
        t *= 2
        q -= 1
        print(t)

##
# l) Elaborar um programa que leia quinze valores numéricos inteiros e
# no final apresente o somatório da fatorial de cada valor lido.


def fatorial(x):
    cont = x
    fat = 1
    while cont > 0:
        fat *= cont
        cont -= 1
    return fat


def leia15Fatarial():
    i = 1
    soma = 0
    fat = 0
    while i <= 15:
        print("Imput: {}".format(i))
        valor = int(input("digite um valor:"))
        fat = fatorial(valor)
        soma += +fat
        print("O fatorial de {} é {} somando com o fatorial anterior é: {}".format(valor, fat,  soma))
        i +=1

##
# m) Elaborar um programa que leia dez valores numéricos reais e
# apresente no final o somatório e a média dos valores lidos.


def leia10media():
    i = 1
    soma = 0
    while i <=10:
        print("Imput: {}".format(i))
        valor = int(input("Digite um valor:"))
        soma += valor
        i += 1
    print("A soma é {} e a media dos valores inseridos é {}".format(soma, soma / 10))

##
# n) Elaborar um programa que leia sucessivamente valores numéricos e
# apresente no final o somatório, a média e o total de valores lidos.
# O programa deve ler os valores enquanto o usuário estiver fornecendo valores positivos.
# Ou seja, o programa deve parar quando o usuário fornecer um valor negativo (menor que zero).


def mediaPositivo10():
    i = 1
    soma = 0
    valor = 1
    while valor > 0:
        print("Imput: {}".format(i))
        i += 1
        valor = int(input("Digite um valor:"))
        if valor > 0:
            soma += valor

    print("A soma é {} e a media dos valores inseridos é {}".format(soma, soma / (i-1)))

##
# o) Construir um programa que
# apresente como resultado a fatorial dos valores ímpares situados na faixa numérica de 1 até 10.



def fatorial10():
    i = 1
    while i <= 10:

        if i % 2 != 0:
            fat = fatorial(i)
            print("O farorial de {} é {}".format(i, fat))
        i += 1

##
# p) Elaborar um programa que apresente
# os resultados da soma e da média aritmética dos valores pares situados na faixa numérica de 50 até 70.


def somaMedia50e70():
    i = 50
    soma = 0
    while i <=70:
        if i % 2 == 0:
            soma += i
            print(soma)
        i += 1
    print("A soma é {} e a média é {}".format(soma, soma/20))


##
# q) Escrever um programa que possibilite calcular a área total em metros de uma residência com os
# cômodos sala, cozinha, banheiro, dois quartos, área de serviço, quintal, garagem, entre outros
# que podem ser fornecidos ao programa.
# O programa deve solicitar a entrada do nome, da largura e do comprimento de um determinado cômodo.
# Em seguida, deve apresentar a área do cômodo lido
# e também uma mensagem solicitando ao usuário a confirmação de continuar calculando novos cômodos.
# Caso o usuário responda “NÃO”,
# o programa deve apresentar o valor total acumulado da área residencial.

def residenciaTotal():
    solicitacao = "sim"
    while solicitacao == "sim":
        nome = input("Digite o nome do comodo:")
        largura = float(input("Digite a largura:"))
        comprimento = float(input("Digite o comprimento"))
        area = largura*comprimento
        print("A area do comodo {} com largura de {} e comprimento de {} é {}".format(nome, largura, comprimento, area))
        solicitacao = input("Deseja continuar continuar calculando novos cômodos ? ")

##
# r) Elaborar um programa que leia valores positivos inteiros até que um valor negativo seja informado.
# Ao final devem ser apresentados o maior e o menor valores informados pelo usuário.


def maiorMenorpositivo():
    numero = 1
    numero1 = 0
    while numero >= 0:
        numero02 = numero1
        numero1 = numero
        if numero1 >= numero02:
            maior = numero1
            menor = numero02
        else:
            maior = numero02
            menor = numero1

        numero = int(input("Digite o número inteiro: "))
    print("O número maior é {} e o menor {}".format(maior, menor))


##
# s) Elaborar um programa que apresente o resultado inteiro da divisão de dois números quaisquer,
# representando o dividendo e o divisor da divisão a ser processada.
# Sugestão: para a elaboração do programa, não utilize o operador aritmético de divisão com quociente inteiro div.
# Use uma solução baseada em laço.
# O programa deve apresentar como resultado (quociente) quantas vezes o divisor cabe no dividendo.


def inteiroDivisao():
    dividendo = int(input("Digite o dividendo:"))
    divisor = int(input("Digite o divisor:"))
    quociente = 1
    resultado = 1
    while resultado != 0:
        divisao1 = (quociente * divisor) - dividendo
        if quociente > dividendo:
            print("Divisão com resultado real")
            print(dividendo/divisor)
            break
        if divisao1 == 0:
            resultado = 0
        else:
            quociente += 1
    if resultado == 0:
        print("O quociente da divisão {} com {} é {}".format(dividendo, divisor, quociente))

inteiroDivisao()
##
# t) Elaborar um programa que apresente os quadrados sem armazená-los na memória dos valores inteiros existentes
# na faixa de valores de 15 a 200 com saltos de 3 em 3.


def quadradosFaixa15a200():
    cont = 15
    while cont <= 200:
        print(cont*cont)
        cont += 3

