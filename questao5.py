"""
5) Considere um sistema onde os dados são armazenados em dicionários.
Nesse sistema existe um dicionario principal e o dicionário de backup.
Cada vez que o dicionário principal atinge tamanho 5, ele imprime os
dados na tela e apaga o seu conteúdo. Crie um programa que insira dados
em um dicionário, realizando o backup a cada dado e excluindo os dados
do dicionário principal quando ele atingir tamanho 5.

"""

def fazer_backup(dados, backup):
    backup.update(dados)
    dados.clear()


dicionarioP = {}
dicionarioB = {}



while True:

    chave = input("Digite o Nome ou 'Sair' para encerrar: ")

    if chave == 'sair':
        break

    idade = int(input('idade: '))
    
    dicionarioP[chave] = idade
    
    
    if len(dicionarioP) >= 5:
        print("Dicionário principal atingiu tamanho 5. Fazendo backup...")
        fazer_backup(dicionarioP, dicionarioB)
    
    print("Dicionário Principal:", dicionarioP)
    print("Dicionário de Backup:", dicionarioB)

print("Encerrando o programa.")
       

"""
def fazer_backup(dados, backup):
    backup.update(dados)
    dados.clear()

dict_principal = {}
dict_backup = {}

while True:
    chave = input("Digite a chave (ou 'sair' para encerrar): ")
    
    if chave == 'sair':
        break
    
    valor = input("Digite o valor: ")
    
    dict_principal[chave] = valor
    
    if len(dict_principal) >= 5:
        print("Dicionário principal atingiu tamanho 5. Fazendo backup...")
        fazer_backup(dict_principal, dict_backup)
    
    print("Dicionário Principal:", dict_principal)
    print("Dicionário de Backup:", dict_backup)

print("Encerrando o programa.")
"""
       
