from random import randint
from time import sleep
import os

cont = 0
#estou defindo uma função para separar entre anuciado do programa/tentativas/conclusão
def lin():
    print("-="*30)

#estou fazendo uma variavel para guardar o numero escolhido pela função randint(computador)
Ncomp = randint(0,100)

lin()
print(f"{'JOGO DA ADIVINHAÇÃO':>38}")
lin()
sleep(3)
os.system("cls")

#inicio das tentativas
print("Olá eu sou o seu computador, Você consegue advinhar qual numero estou pensando. ")
esc = int(input("O numero que estou pensando é : "))
while True:
    cont += 1
    if esc > Ncomp:
        esc = int(input("Chute um valor MENOR !"))
        continue
    elif esc < Ncomp:
        esc = int(input("Chute um valor MAIOR !"))
        continue
    elif esc == Ncomp:
        break
    esc = int(input("Tente novamente: "))
os.system("cls")
#conclusão
lin()
if cont == 1:
    print("PARABENS VOCÊ CONSEGUIU ADIVINHAR MEU NUMERO COM APENAS UMA TENTATIVA !")
else:
    print(f"PARABENS VOCÊ CONSEGUIU ADIVINHAR MEU NUMERO  COM {cont} TENTATIVAS")
lin()