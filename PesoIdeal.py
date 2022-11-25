#------Inputs------
nome = input('Qual é o seu nome?')
peso = float(input('Qual é o seu peso?'))
altura = float(input('Qual é a sua altura'))
#-------------Cálculo----------------
imc = peso / pow(altura, 2)
pesoApoximado = 18.50 * peso / imc
pesoApoximado2 = 25 * peso / imc
pesoIdeal = 22 * peso / imc
#-------------Resposta ao imc da pessoa-----------------
if imc < 18.00:
    print(f'{nome}, seu imc é {imc}. Seu imc está para magreza')
    print(f'Seu peso ideal seria {round(pesoIdeal)} ou algo em torno de {round(pesoApoximado)} e {round(pesoApoximado2)}.')
elif imc < 25.00:
    print(f'{nome}, seu imc é {imc}. Imc ideal, parabéns.')
    print(f'Mas sempre da para melhor, {nome}')
elif imc < 30.00:
    print(f'{nome}, seu imc é {imc}. Você está na pré obesidade')
    print(f'Seu peso ideal seria {round(pesoIdeal)} ou algo em torno de {round(pesoApoximado)} e {round(pesoApoximado2)}.')
elif imc < 35:
    print(f'{nome}, seu imc é {imc}. Você está na obesidade grau 1.')
    print(f'Seu peso ideal seria {round(pesoIdeal)} ou algo em torno de {round(pesoApoximado)} e {round(pesoApoximado2)}.')
elif imc > 35:
    print(f'{nome}, seu imc é {imc}. Você está na obesidade grau 2')
    print(f'Seu peso ideal seria {round(pesoIdeal)} ou algo em torno de {round(pesoApoximado)} e {round(pesoApoximado2)}.')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Feito por Matheus Batista
