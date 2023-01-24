"""Resumo
O algoritmo de validação do CPF calcula o primeiro dígito verificador a partir dos 9 primeiros dígitos do CPF, e em seguida, calcula o segundo dígito verificador a partir dos 9 (nove) primeiros dígitos do CPF, mais o primeiro dígito, obtido na primeira parte.

Exemplo
Vamos usar como exemplo o CPF fictício : 111.444.777-35.

1. Cálculo do Primeiro Dígito
O primeiro passo é calcular o primeiro dígito verificador, e para isso, separamos os primeiros 9 dígitos do CPF (111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2, como no exemplo abaixo :

| 1 | 1 | 1 | 4 | 4 | 4 | 7 | 7 | 7 |
| - | - | - | - | - | - | - | - | - |
| 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
| 10 | 9 | 8 | 28 | 24 | 20 | 28 | 21 | 14 |

Multiplicamos cada digito do CPF pelo respectivo número e somamos cada um dos resultados : 10 + 9 + 8 + 28 + 24 + 20 + 28 + 21 + 14 = 162

Pegamos o resultado obtido 162 e dividimos por 11.  Consideramos como quociente apenas o valor inteiro.

162 / 11  =    14  com resto 8

- Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
- Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).

No nosso exemplo temos que o resto é 8 então faremos 11 - 8 = 3

Logo o primeiro dígito verificador é 3. Então podemos escrever o CPF com os dois dígitos calculados :  111.444.777-3X

2. Cálculo do Segundo Dígito
Para  calcular o segundo dígito vamos usar o primeiro digito já calculado. Vamos montar a mesma tabela de multiplicação usada no cálculo do primeiro dígito. Só que desta vez usaremos na segunda linha os valores 11, 10, 9, 8, 7, 6, 5, 4, 3, 2 já que estamos incluindo mais um digito no cálculo(o primeiro dígito calculado):

| 1 | 1 | 1 | 4 | 4 | 4 | 7 | 7 | 7 | 3 |
| - | - | - | - | - | - | - | - | - | - |
| 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
| 11 | 10 | 9 | 32 | 28 | 24 | 35 | 28 | 21 | 6 |

Novamente, efetuamos somamos o resultado da multiplicação : 11 + 10 + 9 + 32 + 28 + 24 + 35 + 28 + 21 + 6 = 204

Dividimos o total do somatório por 11 e consideramos o resto da divisão.

204 / 11  =  18  e  resto 6

Após obter o resto da divisão, precisamos aplicar a mesma regra que utilizamos para obter o primeiro dígito:

- Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
- Se o resto da divisão for maior ou igual a 2, então o dígito é igual a 11 menos o resto da divisão (11 - resto).

11 - 6 = 5   logo 5 é o nosso segundo dígito verificador.

Logo o nosso CPF fictício será igual a : 111.444.777-35.
"""
while True:
    # um loop para verificar se o usuário deseja validar cpf ou encerrar o programa.
    op = int(input("""Escolha a opção que deseja realizar:
            [1] Validar CPF
            [0] Encerrar o Programa"""))
    # opções para o usuário escolher o que deseja fazer.

    if not type(op) is int:
        # se não for do tipo int levanta um erro.
        raise TypeError("Apenas números inteiros são permitidos")

    if op == 0:
        # caso o usuário selecione 0 o program é encerrado.
        break

    cpf = input(
        "Digite um CPF para verificar se é válido(CPF é composto por 11 números): ")
    # valor de um cpf que é válido, pra testes = '11144477735'

    cpfCorrigido = cpf
    cpfCorrigido.replace('.', '').replace('-', '')
    # substitui pontuação de cpf para poder fazer cálculo e comparações posteriores.

    """def tratamentoDeErro():
        # tratamentos de erros de digitação de usuário
        if:"""

    valor = primeiroDigito = segundoDigito = 0
    # inicializando valores e primeiro digito em 0 para serem alterados posteriormente.
    multiplicador1 = 10
    soma = 0
    for num in cpfCorrigido[:9]:
        # faz cálculo dos primeiros 9 números digitados pelo usuário para descobrir o digito 10
        resultado = int(num) * multiplicador1
        multiplicador1 -= 1
        soma += resultado

    valor = soma % 11

    if valor < 2:
        primeiroDigito = 0
    else:
        primeiroDigito = 11 - valor

    multiplicador2 = 11
    soma2 = 0
    for num2 in cpfCorrigido[:10]:
        # faz segundo cálculo, ou seja dos 10 números para descobrir o 2 dígito final do cpf
        resultado = int(num2) * multiplicador2
        multiplicador2 -= 1
        soma2 += resultado

    valor2 = (soma2 % 11)
    if valor2 < 2:
        segundoDigito = 0
    else:
        segundoDigito = 11 - valor2

    digitosCpf = cpfCorrigido[:9] + str(primeiroDigito) + str(segundoDigito)
    # pega os 9 digitos do cpf digitados pelo usuário, atribui a eles os 2 números descobertos atráves de cálculos anteriores
    print(digitosCpf)

    if cpfCorrigido == digitosCpf:
        # compara o cpf digitado com o calculado para validar e verificar se está correto ou é inválido
        print("O CPF está correto.")
    else:
        print("O CPF informado, não é válido.")
