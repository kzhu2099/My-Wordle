'''
Author: Kevin Zhu
Wordle is owned by the NYT. This class aims to mimic its behavior for python users and is not the actual Wordle.
Please visit https://www.nytimes.com/games/wordle/index.html to play the actual game online.
'''

import random
import time

from importlib.resources import open_text

class Wordle:

    '''
    A class that provides a game like Wordle and allows for users to play in Python.

    The aim is to guess a 5-letter word within 6 attempts.
    When you guess the word, you will be given a color-coded result with the following key:

    - Green is the correct letter in the correct spot
    - Yellow is the correct letter but it is in a different spot
    - Gray/White means that the letter is not in the word.

    '''

    def __init__(self):
        self.word_list = []
        with open_text('mynyt.data', 'possible_words.txt') as file:
            text = file.read()
            self.word_list = text.split('\n')

        self.guess_list = []
        with open_text('mynyt.data', 'possible_guesses.txt') as file:
            text = file.read()
            self.guess_list = text.split('\n')

        self.word = ''

        # ANSI Colors
        self.GREEN = '\x1B[1m\033[32m'
        self.YELLOW = '\x1B[1m\033[33m'
        self.WHITE = '\x1B[1m\033[37m'
        self.GREY = '\x1B[1m\033[90m'
        self.RESET = '\x1B[0m\033[0m'

        self.keyboard = {}

    def play(self, num_guesses = 6, custom_word = None, restrict_word = True):

        '''
        Plays the game Wordle, with the target either being a random word or custom_word!

        Parameters
        ----------
        string custom_word, optional:
            a 5-letter word in the list of vaid words to use as the target word. If it is not valid, defaults to a random word.

        Returns
        -------
            A boolean of whether or not the player won.
        '''

        if custom_word and restrict_word and not self.is_valid_guess(custom_word):
            print('Invalid custom word, using a default one instead.')
            custom_word = None

        self.word = custom_word or self.word_list[random.randint(0, len(self.word_list))]
        self.word = self.word.upper()

        self.keyboard = [
            {'Q': self.WHITE, 'W': self.WHITE, 'E': self.WHITE, 'R': self.WHITE, 'T': self.WHITE, 'Y': self.WHITE, 'U': self.WHITE, 'I': self.WHITE, 'O': self.WHITE, 'P': self.WHITE},
                {'A': self.WHITE, 'S': self.WHITE, 'D': self.WHITE, 'F': self.WHITE, 'G': self.WHITE, 'H': self.WHITE, 'J': self.WHITE, 'K': self.WHITE, 'L': self.WHITE},
                    {'Z': self.WHITE, 'X': self.WHITE, 'C': self.WHITE, 'V': self.WHITE, 'B': self.WHITE, 'N': self.WHITE, 'M': self.WHITE}
        ]

        print('The word is ready!')
        guesses = []
        win = False

        for i in range(num_guesses):
            while True:
                print('-' * 25)
                self.print_keyboard()
                guess = input(f'Guess #{i + 1}: ').upper()

                if len(guess) != len(self.word):
                    print('Invalid length, please try again')

                elif restrict_word and self.is_valid_guess(guess):
                    print('Invalid word, please try again.')

                else:
                    break

            result = self.guess_word(guess)

            full_guess = ''
            for char, color in zip(list(guess), list(result)):
                formatted_char = f'{color}{char}{self.RESET} '
                print(formatted_char, end = '', flush = True)
                full_guess += formatted_char
                time.sleep(0.4)
            print()
            guesses.append(full_guess)

            if ''.join(result) == self.GREEN * 5:
                win = True
                break

        formatted_word = self.WHITE
        formatted_word += ' '.join(list(self.word))
        formatted_word += self.RESET

        if win:
            print(f'Congratulations! The word was {formatted_word}. You got it in {i + 1} guesses!')

        else:
            print(f'Sorry, you ran out of guesses! The word was {formatted_word}.')

        print('Your guesses: ')
        print('\n'.join(guesses))

        return win

    def is_valid_word(self, word):

        '''
        Determines if this word is valid (if it has 5 letters and is inside the WORD list).

        Parameters
        ----------
        string word:
            the word to check

        Returns
        -------
        boolean
            whether or not this word is valid
        '''

        return len(word) != 5 or word.lower() not in self.word_list

    def is_valid_guess(self, word):
        '''
        Determines if this guess is valid (if it has 5 letters and is inside the GUESS list).

        Parameters
        ----------
        string word:
            the word to check

        Returns
        -------
        boolean
            whether or not this word is valid
        '''

        return len(word) != 5 or word.lower() not in self.guess_list

    def guess_word(self, guess, target_word = None):

        '''
        Determines whether how close the guess is to the target word.

        Parameters
        ----------
        string guess:
            a valid 5 letter word
        string target_word, optional:
            an optional word to use for the target (defaults to self.word)

        Returns
        -------
        list
            a list of colors depending on each character's value
        '''

        word = target_word or self.word
        result = []
        target_characters = list(word)
        guess_characters = list(guess)

        for i in range(len(word)):
            if guess_characters[i] == target_characters[i]:
                result.append(self.GREEN)
                self.update_keyboard(target_characters[i], self.GREEN)
                target_characters[i] = None

            else:
                result.append(None)

        for i in range(len(word)):
            if result[i] is None and guess_characters[i] in target_characters:
                result[i] = self.YELLOW
                self.update_keyboard(guess_characters[i], self.YELLOW)
                target_characters[target_characters.index(guess_characters[i])] = None

            elif result[i] is None:
                result[i] = self.GREY
                self.update_keyboard(guess_characters[i], self.GREY)

        return result

    def update_keyboard(self, key, color):

        '''
        Changes the keyboard to reflect the current game.

        Parameters
        ----------
        string key:
            the 1 letter key to update

        string color:
            the ANSI color to update the key with
        '''

        for row in self.keyboard:
            if key in row:
                row[key] = color
                break

    def print_keyboard(self):

        '''
        Prints the keyboard with the correct positioning and color coding.
        '''

        indent = ''
        for row in self.keyboard:
            print(indent, end = '')
            for key in row.keys():
                print(row[key] + key + self.RESET + ' ', end = '')
            print()
            indent += ' '