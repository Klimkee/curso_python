"""
Exercício 
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba: "Desculpe, você deixou campos vazios."
"""
nome_1 = input('Digite seu nome:')
idade_1 = input('Qual sua idade?:')

if ' ' in nome_1: 
    print('Seu nome contém espaços')
elif nome_1: 
    print('Seu nome não contém espaços')

if nome_1 and idade_1:
    print(f'Seu nome é {nome_1}')
    print('Seu nome invertido é'f' {nome_1 [::-1]}')
    print(f'Seu nome tem {len(nome_1)} letras')
    print(f'A primeira letra do seu nome é:{nome_1[:1:]}')
    print('A última letra do seu nome é:' f' {nome_1 [-1]}')

else: 
    print('Desculpe, você deixou campos vazios.')
