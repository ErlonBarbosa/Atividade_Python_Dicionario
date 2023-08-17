"""
8) Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
Escreva um programa que leia todos os tempos em segundos e os guarde
em um dicionário, onde a chave é o nome do corredor. Ao final diga de
quem foi a melhor volta da prova e em que volta; e ainda a classificação
final em ordem (1o o campeão). O campeão é o que tem a menor média
de tempos.
"""

import random


def calcular_media(tempos):
    return sum(tempos) / len(tempos)

num_corredores = 6
num_voltas = 10


tempos_corredores = {}


for i in range(num_corredores):
    nome_corredor = f"Corredor {i + 1}"
    tempos = [random.randint(60, 120) for _ in range(num_voltas)] 
    tempos_corredores[nome_corredor] = tempos


melhor_volta = float('inf')
melhor_corredor = None
melhor_volta_num = None

for nome, tempos in tempos_corredores.items():
    volta_melhor_tempo = min(tempos)
    if volta_melhor_tempo < melhor_volta:
        melhor_volta = volta_melhor_tempo
        melhor_corredor = nome
        melhor_volta_num = tempos.index(volta_melhor_tempo) + 1


classificacao_final = sorted(tempos_corredores.keys(), key=lambda nome: calcular_media(tempos_corredores[nome]))


print(f"Melhor volta da prova: {melhor_corredor}, Volta: {melhor_volta_num}, Tempo: {melhor_volta} segundos")
print("Classificação final:")
for posicao, corredor in enumerate(classificacao_final, start=1):
    media_tempo = calcular_media(tempos_corredores[corredor])
    print(f"{posicao}º lugar: {corredor}, Média de tempo: {media_tempo:.2f} segundos")