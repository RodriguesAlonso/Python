'''
Problema Prático 4.1
Comece executando a atribuição:
s = '0123456789'
Agora, escreva expressões (usando s e o operador de indexação) que sejam avaliadas como:
(a)'234'
(b)'78'
(c)'1234567'
(d)'0123'
(e)'789
'''
##
s = '0123456789'
print('<==A==>'*5)
print(s[2:5])
print('<==B==>'*5)
print(s[7:9])
print('<==C==>'*5)
print(s[1:8])
print('<==D==>'*5)
print(s[:4])
print('<==E==>'*5)
print(s[7:10])

'''
Problema Prático 4.2
Supondo que a variável previsão tenha recebido a string
'It will be a sunny day today'
escreva instruções Python correspondentes a estas atribuições:
(a)À variável cont, a quantidade de ocorrências da string 'day' na string previsão.
(b)À variável clima, o índice em que a substring 'sunny' começa.
(c)À variável troca, uma cópia de previsão na qual cada ocorrência da substring 'sunny' é substituída por 'cloudy'
'''
##
s = 'It will be a sunny day today'
print('==A=='*5)
cont = s.count('day')
print(cont)
print('==B=='*5)
clima = s.find('sunny')
print(clima)
print('==C=='*5)
troca = s.replace('sunny', 'cloudy')
print(troca)