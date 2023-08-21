import math

a = float(input("Digite um valor inteiro"))
a = math.ceil(a)

if(a % 2 == 0):
    print ("par")
else: 
    print("Ímpar")