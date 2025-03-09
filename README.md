# mywordle

mywordle is a library that is simply Wordle.

Millions of people enjoy Wordle every day from the NYT. However,

- HomePage: https://github.com/kzhu2099/My-Wordle
- Issues: https://github.com/kzhu2099/My-Wordle/issues

Author: Kevin Zhu

## Features

- Allows users to play Wordle

## Installation

To install mywordle, use pip: ```pip install mywordle```.

However, many prefer to use a virtual environment.

MacOS / Linux:

```sh
# make your desired directory
mkdir /path/to/your/directory
cd /path/to/your/directory

# setup the .venv (or whatever you want to name it)
pip install virtualenv
python3 -m venv .venv

# install mywordle
source .venv/bin/activate
pip install mywordle

deactivate # when you are completely done
```

Windows CMD:

```sh
# make your desired directory
mkdir C:path\to\your\directory
cd C:path\to\your\directory

# setup the .venv (or whatever you want to name it)
pip install virtualenv
python3 -m venv .venv

# install mywordle
.venv\Scripts\activate
pip install mywordle

deactivate # when you are completely done
```

## Information

Wordle is a game that is now owned by the NYT.
The aim is to guess a 5-letter word within 6 attempts.
When you guess the word, you will be given a color-coded result with the following key:

- Green is the correct letter in the correct spot
- Yellow is the correct letter but it is in a different spot
- Gray/White means that the letter is not in the word.

## Usage

This game aims to mimic Wordle with thousands of available words.
To use it is very simple! Simply run:

```python
from mynyt import Wordle

game = Wordle()

game.play()
```

Guesses/words are not case sensitive.

You may pass in a custom word to guess for but it must be 5 letters, just like guesses.

It also must be part of the ```guess_list```. This is a list of words that are valid guesses, while ```word_list``` is a list of words that are valid starting points.
Randomly generated words are from the latter, because they are more well known. However, if you want to use a custom target, it must be part of guess_list.

To check if a word falls into either, use ```is_valid_word``` or ```is_valid_guess```

This means that you can guess with ```xylyl``` but it won't ever appear unless if you use ```game.play('xylyl')```.

See examples for more information.

## Disclaimer

Wordle is owned by the NYT. This library provides a version of Wordle that mimics its behavior for personal and non-commercial use.

## License

The License is an MIT License found in the LICENSE file.