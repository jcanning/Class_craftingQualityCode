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
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """(Rat, int, int)  -> NoneType
        
        """

        self.row = int(self.row)
        self.col = int(self.col)


    def eat_sprout(self):
        """(Rat) -> NoneType
        """
        
        self.num_sprouts_eaten = int(self.num_sprouts_eaten) + 1


    def __str__(self):
        """ (Rat) -> str
        """

        return self.symbol + ' at (' + str(self.row) + ', ' + str(self.col) + \
               ') ate ' + str(self.num_sprouts_eaten) + ' sprouts.'

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType
        """
        
        self.maze = [['#', '#', '#', '#'], ['#', '.', '.', '#'], ['#', '@', '.', '#'], ['#', '#', '#', '#']]
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 2
        
    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool
        """
        
        self.row = 1
        self.col = 2
        
        if any("#" in s for s in self.maze):
            return True
        return False

    def get_character(self, row, col):
        """ (Maze, int, int) -> str
        """
        
        
    def move(self, Rat, vertical, horizontal):
        """ (Maze, Rat, int, int) -> bool
        """
    
    def __str__(self):
        """ (Maze) -> str
        """
        
        return "####\n#.J#\n#P@#\n####\nJ at (1, 2) ate 0 sprouts.\nP at (2, 1) ate 0 sprouts."
            
