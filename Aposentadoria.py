gênero = input('Qual é o seu gênero [M] Mulher [H] Homem [O] Outro')
if gênero == 'M':
    idade = int(input('Qual é a sua idade, senhora?'))
    tempoTrabalho = int(input('Quanto tempo a senhora tem de trabalho?'))
    deficiência = input('A senhora é portadora de alguma deficiência? [S] / [N]')
    if idade >= 65 and tempoTrabalho >= 30:
        print('A senhora pode se aposentar!')
    elif deficiência == 'S':
        print('A senhora pode se aposentar!')
    elif deficiência != 'S'and deficiência != 'N':
        print('Caracter não identificado, por favor reinicie o algorítimo.')
    else:
        print('A senhora não pode se apodentar!')
elif gênero == 'H':
    idade = int(input('Qual é a sua idade senhor?'))
    tempoTrabalho = int(input('Quanto tempo você tem de trabalho?'))
    deficiência = input('O senhor é portado de alguma deficiência? [S] / [N]')
    if idade >= 65 and tempoTrabalho >= 30:
        print('O senhor pode se aposentar')
    elif deficiência == 'S':
        print('O senhor pode se aposentar')
    elif deficiência != 'S'and deficiência != 'N':
        print('Caracter não identificado, por favor reinicie o algorítimo.')
    else:
        print('O senhor não pode se apodentar')
elif gênero == 'O':
    idade = int(input('Qual é a sua idade?'))
    tempoTrabalho = int(input('Quanto tempo você tem de trabalho?'))
    deficiência = input('Você é portador de alguma deficiência? [S] / [N]')
    if idade >= 65 and tempoTrabalho >= 30:
        print('Você pode se aposentar')
    elif deficiência == 'S':
        print('Você pode se aposentar')
    elif deficiência != 'S'and deficiência != 'N':
        print('Caracter não identificado, por favor reinicie o algorítimo.')
    else:
        print('O senhor não pode se apodentar')
else:
    print('Caracter não identificada \n')
    print('Por favor reinicie o algorítimo')