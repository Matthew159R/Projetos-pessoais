import random
import os
desafio = int(input('Qual desfio de raciocínio deseja fazer? (1)[Raciocínio] / (2)[Memória]'))
match desafio:
    case 1:
        operações = int(input('Qual operção você deseja fazer? [1]Sequência lógica | [2]Adição | [3]Subtração | [4]Multiplicação | [5]Divisão | [6] Cálculo com número binário | [7] perguntas de lógica '))
        match operações:
            case 1:
                pontos_Raciocínio_Soma = 0
                for i in range(0, 10):
                    number1 = number = random.randint(0, 50)
                    number2 = number = random.randint(0, 50)
                    resultado = number1 + number2
                    print(f'{number1} + {number2}')
                    soma = int(input('Digite o resultado...'))
                    if soma != resultado:
                        print(f'Errou...{resultado}')
                    elif soma == resultado:
                        pontos_Raciocínio_Soma += 1
                        print('Acertou...')
                if pontos_Raciocínio_Soma > 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Soma))
                    print('Você foi muito bem! Mas ainda da para melhorar.')
                elif pontos_Raciocínio_Soma == 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Soma))
                    print('Você está na média. Continue praticando')
                elif pontos_Raciocínio_Soma == 10:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Soma))
                    print('Perfeito! Você conseguiu a pontuação máxima.')
                elif pontos_Raciocínio_Soma > 0 and soma < 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Soma))
                    print('Sua pontuação foi baixa, mas tente novamente.')
                elif pontos_Raciocínio_Soma == 0:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Soma))
                    print('Você não acertou nada. Pratique mais.')
                elif pontos_Raciocínio_Soma == 10:
                    print('Perfeito! Você acertou tudo.')
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Soma))
            case 2:
                pontos_Raciocínio_Subtração = 0
                for i in range(0, 10):
                   number1 = random.randint(0, 50)
                   number2 = random.randint(0, 50)
                   if number1 < number2:
                    number1 == number2
                    number2 = number1
                   if number1 == number2:
                    number1 += number2
                   resultado = number1 - number2
                   print(f'{number1} - {number2}')
                   subtração = int(input('Digite o resultado'))
                   if subtração != resultado:
                        print(f'Errou...{resultado}')
                   elif subtração == resultado:
                        pontos_Raciocínio_Subtração += 1
                        print('Acertou...')
                if pontos_Raciocínio_Subtração > 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Subtração))
                    print('Você foi muito bem! Mas ainda da para melhorar.')
                elif pontos_Raciocínio_Subtração == 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Subtração))
                    print('Você está na média. Continue praticando')
                elif pontos_Raciocínio_Subtração == 10:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Subtração))
                    print('Perfeito! Você conseguiu a pontuação máxima.')
                elif pontos_Raciocínio_Subtração > 0 and subtração < 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Subtração))
                    print('Sua pontuação foi baixa, mas tente novamente.')
                elif pontos_Raciocínio_Subtração == 0:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Subtração))
                    print('Você não acertou nada. Pratique mais.')
                elif pontos_Raciocínio_Subtração == 10:
                    print('Perfeito! Você acertou tudo.')
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Subtração))
            case 3:
                pontos_Raciocínio_Multiplicação = 0
                for i in range(0, 10):
                    number1 = random.randint(0, 7)
                    number2 = random.randint(0, 50)
                    resultado = number1 * number2
                    print(f'{number1} * {number2}')
                    multiplicação = int(input('Digite o resultado'))
                    if multiplicação != resultado:
                        print('Errou...')
                    elif multiplicação == resultado:
                        pontos_Raciocínio_Multiplicação += 1
                        print(f'Acertou...{resultado}')
                if pontos_Raciocínio_Multiplicação > 6:
                    print('Seus pontos foram: ({})').format(pontos_Raciocínio_Multiplicação)
                    print('Você foi muito bem! Mas ainda da para melhorar.')
                elif pontos_Raciocínio_Multiplicação == 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Multiplicação))
                    print('Você está na média. Continue praticando')
                elif pontos_Raciocínio_Multiplicação == 10:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Multiplicação))
                    print('Perfeito! Você conseguiu a pontuação máxima.')
                elif pontos_Raciocínio_Multiplicação > 0 and multiplicação < 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Multiplicação))
                    print('Sua pontuação foi baixa, mas tente novamente.')
                elif pontos_Raciocínio_Multiplicação == 0:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Multiplicação))
                    print('Você não acertou nada. Pratique mais.')
                elif pontos_Raciocínio_Multiplicação == 10:
                    print('Perfeito! Você acertou tudo.')
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Multiplicação))
            case 4:
                pontos_Raciocínio_Divisão = 0
                for i in range(0, 10):
                    number1 = random.randint(0, 500)
                    number2 = random.randint(0, 100)
                    resultado = number1 / number2
                    print(f'{number1} / {number2}')
                    divisão = int(input('Digite o resultado'))
                    if divisão == resultado:
                        pontos_Raciocínio_Divisão += 1
                        print('Acertou...')
                    else:
                        print(f'Errou...{resultado}')
                if pontos_Raciocínio_Divisão > 6:
                    print('Seus pontos foram: ({})').format(pontos_Raciocínio_Divisão)
                    print('Você foi muito bem! Mas ainda da para melhorar.')
                elif pontos_Raciocínio_Divisão == 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Divisão))
                    print('Você está na média. Continue praticando')
                elif pontos_Raciocínio_Divisão == 10:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Divisão))
                    print('Perfeito! Você conseguiu a pontuação máxima.')
                elif pontos_Raciocínio_Divisão > 0 and divisão < 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Divisão))
                    print('Sua pontuação foi baixa, mas tente novamente.')
                elif pontos_Raciocínio_Divisão == 0:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Divisão))
                    print('Você não acertou nada. Pratique mais.')
                elif pontos_Raciocínio_Divisão == 10:
                    print('Perfeito! Você acertou tudo.')
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_Divisão))
            case 5:
                iniciar = input('Nesse desafio você irá demorar um pouco mais. Use lapis e papel se precisar. Caso não saiba converter digite [N]')
                if iniciar == 'N' or iniciar == 'n':
                    print('Clique no link para saber converter binário em decimal:  ----(https://youtu.be/zToihF2FE9I)----')
                    print('Clique nessa para saber converter decimal em binário:    ----https://youtu.be/mttrG_kbHN4)----')
                pontos_Raciocínio_NumBinario = 0
                for i in range(0, 5):
                    number = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1) ]
                    decimal = pow(number[7] * 2, 0) + pow(number[6] * 2, 1) + pow(number[5] * 2, 2) + pow(number[4] * 2, 3) + pow(number[3] * 2, 4) + pow(number[2] * 2, 5) + pow(number[1] * 2, 6) + pow(number[0] * 2, 7)
                    if number[7] == 0:
                        decimal = decimal - 1
                    resposta = int(input(f'Converta esse binário para decimal: {number}'))
                    if resposta == decimal:
                        print('Acertou...')
                        pontos_Raciocínio_NumBinario += 1
                    else:
                        print(f'Errou... O resultado era: {decimal}')
                    def decimalParaBinario(valor):
                        if valor <= 0:
                            return '0'
                        binario = ''
                        while valor > 0:
                            resto = int(valor % 2)
                            valor = int(valor / 2)
                            binario = str(resto) + binario
                            return binario
                    num = random.randint(0, 70)
                    binario = decimalParaBinario(num)
                    resposta = int(input(f'Converta esse número para binário {num}'))
                    resposta = str(resposta)
                    if resposta == binario:
                        print('Acertou...')
                        pontos_Raciocínio_NumBinario += 1
                    else:
                        print('Errou...')
                if pontos_Raciocínio_NumBinario > 6:
                    print('Seus pontos foram: ({})').format(pontos_Raciocínio_NumBinario)
                    print('Você foi muito bem! Mas ainda da para melhorar.')
                elif pontos_Raciocínio_NumBinario == 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_NumBinario))
                    print('Você está na média. Continue praticando')
                elif pontos_Raciocínio_NumBinario == 10:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_NumBinario))
                    print('Perfeito! Você conseguiu a pontuação máxima.')
                elif pontos_Raciocínio_NumBinario <= 6:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_NumBinario))
                    print('Sua pontuação foi baixa, mas tente novamente.')
                elif pontos_Raciocínio_NumBinario == 0:
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_NumBinario))
                    print('Você não acertou nada. Pratique mais.')
                elif pontos_Raciocínio_NumBinario == 10:
                    print('Perfeito! Você acertou tudo.')
                    print('Seus pontos foram: ({})'.format(pontos_Raciocínio_NumBinario))
            case 6:
                pontos_Raciocínio_Sequência_Lógica = 0
                print(1, 3, 6,'?')
                sequência1 = int(input('Qual é o número da sequência?'))
                if sequência1 == 9:
                    pontos_Raciocínio_Sequência_Lógica += 1
                    print('Acertou!')
                else:
                    print('Errou...')
                print(1, 1, 2, 3, 5, '?')
                sequência2 = int(input('Qual é o número da sequência?'))
                if sequência2 == 8:
                    pontos_Raciocínio_Sequência_Lógica += 1
                    print('Acertou!')
                else:
                    print('Errou...')
                print(1, 1, 4, 18, 96, '?')
                sequência3 = int(input('Qual é o número da sequência?'))
                if  sequência3 == 600:
                    pontos_Raciocínio_Sequência_Lógica += 1
                    print('Acertou!')
                else:
                    print('Errou...')
                print(1, 1, 2, 4, 8, 16, 32, 68,'?')
                sequência4 = int(input('Qual é o número da sequência?'))
                if  sequência4 == 68:
                    pontos_Raciocínio_Sequência_Lógica += 1
                    print('Acertou!')
                else:
                    print('Errou...')
                print('👆', '👉', '👇', '?')
                sequência5 = int(input('Qual é o emoji da sequência? 1(👈) 2(👉) 3(🤘) 4(🤜) '))
                if  sequência5 == 1:
                    pontos_Raciocínio_Sequência_Lógica += 1
                    print('Acertou!')
                else:
                    print('Errou...')
                print('Gol = 34 | Kiwi = 52 | Proz = ?')
                sequência6 = int(input('Proz é igual a qual número?'))
                if  sequência6 == 75:
                    pontos_Raciocínio_Sequência_Lógica += 1
                    print('Acertou!')
                else:
                    print('Errou...')
            
                print('Seus pontos foram {}'.format(pontos_Raciocínio_Sequência_Lógica))
            case 7:
                pontos_Raciocínio_Perguntas = 0
                print('Nesse desafio você vai Responder perguntas de lógica')
                pronto = input('Pronto?. Pressione <enter>')
                os.system('cls')
                print('Qual das combinações não pertence ao grupo?')
                resposta1 = int(input('(1)[VBNM] (2)[AOEI] (3)TPLK (4)SDGF'))
                if resposta1 == 2:
                    print('Acertou...')
                    print('Diferente de todas as outras a segunda opção só tem vogais')
                    pontos_Raciocínio_Perguntas += 1
                else:
                    print('Errou...')
                    print('qual desses números não pertence à sequência?')
                    resposta2 = int(input('(1)[2716] (2)[4135] (3)[5321] (4)[7145]'))
                if resposta2 == 1:
                    print('Acertou...')
                    print('Se você somar cada dígito desses números eles irão formar números ímpares, já a primeira opção irá nos dar o número par 16')
                    pontos_Raciocínio_Perguntas += 1
                else:
                    print('Errou...')
                if resposta1 == 2 and resposta2 == 1:
                    print('Você está indo bem')
                print('“Se João estuda, então Marcela chora”. A negação dessa proposição é logicamente equivalente a:')
                resposta3 = int(input('1) Se João não estuda então Marcela não chora 2) João não estuda ou Marcela não chora 3) João não estuda e Marcela não chora 4) João estuda e Marcela não chora 5) João estuda ou Marcela não chora'))
                if resposta3 == 'D' or resposta3 == 'd':
                    print('Acertou...')
                    print('Uma negação mantém a primeira sentença (“Se João estuda”) e nega a segunda (“então Marcela chora”)')
                    pontos_Raciocínio_Perguntas += 1
                else:
                    print('Errou...')
                print(f'Seus pontos foram {pontos_Raciocínio_Perguntas}')
                if pontos_Raciocínio_Perguntas > 2:
                    print('Perfeito!')
                else:
                    print('Tente mais uma vez')
    case 2:
        ponstos_Memória_Nomes = 0
        Condição = input('Nesse desafio você terá que lembrar nomes de pessoas. Demore 3 segundos em cada um e aperte enter. Pressione enter')
        nomes = input('(🦸)Sofia (🧚‍♀️)Júlia (🧙)Amir')
        os.system('cls')
        print('(🦸) (🧚‍♀️) (🧙) Qual o nome deles na ordem?')
        resposta = input('A) Lucas, Lucia, Julio B)Luana, Nina, Lucas C) Julia, Sofia, Amir D) Sofia, Júlia, Amir')
        if resposta == 'D' or resposta == 'd':
            print('Acertou')
            ponstos_Memória_Nomes += 1
        else:
            print('Errou...')
        nomes2 = input('(👨‍🔬)Nícolas (👩‍🎨)Lúcia (👨‍⚖️)Neytan (👨‍💻)Matheus (👨‍🍳)Luck')
        os.system('cls')
        print('(👨‍🔬) (👩‍🎨) (👨‍⚖️) (👨‍💻) (👨‍🍳) Qual o nome deles na ordem?')
        resposta2 = input('A)Nícolas, Lúcia, Neytan, Matheus, Luck B)Robson, Júlia, Neytan, Lucas, C)Rodney, Gina, Nick, John D)Rub, lúcia, Bobby, Nícolas')
        if resposta2 == 'A' or resposta2 == 'a':
            print('Acertou...')
            ponstos_Memória_Nomes += 1
        else:
            print('Errou...')
        nomes3 = input('(🧔)Huck (👷‍♂️)Brock (👮‍♀️)Alícia (🕵️‍♀️)Rúbia (👨‍🏭)Acir')
        os.system('cls')
        print('(🧔) (👷‍♂️) (👮‍♀️) (🕵️‍♀️) (👨‍🏭) Qual o nome deles na ondem?')
        resposta3 = input('A)Lúcia, Hulk, Bobby, Vex, Acir B)Huck, Brock, Alícia, Rúbia, Acir C)Rock, Nick, John, Brock, Nina D)Dina, Rock, Júlio, Lúcio, Daniel')
        if resposta3 == 'B' or resposta3 == 'b':
            print('Acertou...')
            ponstos_Memória_Nomes += 1
        else:
            print('Errou...')
        nomes4 = input('(👩‍🏫)Silvana (👵)Regina (💂‍♀️)Roberta (👴)Pereira (👲)Júnior')
        os.system('cls')
        print('(👩‍🏫) (👵) (💂‍♀️) (👴) (👲) Qual o nome deles na ordem')
        resposta4 = input('A) Rúbia, joana, nícolas, Bruno, Gabriel B)Silvana, Regina, Brock, john, rúbia C) Silvana, Regina, Roberta, Pereira, Júnios D)Lucas, Nina, Roberta, Pereira, Luck')
        if resposta4 == 'C' or resposta4 == 'c':
            print('Acertou...')
            ponstos_Memória_Nomes += 1
        else:
            print('Errou...')
        print('Seus pontos foram {}'.format(ponstos_Memória_Nomes))
        if ponstos_Memória_Nomes < 3:
            print('Você foi mal neste teste, mas tente novamente')
        elif ponstos_Memória_Nomes == 3:
            print('Ótimo, você foi muito bem')
        elif ponstos_Memória_Nomes == 4:
            print('Perfeito, você tirou nota máxima')
