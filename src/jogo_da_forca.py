def checkLetter(letter,secret,word):
    word = list(word)
    aux = len(secret)
    for x in range(aux):
        if letter == secret[x]:
            word[x] = letter
    word = "".join(z for z in word)
    secret = str(secret)
    return word

play = input('DO YOU WANT TO PLAY THE HANGMAN GAME?(Type 1 if yes / Type 0 if no) ')
while play.isnumeric() == False or (int(play) != 1 and int(play) != 0):
    play = input('DO YOU WANT TO PLAY?(Type 1 if yes / Type 0 if no) ')

if int(play) == 0:
    print('Maybe next time, right?\nSee you later.')
else:
    secret = input('Type the secret word: ')
    attempt = 0
    word = '*' * len(secret)
    while word != secret and attempt < 5:
        print(f'You have {5 - attempt} attempts.\n\n')
        letter = input ('Say a letter: ')
        while len(letter) > 1:
            letter = input ('Say a letter:(only 1 caracter) ')
        aux = word
        word = checkLetter(letter,secret,word)
        if word != aux:
            print(f'Congratulations! The letter is in the secret word.\n{word}\n\n')
        else:
            attempt += 1
            print(f'Ops. Miss it.\n{word}\n\n')
    if word != secret:
        print(f'Sorry, you lost! The secret word is: {secret}.\nTry again some other time.')
    else:
        print(f'You did it! You found the word: {word}.')
    
    print('\nThanks for playing! See you later.')

