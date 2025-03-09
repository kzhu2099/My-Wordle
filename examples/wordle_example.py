'''
Author: Kevin Zhu

Basic example for Wordle showing what to do and what not to do.
'''

from mywordle import Wordle

if __name__ == '__main__':
    game = Wordle()

    '''
    Examples of good uses
    '''
    # game.play('words')

    # game.play() # random word

    '''
    Examples of errors
    '''
    # game.play('12345', restrict_word = False) # contains digits so raises a ValueError

    # game.play('aaaaa') # is not valid so defaults to a random word

    '''
    Example of customization
    '''
    game.play('magazine', num_guesses = 7, restrict_word = False)  # is not valid so defaults to a random word

    game2 = Wordle(['magazine'], []) # allows any guesses after picking from this list

    game2.play()