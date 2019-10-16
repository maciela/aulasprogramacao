# Raízes de uma equação do 2º grau
import math

a = float(input("Entre com um valor para a:"))
b = float(input("Entre com um valor para b:"))
c = float(input("Entre com um valor para c:"))
delta = (b**2)-4*a*c
if delta < 0:
    print("A equação não possui raízes reais")
elif delta == 0:
    raiz = (-b + math.sqrt(delta)) / (2 * a)
    print("A raiz da equação é: ",raiz)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print("As raízes são:", raiz1,"e", raiz2)
