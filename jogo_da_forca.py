def verificaLetra(letra,secreto,palavra):
    
    for x in range(0,len(secreto)+1):
        if letra == x:
            palavra[x] = letra
    
    return palavra

jogar = input('Deseja jogar o jogo da forca?(Digite 1 se sim / Digite 0 se não) ')
while jogar.isnumeric() == False or (int(jogar) != 1 and int(jogar) != 0):
    jogar = input('Deseja jogar o jogo da forca?(Digite 1 se sim / Digite 0 se não) ')

if int(jogar) == 0:
    print('Quem sabe na próxima,ne?\nAté mais.')
else:
    secreto = input('Diga a palvra secreta: ')
    print('\n\n\n\n\n\n\n\n\n\n\n')
    tentativa = 0
    palavra = '*'*len(secreto)
    while palavra != secreto and tentativa < 5:
        print(f'Você tem {5 - tentativa} tentativas.\n\n')
        letra = input ('Diga uma letra: ')
        while len(letra) > 1:
            letra = input ('Diga uma letra:(somente 1 caracter) ')
        aux = palavra
        palavra = verificaLetra(letra,secreto, aux)
        if palavra != aux:
            print(f'Parabéns! Você acertou a letra.\n{palavra}\n\n')
        else:
            tentativa += 1
            print(f'Errou.Tente novamente.\n{palavra}\n\n')

    print(f'Você acertou a palavra {palavra}.')
    print('Obrigado por jogar! Até mais.')

