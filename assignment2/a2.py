# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """(Rat, str, int, int) -> NoneType
        >>> Player1 = Rat('P', 1, 4)
        >>> Player2 = Rat('J', 2, 3)
        
        """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = num_sprouts_eaten

    def set_location(self, row, col):
        """(Rat, int, int)  -> NoneType
        
        """

        row = 0
        col = 0
        
        for rows in self.row:
            row = self.row + row
            
        for cols in self.col:
            col = self.col + col


    def eat_sprout(self):
        """(Rat) -> NoneType
        """

        num_sprouts_eaten = 0
        
        for sprout in self.num_sprouts_eaten:
            num_sprouts_eaten = num_sprouts_eaten + 1


    def __str__(self):
        """ (Rat) -> str
        """

        return self.symbol + ' at (' + self.row + ', ' + self.col + \
               ') ate ' + self.num_sprouts_eaten + ' sprouts.'

        

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
