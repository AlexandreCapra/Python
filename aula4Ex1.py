"""[Exercício 1] Escreva um programa que o computador
pensará em um número entre 0 e 5. Em seguida, o usuário
deverá adivinhar esse valor. Caso o usuário acerte,
retorne “VENCEU”, caso perca, retorne “PERDEU”."""
import random
maquina = random.randint(0, 5)
jogador = int(input("Vamos jogar um jogo, tente advinhar um número entre 0 e 5: "))


if jogador == maquina:
    print(f"Parabéns você \033[1;32mAcertou\033[m, você escolheu {jogador} e a máquina escolheu {maquina}")
else:
    print(f"Você \033[1;31mErrou\033[m, pois escolheu {jogador} e a máquina escolheu {maquina}")