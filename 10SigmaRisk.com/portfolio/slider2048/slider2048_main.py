"""
Clone of 2048 sliding tiles game.

1) Slide tile in one of 4 possible directions.
2) If two tile have same numbers, merge them.
   Always merge "front" first.
   Do not merge same tile twice in one turn.
   * Define grid input to class object.
3) Create a "new tile" after sliding.
   Check for empty space, randomy assigne to empty space list.
4) Modify Class to allow arbitray length, width.

*  Grid starts with [0, 0] top-left, then [max-row, max-col] bottom right.
   Create empty [row, col] matrix filled with 0s to start.
** Optional, check for "win" when 2048 number is reached after each round.
   Printout "High Score" with max score reached per game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),  #JY add to base index.
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}
# Test indexing through dicitonary.  a_dict[key][list index].

# -------------------------------------------------------------------------- #
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    Input line, type list.  Return new_line, merged, type list.
    """
    # Initialize empty list of zeros.
    new_line = len(line) * [0]
    # Slide step.
    new = 0
    for num in range(len(line)):
        if line[num] != 0:
            # Copy non-zero value to next element of new_line.
            new_line[new] = line[num]
            new += 1
    # Merge step.
    for num in range(len(new_line)-1):
        if new_line[num] == 0:
            pass
        else:
            if new_line[num] == new_line[num+1]:
                new_line[num] *= 2
                new_line.pop(num+1)
                new_line.append(0)
    return new_line

# -------------------------------------------------------------------------- #
class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height=4, grid_width=6):
        self.height = grid_height
        self.width = grid_width
        # Set initial tiles.
        up_init = []
        down_init = []
        left_init = []
        right_init = []
        for col in range(self.width):
            up_init.append([0, col])
            down_init.append([self.height-1, col])
        for row in range(self.height):
            left_init.append([row, 0])
            right_init.append([row, self.width-1])
        self.init_tiles = {
            UP: up_init,
            DOWN: down_init,
            LEFT: left_init,
            RIGHT: right_init }
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = [[0 for dummy_col in range(self.width)]
                        for dummy_row in range(self.height)]
        # Other parts of code write INTO this self.grid using [row],[col].
        return self.grid

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for row in range(self.height):
            for col in range(self.width):
                value = self.grid[row][col]
                value_str = str(value)
        return value_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        front_tiles = self.init_tiles.get(direction)
        if (direction == UP) or (direction == DOWN):
            lrange = self.height
        else:
            lrange = self.width

        # Take each line and process.
        for line_num in range(len(front_tiles)):
            # Take the first tile(row, col), compute values of line.
            first = front_tiles[line_num]
            input_line_values = []
            for num in range(lrange):
                new_row = first[0] + OFFSETS[direction][0]*num
                new_col = first[1] + OFFSETS[direction][1]*num
                input_line_values.append(self.get_tile(new_row, new_col))
            output_line = merge(input_line_values)
            # Transfer line values into self.grid.
            for num in range(lrange):
                new_row = first[0] + OFFSETS[direction][0]*num
                new_col = first[1] + OFFSETS[direction][1]*num
                self.set_tile(new_row, new_col, output_line[num])
        self.new_tile()
        # After calling new_tile(), if False is returned, no empties.

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty square.
        The tile should be 2 90% of the time and 4 10% of the time.
        """
        # Randomly select a 0-valued grid square, if one exists.
        empties = []
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 0:
                    empties.append([row, col])
        if empties == []:
            print "No empty tile."
            result = False
        else:
            new_tile = random.choice(empties)
            new_row = new_tile[0]
            new_col = new_tile[1]
            result = True

            # Randomly assign value. Prob = 4 * 10% + 2 * 90%.
            prob_space = [4] * 1 + [2] * 9
            random.shuffle(prob_space)
            new_value = random.choice(prob_space)
            # Call set_tile to assign value to new tile.
            self.set_tile(new_row, new_col, new_value)
        return result

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value
        return self.grid

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        tile_value = self.grid[row][col]
        return tile_value

# -------------------------------------------------------------------------- #
poc_2048_gui.run_gui(TwentyFortyEight(4, 6))



