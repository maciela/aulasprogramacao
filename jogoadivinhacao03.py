# Jogo de Adivinhação - versão 03

from random import randint
secret = randint(1,10)
print("Bem vindo!")
palpite = 0

while palpite != secret:
    palpite = int(input("Digite um número: "))
    if palpite == secret:
        print("Você Ganhou!")
    else:
        if palpite > secret:
            print("muito alto")
        else:
            print("muito baixo")
print("Fim de jogo!")
