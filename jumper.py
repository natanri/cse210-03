class Jumper:

    """
    This class will initialize to drawing a jumper
    """
    def __init__(self):
        self._incorrect_letter = 0
        self._end_game = False

    def draw_jumper(self):
        """
        If the letter is incorrect then this function will erase a line until jumper die.
        """

        if self._incorrect_letter == 0:
            jumper = """
              ___
             /___\
             \   /
              \ /
               0
              /|\
              / \
            """

        elif self._incorrect_letter == 1:
            jumper = """
              
             /___\\
            \\   /
             \\ /
               0
              /|\\
              / \\
            """

        elif self._incorrect_letter == 2:
            jumper = """
              
              
            \\   /
             \\ /
               0
              /|\\
              / \\
            """
        elif self._incorrect_letter == 3:
            jumper = """
              
             
         
             \\ /
               0
              /|\\
              / \\
            """

        elif self._incorrect_letter == 4:
            jumper = """
              
             
            
             
               X
              /|\\
              / \\
            """
            self._end_game = True
        return jumper

    def get_jumper(self):
        """
        this will return a draw jumper
        """
        return self.draw_jumper()

    def get_end_game(self):
        """
        This will return the end game attribute
        """
        return self._end_game

    def set_incorrect_letter(self, letter):

        """
        This will set the incorrect letter
        """
        self._incorrect_letter = letter


    
