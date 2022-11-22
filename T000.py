while True:

    resposta = str(input("Deseja continuar [S/N]?")).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input(f"\033[31mRESPOSTA INVÁLIDA.\033[m\nDeseja continuar [S/N]?")).upper().strip()[0]

    if resposta == 'N':
        break

print(f"{f'='*20}\n\033[34m{f'FIM DO PROGRAMA':^20}\033[m\n{f'='*20}")