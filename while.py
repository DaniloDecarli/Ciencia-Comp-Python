num = int(input('Digite um número inteiro: '))

decrescente = True
valor = 1
while valor != 0 and decrescente:
    valor = int(input('Digite o próximo número inteiro: '))
    if valor > num:
        decrescente = False
if decrescente:
    print('A sequência está me ordem decrescente!')
else:
    print('A sequência não está me ordem decrescente!')    


