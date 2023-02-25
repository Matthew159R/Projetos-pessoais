import re

title_posts = [
    'O que são buracos negros e como eles funcionam',
    'Como as estrelas morrem',
    'Por que a galáxia de andrômeda e a via lactea vão se colidir um dia',
    'Teorias de como o universo vai acabar',
    'Como o universo surgiu',
    'O maior buraco negro já descoberto [Phoenix Cluster]',
    'O que é a energia e matéria escura?',
    'Como viajar no tempo',
    'Como será o futuro? Um futuro bem distante? [Ano de 2000024]',
    'Como sobreviver a uma ilha deserta, o guia',
    'Como funciona um motor de dobra espacial',
    'Escala Kardashev, os 6 tipos de civilizações',
    ''
]
while True:
    def Pesquisar():
        entrada = input("Pesquisar...🔎")

#-
        Condição_caracter_especial =  re.match("^[a-zA-Z0-9 áàãâéêíóôõúç.,?!:;()-]*$", entrada)

        Procuras_correspondentes = []

        for Procura in title_posts:
            if entrada.lower() in Procura.lower():
                Procuras_correspondentes.append(Procura)

        if Procuras_correspondentes:
            print("Resultados da busca:")
            print()
            for Procura in Procuras_correspondentes:
                espaço = '-' * len(Procura)
                Destaque_na_pesquisa = Procura.lower().replace(entrada.lower(), f"\033[1m{entrada.lower()}\033[0m")
                print(f'I{espaço}I')
                print(f'|{Destaque_na_pesquisa}|')
                print(f'I{espaço}I')
                print()
        else:
            print('I------------------I')
            print('|Nada encontrado 👀|')
            print('I------------------I')

    Pesquisar()