"""
4) Crie um programa que cadastre informações de várias pessoas (nome,
idade e cpf) e depois coloque em um dicionário. Depois remova todas as
pessoas menores de 18 anos do dicionário e coloque em outro dicionário.

"""

dicionario = {}
dicionario2 = {}

while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = int(input("CPF: "))

    if idade > 18:
        dicionario["Nome"] = nome
        dicionario["Idade"] = idade
        dicionario["CPF"] = cpf

    else:
        dicionario2["Nome"] = nome
        dicionario2["Idade"] = idade
        dicionario2["CPF"] = cpf
    continuar = input('Deseja continuar? [S/N]')
    if continuar in 'Nn':
        break

print(f'Maiores de 18 anos {dicionario}')
print(f'Menores de 18 anos {dicionario2}')
