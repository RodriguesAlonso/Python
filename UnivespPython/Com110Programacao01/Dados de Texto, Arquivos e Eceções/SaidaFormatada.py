'''
Problema Prático 4.3
Escreva uma instrução que exibe os valores das variáveis último, primeiro e meio em uma linha,
separadas por um caractere de tabulação horizontal.
(A sequência de escape Python para o caractere de tabulação horizontal é \t.)
Se as variáveis são atribuídas desta forma:
último = 'Smith'
primeiro = 'John'
meio = 'Paul'
a saída deverá ser:
Smith   John   Paul
'''
##
ultimo = 'Smith'
primeiro = 'John'
meio = 'Paul'
print(ultimo, primeiro, meio, sep='\t')
'''
Problema Prático 4.4
Escreva a função par() que toma um inteiro positivo n como entrada e exibe na tela todos os números entre 2 (inclusive) 
e n, que sejam divisíveis por 2 ou por 3, usando este formato de saída:
>>> even(17)
2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16,
'''
##
def par(n):
    for x in range(2, n + 1):
        if x % 2 == 0 or x % 3 ==0:
            print(x, end=', ')

'''
Problema Prático 4.5
Suponha que as variáveis primeiro, último, rua, número, cidade, estado, codPostal já tenham sido atribuídas. 
Escreva uma instrução print que crie uma etiqueta de correspondência:
John Doe
123 Main Street
AnyCity, AS 09876
supondo que:
primeiro = 'John'
último = 'Doe'
rua = 'Main Street'
número = 123
cidade = 'AnyCity'
estado = 'AS'
codPostal = '09876'
'''
primeiro = 'John'
ultimo = 'Doe'
rua = 'Main Street'
numero = 123
cidade = 'AnyCity'
estado = 'AS'
codPostal = '09876'

print('{} {}\n{}, {}\n{}, {} {}'.format(primeiro, ultimo, numero, rua, cidade, estado, codPostal))