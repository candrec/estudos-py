#Este é um jogo de adivinhar o número.
import random
secret_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Peça para o jogador adivinhar 6 vezes
print('You will have six chances to guess.')
for guesses_taken in range(1,7):   #lembrar, o range começa em 1 e vai até 6
    guess = int(input('Take a guess: '))

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('your guess is too high.')
    else:
        break   #esta condição corresponde ao palpite correto!

if guess == secret_number:
    print(f'Good job! You guessed my number in {guesses_taken} guesses!')
else:
    print(f'Nope. The number I was thinking of was {secret_number}!')