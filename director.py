from jumper import Jumper

class Director:
    """
    This will contain the method in order to performance each act
    """

    def __init__(self):

        self.terminal = Terminal()
        self.jumper = Jumper()
        self.hide_word = Hide_Word()
        self.is_palying = True
        self.input = ""
        self.guy = ""
        self.list_words = []
        self.first_game = True
    
    def star_game(self):
        self.guy = self.jumper.draw_jumper()
        self.hide_word.pick_word()
        self