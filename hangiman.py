import random
import string


class HangimanGame:
    def __init__(self, word=None, max_tries=6):

        # Opening the text file
        f = open("CommonEnglishWords.txt", "r")
        # Reading the file
        file = f.read()
        # Splitting the file into a list of words
        self.word_list = file.splitlines()
        # Close the file
        f.close()

        g = open("LongerEnglishWords.txt", "r")
        gile = g.read()
        self.longer_word_list = gile.splitlines()
        g.close()

        self.word = word or random.choice(self.word_list+self.longer_word_list)
        self.max_tries = max_tries
        self.guesses = set()
        self.tries_left = max_tries
        self.status = 'playing'  # can be 'playing', 'won', 'lost'



    def guess(self, letter):
        if self.status != 'playing' or not letter.isalpha() or len(letter) != 1:
            return
        letter = letter.lower()
        if letter in self.guesses:
            return
        self.guesses.add(letter)
        if letter not in self.word:
            self.tries_left -= 1
        if all(l in self.guesses for l in self.word):
            self.status = 'won'
        elif self.tries_left <= 0:
            self.status = 'lost'

    def get_display_word(self):
        return ' '.join([l if l in self.guesses else '_' for l in self.word])

    def get_state(self):
        return {
            'display_word': self.get_display_word(),
            'guesses': sorted(list(self.guesses)),
            'tries_left': self.tries_left,
            'status': self.status,
            'word': self.word if self.status != 'playing' else None
        }
