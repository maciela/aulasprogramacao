# Jogo de Adivinhação - versão 02

print("Bem vindo!")
g = input("Digite um número: ")
número = int(g)
if número ==5:
    print("Você Ganhou!")
else:
    if número > 5:
        print("muito alto")
    else:
        print("muito baixo")
print("Fim de jogo!")
