nome = str(input("Digite seu nome: "))
fim = False
op = int
while not fim:

    while op:

        print("=-=" * 20)
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite um número: "))
        print(f"""Olá, {nome}, o que você deseja fazer:
        [1] Somar 
        [2] Subtrair 
        [3] Dividir 
        [4] Multiplicar 
        [5] Zerar resultado
        [6] Sair 
        """)
        print("=-=" * 20)

        op = int(input("Escolha uma opção: "))

        if op == 1:
            resultado = n1 + n2
            print(f"{n1} + {n2} = {resultado}")


        elif op == 2:
            resultado = n1 - n2
            print(f"{n1} - {n2} = {resultado}")


        elif op == 3:
            resultado = n1 / n2
            print(f"{n1} / {n2} = {resultado}")


        elif op == 4:
            resultado = n1 * n2
            print(f"{n1} * {n2} = {resultado}")



        elif op == 5:
            resultado = 0
            print(f" Zerado = {resultado}")


        elif op == 6:
            fim = True
            print("Você escolheu encerrar o programa é o fim.")
            break
        else:
            print("Opção inválida")
            print("=-=" * 20)
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite um número: "))
            print(f"""Olá, {nome}, o que você deseja fazer:
                [1] Somar 
                [2] Subtrair 
                [3] Dividir 
                [4] Multiplicar 
                [5] Zerar resultado
                [6] Sair 
                """)
            print("=-=" * 20)

            op = int(input("Escolha uma opção: "))
