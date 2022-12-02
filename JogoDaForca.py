"""
[Exercício 2] Faça o jogo da forca em Python. Porém, apenas com os conhecimentos aprendidos até agora.

"""

import random
import re


#Cria uma lista de palavras, das quais vai selecionar uma delas aleatoriamente, para ela fazer parte do jogo

palavras = ["cachorro", "gato", "passaro", "banana", "carro", "concreto", "godzilla", "celular"]
tentativas = 0 #numero de tentativas
print("JOGO DA FORCA\n Você só pode errar 6 vezes, boa sorte")

#escolhe palavra aleatoria para a forca
palavraEscolhida = random.choice(palavras).upper()
tentativasRestante = 6
letrasErradas = []

"""Transforma a palavra aleatória da forca em ---------- em uma palavra com pontilhados esperando as letras serem descobertas
   sendo assim, depois vai substituindo as simbolos pelas letras conforme o usuário for descobrindo.
"""
#palavraIncognita = palavraEscolhida.replace("\w", "-").upper()
palavraIncognita = re.sub("\w","-", palavraEscolhida)
fimDeJogo = False
while True:
    print(palavraIncognita)
    print(f"Letras que você errou da palavra: {letrasErradas}")
    letraTentativa = str(input("Digite uma letra pra adivinhar a palavra: ")).upper().strip()[0]

    if letraTentativa not in palavraIncognita:
        if letraTentativa not in palavraEscolhida:
            if letraTentativa not in letrasErradas:
                letrasErradas.append(letraTentativa)
            else:
                print(f"Você já escreveu essa letra anteriormente: {letraTentativa}.")
            tentativas += 1
            tentativasRestante -= 1
            print(f"Errou perdeu {tentativas} chances de 6 e agora tem só mais {tentativasRestante}")

            if tentativas == 6:
                print(f"Acabaram suas chances você usou {tentativas}, fim de jogo a palavra era {palavraEscolhida}.")
                fimDeJogo = True

        elif letraTentativa in palavraEscolhida:
            indices = [i for i, x in enumerate(palavraEscolhida) if x == letraTentativa]
            temp = list(palavraIncognita)
            for indice in indices:
                temp[indice] = letraTentativa
            palavraIncognita = "".join(temp)
    else:
        print(f"A letra {letraTentativa} já existe, digite uma letra diferente. ")
    if palavraEscolhida == palavraIncognita:
        print(f"Parabéns você descobriu a palavra: {palavraEscolhida}")
        fimDeJogo = True

    if fimDeJogo:
        resposta = str(input("Deseja continuar[S/N]?")).upper().strip()[0]
        while resposta not in 'SN':
            resposta = str(input(f"\033[31mRESPOSTA INVÁLIDA.\033[m\nDeseja continuar [S/N]?")).upper().strip()[0]

        if resposta == 'N':
            break
        if resposta == 'S':
            tentativas = 0
            tentativasRestante = 6
            fimDeJogo = False
            letrasErradas = []
            palavraEscolhida = random.choice(palavras).upper()
            palavraIncognita = re.sub("\w", "-", palavraEscolhida)
print(f"{f'='*30}\n\033[33m{f'FIM DO JOGO DA FORCA, ATÉ MAIS':^20}\033[m\n{f'='*30}")

