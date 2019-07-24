# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, an integer in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row 
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxes", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7 
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
# 
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

from collections import defaultdict


# check_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]


BOXES_IN_SET = 9
COLS_IN_BLOCK = 3
MAX_VALID_NUMBER = 9
MIN_VALID_NUMBER = 0
NUM_COLS = 9
NUM_ROWS = 9
ROWS_IN_BLOCK = 3


def sanity_checks(grid):
    if not grid or type(grid) not list or len(grid) != NUM_ROWS:
        return None

    for row in grid:
        if not row or type(row) not list or len(row) != NUM_ROWS:
            return None

        for number in row:
            if not number or type(number) not int or number < MIN_VALID_NUMBER or number > MAX_VALID_NUMBER:
                return None

    return True


def check_vertical_values(grid):
    results = []
    col_idx = 0
    while col_idx < NUM_COLS:
        values_counts = defaultdict(int)
        for row in grid:
            values_counts[row[col_idx]] += 1

        results.append(check_values(values_counts))
        col_idx += 1

    return all(results)  # returns True (valid) if all verticals returned True (valid), else False


def check_horizontal_values(grid):
    results = []

    for row in grid:
        values_counts = defaultdict(int)
        for val in row:
            values_counts[val] += 1

        results.append(check_values(values_counts))

    return all(results)  # returns True (valid) if all horizontals returned True (valid), else False


# todo - change to account for zero values
def check_values(values_counts):
    if values_dict[0] > 0:  # one or more missing values
        return check_entries_incomplete(values_counts)
    else:                   # all values filled
        return check_entries_complete(values_counts)


def check_entries_complete(values_counts):
    for count_tuple in values_counts.items():
        if count_tuple[1] != 1:
            return False

    return True


def check_entries_incomplete(values_counts):
    num_boxes_filled = BOXES_IN_SET - values_counts[0]
    total_seen = 0

    for count_tuple in values_counts.items():
        digit = values_counts[0]
        count = values_counts[1]

        if digit != 0 and count > 1:
            return False
        else:
            total_seen += count

    return True


def check_blocks_of_nine(grid):
    results = []

    for row_idx in range(0, 7, 3):       # (0, 3, 6)
        for col_idx in range(0, 7, 3):   # (0, 3, 6)

            local_row_idx = 0  # will be 0 -> 2 (at this point in grid)
            local_col_idx = 0  # will be 0 -> 2 (at this point in grid)
            values_counts = defaultdict(int)

            # add nine entries from block
            while row_idx < ROWS_IN_BLOCK:
                while col_idx < COLS_IN_BLOCK:
                    val = grid[row_idx][col_idx]
                    values_counts[val] += 1

                    col_idx += 1

                row_idx += 1

            results.append(check_values(values_counts))

    return all(results)  # returns True (valid) if all blocks of nine returned True (valid), else False


def check_sudoku(grid):
    results = []

    sane = sanity_checks(grid)
    if sane is None:
        return None

    results.append(check_horizontal_values(grid))
    results.append(check_vertical_values(grid))
    results.append(check_blocks_of_nine(grid))

    return all(results)  # returns True (valid) if all checks passed with True (valid), else False


print check_sudoku(ill_formed) # --> None
print check_sudoku(valid)      # --> True
print check_sudoku(invalid)    # --> False
print check_sudoku(easy)       # --> True
print check_sudoku(hard)       # --> True

