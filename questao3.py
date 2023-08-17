"""
3) Crie um dicionário que é uma agenda e coloque nele os seguintes dados:
chave (cpf), nome, idade, telefone. O programa deve ler um número
indeterminado de dados, criar a agenda e imprimir todos os itens do
dicionário no formato chave: nome-idadefone.
"""

agenda = {}

while True:
    cpf = int(input('Digite o cpf: '))
    nome = input("digite o nome: ")
    idade = int(input("Digite a idade: "))
    telefone = int(input("digite o telefone: "))
    agenda[cpf] = + nome +' -' + str(idade) + ' -' + str(telefone)
    continuar = input('Deseja continuar? [S/N]')
    if continuar in 'Nn':
        break

print(agenda)