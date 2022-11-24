"""[Exercício 1] Escreva um programa que leia o nome completo de uma pessoa e mostre:
1)	O nome com todas as letras maiúsculas;
2)	O nome com todas as letras minúsculas;
3)	Quantas letras ao todo (sem considerar os espaços);
4)	Quantas letras tem o primeiro nome.
"""
nome = str(input("Digite um nome: "))
print(f"Seu nome em maiúsculo é: {nome.strip().upper()}")
print(f"Seu nome em mínusculo é: {nome.strip().lower()}")
print(f"Seu nome tem um total de: {len(''.join(nome.split()))} letras")
print(f"Seu primeiro nome tem um total de {len(nome.split()[0])}")

