# a)Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
# A fórmula de conversão é F ← C * 9 / 5 + 32.
def celciusFahrenheit():
    c = int(input("digite uma temperatura em graus Celsius: "))
    f = c * 9 / 5 + 32
    print("a temperatyra {}  Celsius é {} Fahrenheit".format(c, f))


# b) Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius.
# A fórmula de conversão é C ← ((F – 32) * 5) / 9.
def fahrenheit():
    f = int(input("digite uma temperatura em fahrenheits"))
    c = ((f - 32) * 5) / 9
    print("a temperatura {} fahrenheit é {} celsius".format(f, c))


# c) Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula VOLUME ← 3.14159 * R ↑ 2 * ALTURA
def volumeLata():
    r = float(input("digite o raio do cilindro: "))
    a = float(input("digite a altura do cilindro"))
    volume = 3.14159 * (r ** 2) * a
    print("Um cilindro de raio {} e altura {} tem o volume de: {} metros cubicos".format(r, a, volume))


# d) Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem,
# utilizando um automóvel que faz 12 quilômetros por litro.
# Para obter o cálculo, o usuário deve fornecer o tempo gasto (variável TEMPO)
# e a velocidade média (variável VELOCIDADE) durante a viagem.
# Dessa forma, será possível obter a distância percorrida com a fórmula DISTÂNCIA ← TEMPO * VELOCIDADE.
# A partir do valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com
# a fórmula LITROS_USADOS ← DISTÂNCIA / 12.
# O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida
# e a quantidade de litros utilizada na viagem.

def automovel():
    velocidade = float(input("Digite a velocidade do carro em km/hora: "))
    tempo = float(input("Digite o tempo da viagem em horas: "))
    distância = velocidade * tempo
    litrosGastos = distância / 12
    print("Um carro que faz 12 quilômetros por litro\ncom a velocidade média de {} Km/h e o tempo de {} horas."
          "\nPercorrerá a distância de {} quilômetros, com gasto {} litros".format(velocidade, tempo, distância,
                                                                                   litrosGastos))


# e) Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso,
# utilizando a fórmula PRESTAÇÃO ← VALOR + (VALOR * (TAXA / 100) * TEMPO).

def prestacao():
    valor = float(input("Digite o valor da prestação"))
    prestacao = valor
    taxa = float(input("Digite o valor da taxa de atraso"))
    tempo = int(input("Digite o tempo de atraso"))
    prestacao += valor * (taxa / 100) * tempo
    print("Um bem com o valor de {}R$ com a taxa da multa de {}% "
          "e com {} meses de atraso.\n A prestação será de {}.".format(valor, taxa, tempo, prestacao))


# f) Ler dois valores para as variáveis A e B e efetuar a troca dos valores de forma que a variável
# A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A.
# Apresentar os valores após a efetivação do processamento da troca.
##
def aeb():
    a1 = int(input("Digite o valor de A: "))
    b1 = int(input('Agora o de B: '))
    x = a1
    a2 = b1
    b2 = x
    print("O valor de A era {} ficou {} e o de B era {} ficou {}".format(a1, a2, b1, b2))


##

# g) Ler quatro valores numéricos inteiros e
# apresentar os resultados armazenados em memória das adições e multiplicações
# utilizando o mesmo raciocínio aplicado quando do uso de propriedades distributivas
# para a máxima combinação possível entre as quatro variáveis.
# Não é para calcular a propriedade distributiva, deve-se apenas usar a sua forma de combinação.
# Considerando a leitura de valores para as variáveis A, B, C e D,
# devem ser feitas seis adições e seis multiplicações, ou seja,
# deve ser combinada a variável A com a variável B, a variável A com a variável C, a variável A com a variável D.
# Depois, é necessário combinar a variável B com a variável C e a variável B com a variável D e,
# por fim, a variável C será combinada com a variável D.
##
def calcular(x, y):
    adição = x + y
    multiplicação = x * y
    return print("A a adição de {} com {} é {}\nA multiplicação de {} com {} é {}".format(x, y, adição, x, y
                                                                                          , multiplicação))


def adiMult():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    d = int(input("Digite o valor de d: "))
    calcular(a, b)
    calcular(a, c)
    calcular(a, d)
    calcular(b, c)
    calcular(b, d)
    calcular(d, c)


##
# h) Elaborar um programa que calcule e apresente o valor do volume de uma caixa retangular
# , utilizando a fórmula VOLUME ← COMPRIMENTO * LARGURA * ALTURA.

def volume():
    comprimento = float(input("Digite o comprimento da caixa: "))
    altura = float(input("Agora digite a altura"))
    largura = float(input("por fim digite a largura"))
    volume = comprimento * altura * largura
    print(
        "volume da caixa com comprimento {} altura {} e largura {} é {}.".format(comprimento, altura, largura, volume))


##
# i) Efetuar a leitura de um valor numérico inteiro e
# apresentar o resultado do valor lido elevado ao quadrado, sem efetuar o armazenamento do resultado em memória.

def potencia2():
    numero = int(input("digite um valor inteiro: "))
    print("O número inteiro {} elevado ao quadrado é {}".format(numero, numero * numero))


##
# j) Ler dois valores numéricos inteiros (representados pelas variáveis A e B) e apresentar o resultado
# armazenado em memória do quadrado da diferença do primeiro valor (variável A) em relação ao segundo valor (variável B)

def quadradoDaDiferença():
    a = int(input("digite um valor inteiro: "))
    b = int(input("digite outro valor inteiro"))
    resultado = a * a - b * b
    print("A diferença do quadrado de {} com o quadrado de {} é {}".format(a, b, resultado))

##
# k) Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar (US$).
# O programa deve solicitar o valor da cotação do dólar e também a quantidade de dólares disponível com o usuário
# e armazenar em memória o valor da conversão antes da apresentação.


def realDolar():
    cotação = float(input("digite a cotação do dollar: "))
    dolar = float(input("Digite a quantidade de dolares: "))
    converção= cotação*dolar
    print("Com a cotação {} a quantidade de {} dolares equivale á {} reais".format(cotação, dolar, converção))

##
#l) Elaborar um programa que apresente o valor da conversão em dólar (US$) de um valor lido em real (R$).
# O programa deve solicitar o valor da cotação do dólar
# e também a quantidade de reais disponível com o usuário
# e armazenar em memória o valor da con-versão antes da apresentação.

def dolarReal():
    cotação = float(input("digite a cotação do dollar: "))
    real = float(input("Digite a quantidade de reais: "))
    converção= real/cotação
    print("Com a cotação {} a quantidade de {} reais equivale á {} dolares".format(cotação, real, converção))

#m) Construir um programa que leia três valores numéricos inteiros (representados pelas variáveis A, B e C)
# e apresentar como resultado final, armazenado em memória, o valor da soma dos quadrados dos três valores lidos.
##

def somaDosQuadrados():
    a = int(input("Digite o valora de A: "))
    b = int(input("Digite o valora de B: "))
    c = int(input("Digite o valora de C: "))
    resultado = a**2 + b**2 + c**2
    print("A soma dos quadrados dos valores {}, {}, e {} é: {}".format(a, b, c, resultado))

#n) Construir um programa que leia três valores numéricos inteiros (representados pelas variáveis A, B e C) e
# apresentar como resultado final, armazenado em memória, o valor do quadrado da soma dos três valores lidos.
##
def quadradoDasSomas():
    a = int(input("Digite o valora de A: "))
    b = int(input("Digite o valora de B: "))
    c = int(input("Digite o valora de C: "))
    resultado = (a + b +c)**2
    print("O quadrado da soma dos valores {}, {}, e {} é: {}".format(a, b, c, resultado))


#o) Elaborar um programa que leia quatro valores numéricos inteiros (variáveis A, B, C e D).
# Ao final, o programa deve apresentar o resultado, armazenado em memória,
# do produto (variável P) do primeiro com o terceiro valor,
# e o resultado da soma (variável S) do segundo com o quarto valor.

def produtoSoma():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    d = int(input("Digite o valor de d: "))
    p = a * c
    s = b + d
    print("O produto de {} com {} é {}.\nA soma de {} com {} é {}".format(a, c, p, b, d, s))

##
#p) Elaborar um programa que leia o valor numérico correspondente ao salário mensal (variável SM) de um trabalhador
# e também fazer a leitura do valor do percentual de reajuste (variável PR) a ser atribuído.
# Apresentar o valor do novo salário (variável NS) após o armazenamento do cálculo em memória.

def salario():
    sm = float(input("Digite o valor do salário mensal do trabalhadorRS:"))
    pr = float(input("Digite o valor do percentual de reajuste:%"))
    ns = sm*pr/100 + sm
    print("O trabalhador com o salário mensal de RS:{} com o reajuste de {}%.\nSeu novo salário será de RS:{}".format
          (sm, pr, ns))


##
#q) Elaborar um programa que calcule e apresente o valor do resultado da área de uma circunferência (variável A).
#O programa deve solicitar a entrada do valor do raio da circunferência (variável R).
# Para a execução deste problema, utilize a fórmula A ← 3.14159265* R ↑ 2.
def areaCircunferencia():
    r = float(input("Digite o valor do raio da circunferência: "))
    a = 3.14159265*r**2
    print("Uma circunferência de raio {}. Sua área é de {}.".format(r, a))

##
#r)Em uma eleição sindical concorreram ao cargo de presidente três candidatos(represen-tados pelas variáveis A, B e C).
#Durante a apuração dos votos foram computados votos nulos e em branco, além dos votos válidos para cada candidato.
#Deve ser criado um programa de computador que faça

# a leitura da quantidade de votos válidos para cada candidato,
# além de ler também a quantidade de votos nulos e em branco.
# Ao final, o programa deve apresentar o número total de eleitores, considerando votos válidos, nulos e em branco;
# o percentual correspondente de votos válidos em relação à quantidade de eleitores;
# o percentual correspondente de votos válidos do candidato A em relação à quantidade de eleitores;
# o percentual correspondente de votos válidos do candidato B em relação à quantidade de eleitores;
# o percentual correspondente de votos válidos do candidato C em relação à quantidade de eleitores;
# o percentual correspondente de votos nulos em relação à quantidade de eleitores; e, por último,
# o percentual correspondente de votos em branco em relação à quantidade de eleitores.
# Todos os cálculos devem efetivamente ser armazenados em memória.


def porcentagem(x, y):
    return y/x*100


def eleição():
    a = "candidato A"
    b = "candidato B"
    c = "candidato C"
    votoA = int(input("Digite o número de votos para o candidato A:"))
    votoB = int(input("Digite o número de votos para o candidato B:"))
    votoC = int(input("Digite o número de votos para o candidato C:"))
    nulos = int(input("Digite o número de votos nulos:"))
    brancos = int(input("Digite o número de votos em brancos:"))

    votosInválidos = nulos + brancos
    votosVálidos = votoA + votoB + votoC
    totalEleitores = votosInválidos + votosVálidos

    validosEleitor = porcentagem(totalEleitores, votosVálidos)
    validosA = porcentagem(votosVálidos, votoA)
    validosB = porcentagem(votosVálidos, votoB)
    validosC = porcentagem(votosVálidos, votoC)
    nulosEleitores = porcentagem(totalEleitores, nulos)
    brancosEleiores = porcentagem(totalEleitores, brancos)

    print("Na eleição sindical o total de votos para os canditados A, B e C foram:"
          "\npara A {}\npara B {}\npara C {}\nnulos {}\nbrancos {}\n--------"
          "\ntotal de eleitores {}\n--------\nPercentuais\nválidos {:.2f}\nCandidatos\nA {:.2f}, B {:.2f}, C {:.2f}\n"
          "nulos {:.2f}, brancos {:.2f}".format(votoA, votoB, votoC, nulos, brancos, totalEleitores, validosEleitor,
                                          validosA,validosB, validosC, nulosEleitores, brancosEleiores))
##
#s)Elaborar um programa que leia dois valores numéricos reais desconhecidos representa-dos pelas variáveis A e B.
# Calcular, armazenar e apresentar os resultados das quatro operações aritméticas básicas.


def operacoesAritmeticasBasicas():
    a = float(input("Digite o primeiro valor:"))
    b = float(input("Digite o segundo valor:"))
    adicao = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    print("Operações aritméticas basicas do valor {} com {}\nAdição {:.2f}\nSubtração {:.2f}\nMultiplicação {:.2f}"
          "\nDivisão {:.2f} ".format(a, b, adicao, subtracao, multiplicacao, divisao))

##
#t) Construir um programa que calcule, armazene e apresente em metros por segundo
# o valor da velocidade de um projétil que percorre
# uma distância em quilômetros a um espaço de tempo em minutos.
# Utilize a fórmula VELOCIDADE ← (DISTÂNCIA * 1000) / (TEMPO * 60).


def velocidade():
    distancia = float(input("digite a distância percorrida pelo projétil em quilometros:"))
    tempo = float(input("digite o tempo para que o projétil percorra a distância de {} em minutos: ".format(distancia)))
    velocidade = int(distancia*1000/tempo*60)
    print("---\nA velocidade de um projétil que percorra {} quilometros no tempo de {} minutos"
          " é de {} metros por segundo ".format(distancia, tempo, velocidade))



##
#u)Elaborar um programa de computador que calcule e apresente o valor do volume de uma esfera.
# Utilize a fórmula VOLUME ← (4 / 3) * 3.14159 * (RAIO ↑ 3).

def volumeEsfera():
    raio = float(input("Digite o valor do raio da esdera: "))
    volume = 4/3*3.14*raio**3
    print("O volume de uma esfera de raio {} é {}".format(raio, volume))

##
#v)Elaborar um programa que leia dois valores numéricos inteiros,
#as quais devem representar a base e o expoente de uma potência,
# calcular a potência, armazenar em memória o resultado calculado e apresentar o resultado obtido.

def baseExpoente():
    base = int(input("Digite o número da base: "))
    expoente = int(input("Digite o expoente da potência"))
    calculo = base**expoente
    print("O número {} elevado à {} potencia é {}".format(base, expoente, calculo))

##
#w)Elaborar um programa que leia uma medida em pés, calcular, armazenar e apresentar o seu valor convertido em metros,
#lembrando que um pé mede 0,3048 metro, ou seja, um pé é igual a 30,48 centímetros.


def imperial():
    pes = float(input("Digite o valor em pés"))
    resultado = pes*0.3048
    print(" Para {} pés tempos {} metros".format(pes, resultado))


##
#x) Elaborar um programa que calcule e armazene uma raiz de base qualquer com índice qualquer.

def raiz():
    base = int(input("Digite a base do número:"))
    indice = int(input("Digite o índice"))
    raiz = base**1/indice
    print("O número {} raiz de {} é {}".format(base, indice, raiz))


##
#y)Construir um programa que leia um valor numérico inteiro e
#apresente como resultado armazenado em memória os seus valores sucessor e antecessor.


def sucessorAntecessor():
    num = int(input("Digite o numero: "))
    antecessor = num - 1
    sucessor = num + 1
    print("O antecessor do número {} é {} e o sucessor é {}".format(num, antecessor, sucessor))


##
#z)Ler dois valores numéricos inteiros (representados pelas variáveis A e B) e apresentar o
#resultado inteiro do quadrado da divisão do valor da variável A em relação ao valor da variável B
# armazenado em memória.


def quadradoDivisão():
    a = int(input("Digite o primeiro valor inteiro:"))
    b = int(input("Digite o segundo valor inteiro:"))
    resultado = (a / b)**2
    print("O quadrado da divisão de {} com {} é {}".format(a, b, resultado))

quadradoDivisão()

