'''
Author: Kevin Zhu

Basic example for Wordle showing what to do and what not to do.
'''

from mywordle import Wordle

if __name__ == '__main__':
    game = Wordle()

    '''
    Examples of basic uses
    '''

    game.play() # random word

    game.play('words', challenge_mode = True) # must follow clues given

    '''
    Examples of errors
    '''

    # game.play('12345', allow_any_word = True) # contains digits so raises a ValueError

    # game.play('aaaaa') # is not valid so defaults to a random word

    '''
    Example of customization
    '''

    game.play('magazine', num_guesses = 7) # target will be MAGAZINE

    # game.play(word_length = 8) # any 8 letter word

    game2 = Wordle(['magazine'], []) # allows any guesses after picking from this list

    game2.play()