# Joguinho da Forca
def opcoes():
    print('\n---------- JOGO DA FORCA ----------')
    print('Escolha uma opção:\n')
    opcao = -1

    while opcao != 0:
        opcao = int(input('1 - Partida rápida;\n2 - Desafiar Amigo;\n0 - Sair do Jogo;\n--------\n'))
        if opcao == 1:
            jogar()
        elif opcao == 2:
            partidaEspecial()
        elif opcao == 0:
            print('Thanks!')
        else:
            print('Opção Inválida!\n')


def partidaEspecial():
    acertou = False
    enforcou = False
    palavra = str(input('Digite a palavra que deseja para desafiar um amigo: '))
    palavra = palavra.upper()
    dica = str(input('Digite uma dica: '))
    erros = 0
    letrasUsadas = ''

    aux = str(palavra)

    aux = ["_" for _ in range(len(palavra))]

    print('\n\n\nPronto, podemos começar\n----------\n')
    while not acertou and not enforcou:
        print(aux)
        print('Dica: {}'.format(dica))
        if letrasUsadas != '':
            print('Letras Usadas: {}\n'.format(letrasUsadas))
        chute = str(input('Digite uma letra: '))
        chute = chute.upper()
        letrasUsadas += (chute+' ')
        print('Letras Usadas: {}\n'.format(letrasUsadas))

        if chute in palavra:
            i = 0
            for letra in palavra:
                if chute.upper() == letra.upper():
                    aux[i] = letra
                    print('\nAcertou!\n')
                i += 1
            acertou = '_' not in aux
            if erros == 7:
                enforcou = True
        else:
            erros += 1
            print('\nErrou!\nQuantidade de Erros: {} de {}\n'.format(erros, '7'))
            if erros == 7:
                enforcou = True
            # print(letrasAcertadas)
    if acertou:  # verificando se  acertou é True
        print('Você Ganhou!\nParabéns!\nA palavra é: {}\n---------'.format(palavra.capitalize()))
    else:
        print('Você Perdeu!\nA palavra correta é: {}\n'.format(palavra))
        print('FIM DO JOGO\n---------------')


def jogar():
    print('--------------\nJogo da Forca\n--------------\n')

    palavraSecreta = 'banana'
    acertou = False
    enforcou = False
    erros = 0
    letrasAcertadas = ['_', '_', '_', '_', '_', '_']
    letrasUsadas = ''

    while not acertou and not enforcou:
        print(letrasAcertadas)
        if letrasUsadas != '':
            print('Letras Usadas: {}'.format(letrasUsadas))
        chute = input(str('Digite uma letra: '))
        letrasUsadas += chute + ' '

        if chute in palavraSecreta:
            posicao = 0
            for letra in palavraSecreta:
                if chute.lower() == letra.lower():
                    letrasAcertadas[posicao] = letra
                posicao += 1
            acertou = '_' not in letrasAcertadas  # '_' não está contido em LetrasAcertadas
        else:
            erros += 1
            print('Errou!\nQuantidade de Erros: {} de {}\n'.format(erros, '7'))
            if erros == 7:
                enforcou = True
        # print(letrasAcertadas)
    if acertou:  # verificando se  acertou é True
        print('\nVocê Ganhou!\nParabéns!\n')
    else:
        print('Você Perdeu!\nA palavra correta é: {}\n'.format(palavraSecreta))
    print('FIM DO JOGO\n---------------')


opcoes()
