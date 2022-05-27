import random

class Hide_Words:

    def __init__(self, jumper):

        self.list_words = ["pencil", "computer", "cellphone", "software", "develop"]
        self.hidden_word = []
        self.select_word = ""
        self.select_letter = ""
        self.word_listed = []
        self.length = 0
        self.errors = 0
        self.jumper = jumper


    def pick_word(self):

        """
        select a word
        """
        self.select_word = random.choice(self.list_words)
        self.length = len(self.select_word)
        self.word_listed = [char for char in self.select_word]
        return(self.select_word)

    def hide_word(self):
        """
        Pick the word and becomes into dashes
        """
        self.hidden_word = ["_"] * self.length
        return(self.hidden_word)

    def scanning_letter(self, letter):
        """
        scan the word picked to verify if is in
        """
        self.select_letter = letter
        if self.select_letter in self.select_word:
            self.select_word = self._show_letter(self.select_letter)
            return self.select_word

        else:
            self.errors += 1
            self.jumper.set_incorrect_letter(self.errors)
            return self.select_word

    def _show_letter(self, letter):
        """
        reveal the letter
        """
        self.select_letter = letter
        for i in range(self.length):
            if self.select_letter == self.word_listed[i]:
                self.select_word[i] = self.select_letter
        return(self.select_word)

