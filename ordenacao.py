import math

numero1 = int(input("Digite pimeiro numero inteiro: "))
numero2 = int(input("Digite segundo numero inteiro: "))
numero3 = int(input("Digite terceiro numero inteiro: "))

if numero1 < numero2 and numero2 < numero3:
    print("crescente")
else:
    print("não está em ordem crescente")