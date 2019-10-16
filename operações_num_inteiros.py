#Operações com numeros inteiros

num = 0
i = 1
cont_par = 0
cont_impar = 0
somapar = 0
somarimpar = 0

for i in range(10):

    num = int(input("Digite um número inteiro:"))
    resto = num % 2
    if resto == 0:
        cont_par = cont_par+1
        somapar = somapar+num
    else:
        cont_impar = cont_impar+1
        somarimpar = somarimpar+num
        med = somarimpar/cont_impar
        medarred = round(med, 2)

print(" O número de inteiros pares é:", cont_par)
print(" O número de inteiros ímpares é:", cont_impar)
print("Soma dos números pares é", somapar)
print("Soma dos números impares é", somarimpar)
print("A média dos números ímpares é", medarred)
