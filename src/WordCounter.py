import sys

class WordCounter:

    def __init__(self, sentence):
        self.sentence =  sentence
        self.count = 0
        self.shortestword = sys.maxsize
        self.longestword = 0

    def count_words(self):
        for i in self.sentence.split(" "):
            self.count += 1
            self.shortestword = min(self.shortestword, len(i))
            self.longestword = max(self.longestword, len(i))

    def get_word_count(self):
        return self.count

    def get_shortest_word(self):
        return self.shortestword

    def get_longest_word(self):
        return self.longestword

 