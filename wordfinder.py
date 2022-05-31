"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:

    def __init__(self, path):
        """initialize wordfinder, call get_word_list to strip out /n characters, make a list to work with, prints the total number of words in the list"""
        word_file = open(path, 'r')

        self.path = path
        self.word_list =  self.get_word_list(word_file)

        print(f"{len(self.word_list)} words read")

    def __repr__(self):
        """gives representation string"""
        return f"<WordFinder, finds words in file= {self.path}>"

    def get_word_list(self, word_file):
        """Iterate through each line in the file given, strip /n characters, and append to list"""
        # return [word.strip() for word in word_file]
        word_list = []
        for word in word_file:
            word_list.append(word.strip())
        return word_list
    
    def random(self):
        """Return random word from the word list"""
        return random.choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """A wordfinder class that will not include comments or empty lines"""
    def get_word_list(self, word_file):
        return [word.strip() for word in word_file if not word.startswith("#") and word.strip()]
