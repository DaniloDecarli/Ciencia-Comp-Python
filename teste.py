n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))

def maior(n1, n2):
    if n1 > n2:
        return n1
    else:    
        return n2
print("maximo",(n1, n2))
print(maior(n1,n2))    