from jumper import Jumper
from hide_word import Hide_Words

class Director:
    """
    This will contain the method in order to performance each act
    """

    def __init__(self):

        self.terminal = Terminal()
        self.jumper = Jumper()
        self.hide_word = Hide_Words(self.jumper)
        self.is_palying = True
        self.pick_letter= ""
        self.guy = ""
        self.list_words = []
        self.first_game = True
    
    def star_game(self):
        """
        This guy will star the game means that it will draw the skydiver
        """
        self.guy = self.jumper.draw_jumper()
        self.hide_word.hide_word()
        self.hidden_word = self.hide_word.hide_word()
        self.run_game()

    def get_inputs(self):
        """
        This will update the letter
        """
        self.pick_letter = self.terminal.get_input("Type in a letter: ")

    def update(self):
        """
        This will scan the word and show the letter if is in
        """
        self.hidden_word = self.hide_word.scanning_letter(self.pick_letter)
        self.guy = self.jumper.get_jumper()
        self.run = False
        for i in self.hidden_word:
            if i == "_":
                self.run = True
        if self.jumper.get_end_game() == True:
            self.run = False

    def outcome(self):
        """
        It will show the new shydiver if we picked the rigth letter or remove a line from skydiver if is not
        """
        self.terminal.write(self.guy)
        self.terminal.write(self.hidden_word)

    def run_game(self):
        """
        This will activate all functions
        """
        while self.run:
            if self.first_game == False:
                self.get_inputs()
                self.update()
                self.outcome()
                self.first_game = False