# Calculando distância entre dois pontos num espaço de 3 dimensões
import math
A=float(input("Entre com um valor para A:"))
B=float(input("Entre com um valor para B:"))
C=float(input("Entre com um valor para C:"))

X=float(input("Entre com um valor para X:"))
Y=float(input("Entre com um valor para Y:"))
Z=float(input("Entre com um valor para Z:"))

dist_AB = math.sqrt(((X*B-X*A)**2)+((Y*B-Y*A)**2)+((Z*B-Z*A)**2))
print("A distância entre A e B é:", dist_AB)
