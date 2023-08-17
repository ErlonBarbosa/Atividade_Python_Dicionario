"""
6) Escreva uma função que conta a quantidade de vogais em um texto e
armazena tal quantidade em um dicionário, onde a chave é a vogal
considerada.

"""



def cont_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador_vogais = {}

    for letra in texto:
        if letra in vogais:
            if letra in contador_vogais:
                contador_vogais[letra] += 1
            else:
                contador_vogais[letra] = 1
    
    return contador_vogais

texto = "Esta é uma frase de exemplo contando vogais."
resultado = cont_vogais(texto)

for vogal, quantidade in resultado.items():
    print(f"A vogal '{vogal}' aparece {quantidade} vezes.")

 