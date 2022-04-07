#while -> laço de comando 
i = 0

while i <= 10:
    print(2 ** i)
    i = i + 1

print("*" * 60)

val = int(input('Digite quantos numeros quer informar: '))

v = 0
soma = 0
while v < val:
    valor = float(input('Digite um valor: '))
    soma = soma + valor
    v = v + 1
print('A soma dos valores é:', soma)    

print("*" * 60)


