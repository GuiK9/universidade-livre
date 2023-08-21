a = float(input("Digite o primeiro número "))
b = float(input("Digite o segundo número "))
c = float(input("Digite o terceiro número "))

if(c > b):
    if(b > a):
        print("crescente")
    else:
        print("não está em ordem crescente")
else:
    print("não está em ordem crescente")