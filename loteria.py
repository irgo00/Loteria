# IGOR MICHEL MAZO

import random

# MEGA SENA

def megaSena(qtdApostas):

    # CRIAR LISTA DE NÚMEROS

    numeros = []

    for i in range(1, 61):
        numeros.append(i)

        
    todasApostas = [] # cada lista de aposta ficará em uma posição dessa lista

    for i in range(qtdApostas):

        numerosEscolhidos = []
        numerosDisponiveis = numeros.copy()

        qtd = int(input('QUANTIDADE DE NÚMEROS A ESCOLHER (Mínimo: 6, Máximo: 20): '))
        if qtd < 6 or qtd > 20:
            print('ERRO! QUANTIDADE INVÁLIDA')
            return

        for i in range(qtd):
            print(f'\nNÚMEROS DISPONÍVEIS: {numerosDisponiveis}')
            escolhido = int(input('\nNÚMERO ESCOLHIDO: '))
            if escolhido not in numerosDisponiveis:
                print('\nNÚMERO INVÁLIDO! SELECIONE NOVAMENTE.')
                return
            else:
                numerosEscolhidos.append(escolhido)
                numerosDisponiveis.remove(escolhido)
        print(f'\nNÚMEROS ESCOLHIDOS: {numerosEscolhidos}')

        todasApostas.append(numerosEscolhidos)
        

    # SORTEAR NÚMEROS

    print('\n#-------------------------------------------------#')
    numerosSorteados = random.sample(numeros, 6)
    print(f'\nNÚMEROS SORTEADOS: {numerosSorteados}')

    estatisticas = {i: 0 for i in range(7)}

    for i in range(len(todasApostas)):
        intersecao = set(todasApostas[i]).intersection(numerosSorteados)

        if len(intersecao) in estatisticas:
            estatisticas[len(intersecao)] += 1

        if len(intersecao) == 0:
            print(f'\nNÚMEROS ACERTADOS NA {i+1}ª APOSTA: nenhum')
        else:
            print(f'\nNÚMEROS ACERTADOS NA {i+1}ª APOSTA: {intersecao}')

        if len(intersecao) == 4:
            print(f'PARABÉNS, VOCÊ GANHOU NA QUADRA!')
        elif len(intersecao) == 5:
            print(f'PARABÉNS, VOCÊ GANHOU NA QUINA!')
        elif len(intersecao) == 6:
            print(f'\nPARABÉNS! VOCÊ GANHOU O MAIOR PRÊMIO!!!')

    print('\nESTATÍSTICAS:')
    for acertos, qtd in estatisticas.items():
        print(f'{qtd} aposta(s) com {acertos} acertos.')

# QUINA 

def quina(qtdApostas):
    # CRIAR LISTA DE NÚMEROS

    numeros = []

    for i in range(1, 81):
        numeros.append(i)

    
    todasApostas = [] # cada lista de aposta ficará em uma posição dessa lista

    for i in range(qtdApostas):

        numerosEscolhidos = []
        numerosDisponiveis = numeros.copy()

        qtd = int(input('QUANTIDADE DE NÚMEROS A ESCOLHER (Mínimo: 5, Máximo: 15): '))
        if qtd < 5 or qtd > 15:
            print('ERRO! QUANTIDADE INVÁLIDA')
            return

        for i in range(qtd):
            print(f'\nNÚMEROS DISPONÍVEIS: {numerosDisponiveis}')
            escolhido = int(input('\nNÚMERO ESCOLHIDO: '))
            if escolhido not in numerosDisponiveis:
                print('\nNÚMERO INVÁLIDO! SELECIONE NOVAMENTE.')
                return
            else:
                numerosEscolhidos.append(escolhido)
                numerosDisponiveis.remove(escolhido)
        print(f'\nNÚMEROS ESCOLHIDOS: {numerosEscolhidos}')

        todasApostas.append(numerosEscolhidos)
        
    # SORTEAR NÚMEROS

    print('\n#-------------------------------------------------#')
    numerosSorteados = random.sample(numeros, 5)
    print(f'\nNÚMEROS SORTEADOS: {numerosSorteados}')

    estatisticas = {i: 0 for i in range(6)}

    for i in range(len(todasApostas)):
        intersecao = set(todasApostas[i]).intersection(numerosSorteados)

        if len(intersecao) in estatisticas:
            estatisticas[len(intersecao)] += 1

        if len(intersecao) == 0:
            print(f'\nNÚMEROS ACERTADOS NA {i+1}ª APOSTA: nenhum\n')
        else:
            print(f'\nNÚMEROS ACERTADOS NA {i+1}ª APOSTA: {intersecao}\n')

        if len(intersecao) == 2:
            print(f'PARABÉNS, VOCÊ GANHOU NO DUQUE (menor prêmio)!')
        if len(intersecao) == 3:
            print(f'PARABÉNS, VOCÊ GANHOU NO TERNO!')
        if len(intersecao) == 4:
            print(f'PARABÉNS, VOCÊ GANHOU NA QUADRA!')
        elif len(intersecao) == 5:
            print(f'PARABÉNS, VOCÊ GANHOU NA QUINA (maior prêmio!')

    print('\n#-------------------------------------------------#')
    print('\nESTATÍSTICAS:')
    for acertos, qtd in estatisticas.items():
        print(f'{qtd} aposta(s) com {acertos} acertos.')

# LOTOFÁCIL 

def lotofacil(qtdApostas):
    # CRIAR LISTA DE NÚMEROS

    numeros = []

    for i in range(1, 26):
        numeros.append(i)

    
    todasApostas = [] # cada lista de aposta ficará em uma posição dessa lista

    for i in range(qtdApostas):

        numerosEscolhidos = []
        numerosDisponiveis = numeros.copy()

        qtd = int(input('QUANTIDADE DE NÚMEROS A ESCOLHER (Mínimo: 15, Máximo: 25): '))
        if qtd < 15 or qtd > 25:
            print('ERRO! QUANTIDADE INVÁLIDA')
            return

        for i in range(qtd):
            print(f'\nNÚMEROS DISPONÍVEIS: {numerosDisponiveis}')
            escolhido = int(input('\nNÚMERO ESCOLHIDO: '))
            if escolhido not in numerosDisponiveis:
                print('\nNÚMERO INVÁLIDO! SELECIONE NOVAMENTE.')
                return
            else:
                numerosEscolhidos.append(escolhido)
                numerosDisponiveis.remove(escolhido)
        print(f'\nNÚMEROS ESCOLHIDOS: {numerosEscolhidos}')

        todasApostas.append(numerosEscolhidos)
        

    # SORTEAR NÚMEROS

    print('\n#-------------------------------------------------#')
    numerosSorteados = random.sample(numeros, 15)
    print(f'\nNÚMEROS SORTEADOS: {numerosSorteados}')

    estatisticas = {i: 0 for i in range(16)}

    for i in range(len(todasApostas)):
        intersecao = set(todasApostas[i]).intersection(numerosSorteados)

        if len(intersecao) in estatisticas:
            estatisticas[len(intersecao)] += 1

        if len(intersecao) == 0:
            print(f'\nNÚMEROS ACERTADOS NA {i+1}ª APOSTA: nenhum\n')
        else:
            print(f'\nNÚMEROS ACERTADOS NA {i+1}ª APOSTA: {intersecao}\n')

        if 11 <= len(intersecao) <= 13:
            print(f'PARABÉNS, VOCÊ GANHOU O MENOR PRÊMIO!')
        if len(intersecao) == 14:
            print(f'PARABÉNS, VOCÊ GANHOU O PRÊMIO SECUNDÁRIO!')
        if len(intersecao) == 15:
            print(f'PARABÉNS, VOCÊ GANHOU O MAIOR PRÊMIO!')

    print('\n#-------------------------------------------------#')
    print('\nESTATÍSTICAS:')
    for acertos, qtd in estatisticas.items():
        print(f'{qtd} aposta(s) com {acertos} acertos.')

#------------------------------------------------------------------#

print('\n#-------------------------------------------------#')
print('1 - Mega Sena')
print('2 - Quina')
print('3 - Lotofácil')
print('#-------------------------------------------------#\n')

jogo = int(input('ESCOLHA O JOGO: '))

qtdApostas = int(input('QUANTAS APOSTAS VOCÊ DESEJA REALIZAR? '))

match jogo:
    case 1:
        megaSena(qtdApostas)
    case 2:
        quina(qtdApostas)
    case 3:
        lotofacil(qtdApostas)
    case _:
        print('OPÇÃO INVÁLIDA!')
