import random
import sys

def toss_coin(guess):
    toss = random.randint(1, 2)
    guess_name = 'heads' if guess == 1 else 'tails'
    message = 'right' if toss == guess else 'wrong'
    print('Your guess of {} was {}'.format(guess_name, message))

def ask_guess():
    guess = None
    while guess not in {0, 1, 2}:
        try:
            guess = int(input('Enter 1 for heads or 2 for tails, 0 to quit: '))
        except ValueError:
            print('Guess not valid.')
    return guess

def main():
    print('Welcome to Guess That Coin Toss!')
    while True:
        guess = ask_guess()
        if guess == 0:
            print('Thanks for playing.')
            sys.exit()
        else:
            toss_coin(guess)

if __name__ == '__main__':
    main()
