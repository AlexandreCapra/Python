"""
[Exercício 1] Escreva um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
           "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
           "dezoito", "dezenove", "vinte")

while True:
    n = int(input("Digite um número para mostrar seu valor por extenso. Número entre 0 e 20: "))
    while n not in range(0, 20):
        n = int(input("RESPOSTA INVÁLIDA!\nDigite um número para mostrar seu valor por extenso. Número entre 0 e 20: "))

    print(numeros[n])
    resposta = str(input("Deseja continar [S/N]")).upper().strip()[0]

    while resposta not in "SN":
        resposta = str(input("Resposta inválida. Só pode [S/N].\nDeseja continar [S/N]")).upper().strip()[0]

    if resposta == 'N':
        break
print("--FIM--")


