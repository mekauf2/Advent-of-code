# --- Day 13: Transparent Origami ---
# You reach another volcanically active part of the cave.
# It would be nice if you could do some kind of thermal imaging so you could
# tell ahead of time which caves are too hot to safely enter.

# Fortunately, the submarine seems to be equipped with a thermal camera!
# When you activate it, you are greeted with:

# Congratulations on your purchase! To activate this infrared thermal imaging
# camera system, please enter the code found on page 1 of the manual.
# Apparently, the Elves have never used this feature.
# To your surprise, you manage to find the manual; as you go to open it,
# page 1 falls out.
# It's a large sheet of transparent paper!
# The transparent paper is marked with random dots and includes instructions on
# how to fold it up (your puzzle input). For example:

# 6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5

# The first section is a list of dots on the transparent paper.
# 0,0 represents the top-left coordinate.
# The first value, x, increases to the right.
# The second value, y, increases downward.
# So, the coordinate 3,0 is to the right of 0,0,
# and the coordinate 0,7 is below 0,0.
# The coordinates in this example form the following pattern,
# where # is a dot on the paper and . is an empty, unmarked position:

# ...#..#..#.
# ....#......
# ...........
# #..........
# ...#....#.#
# ...........
# ...........
# ...........
# ...........
# ...........
# .#....#.##.
# ....#......
# ......#...#
# #..........
# #.#........

# Then, there is a list of fold instructions.
# Each instruction indicates a line on the transparent paper
# and wants you to fold the paper up (for horizontal y=... lines)
# or left (for vertical x=... lines).
# In this example, the first fold instruction is fold along y=7,
# which designates the line formed by all of the positions where y is 7
# (marked here with -):

# ...#..#..#.
# ....#......
# ...........
# #..........
# ...#....#.#
# ...........
# ...........
# -----------
# ...........
# ...........
# .#....#.##.
# ....#......
# ......#...#
# #..........
# #.#........

# Because this is a horizontal line, fold the bottom half up.
# Some of the dots might end up overlapping after the fold is complete,
# but dots will never appear exactly on a fold line.
# The result of doing this fold looks like this:

# #.##..#..#.
# #...#......
# ......#...#
# #...#......
# .#.#..#.###
# ...........
# ...........

# Now, only 17 dots are visible.

# Notice, for example, the two dots in the bottom left corner before the
# transparent paper is folded; after the fold is complete, those dots appear
# in the top left corner (at 0,0 and 0,1).
# Because the paper is transparent, the dot just below them in the result
# (at 0,3) remains visible, as it can be seen through the transparent paper.

# Also notice that some dots can end up overlapping;
# in this case, the dots merge together and become a single dot.

# The second fold instruction is fold along x=5, which indicates this line:

# #.##.|#..#.
# #...#|.....
# .....|#...#
# #...#|.....
# .#.#.|#.###
# .....|.....
# .....|.....

# Because this is a vertical line, fold left:

# #####
# #...#
# #...#
# #...#
# #####
# .....
# .....

# The instructions made a square!

# The transparent paper is pretty big, so for now, focus on just completing the
# first fold. After the first fold in the example above, 17 dots are visible -
# dots that end up overlapping after the fold is completed count as a single dot.

# How many dots are visible after completing just the first fold instruction on
# your transparent paper?

# --- Part Two ---
# Finish folding the transparent paper according to the instructions.
# The manual says the code is always eight capital letters.

# What code do you use to activate the infrared thermal imaging camera system?

import numpy as np
np.set_printoptions(edgeitems=1000, linewidth=1000)

def read_file_and_count_visible_dots(filepath, target_folds=np.inf):
    """
    Reads in instructrions for dots and folds and counts visible dots post
        instructions
    
    Input (filepath): filepath
    
    Returns (int): Number of visible dots
    """
    folds_count = 0

    with open(filepath) as f:
        data = f.readlines()

    grid = np.zeros((2,2), dtype = int)
    for row in data:
        if row == "\n":
            continue
        row = row.strip()
        if check_if_number(row[0]):
            values = row.split(",")
            dot_pair = []
            for value in values:
                dot_pair.append(int(value))
            grid = add_dot_to_grid(dot_pair, grid)
        elif folds_count < target_folds:
            fold = row.strip("fold along ")
            if fold[0] == "y":
                fold = int(fold.strip("y="))
                grid = fold_grid([0,fold], grid)
                folds_count +=1
            else:
                fold = int(fold.strip("x="))
                grid = fold_grid([fold,0], grid)
                folds_count +=1
    if target_folds == np.inf:
        with np.printoptions(threshold=np.inf):
            print(grid)
    return len(np.argwhere(grid > 0))


def check_if_number(str):
    """
    Checks if a string is a number
    
    Input (str): string
    
    Returns (bool): T/F if is number
    """
    try:
        int(str)
        return True
    except ValueError:
        return False

def add_dot_to_grid(dot_pair, grid):
    """
    Adds dot to gird
    
    Input:
        dots (list): dot coordinates
        grid (numpy.array): Current grid
    
    Returns (numpy.array): new_grid with dots as 1s
    """
    x,y = dot_pair
    y_size, x_size = grid.shape
    if x_size < x + 1:
        x_delta = x_size - (x+1)
        if y_size < y + 1:
            y_delta = y_size - (y+1)
            new_grid = np.zeros((y+1,x+1))
            new_grid[:y_delta, :x_delta] = grid
        else:
            new_grid = np.zeros((y_size,x+1))
            new_grid[:, :x_delta] = grid
    elif y_size < y + 1:
        y_delta = y_size - (y+1)
        new_grid = np.zeros((y+1,x_size))
        new_grid[:y_delta, :] = grid
    else:
        new_grid = grid
    
    new_grid[y,x] = 1

    return new_grid

def fold_grid(fold, grid):
    """
    Folds a grid along specified row / col
    
    Inputs:
        fold (list): location of fold
        grid (numpy.array): grid of dots
    
    Returns (numpy.array): Modified grid
    """
    x,y = fold
    if x == 0:
        to_fold = grid[y+1:, :]
        to_fold_inverted = np.flipud(to_fold)
        grid_remain = grid[:y, :]
    else:
        to_fold = grid[:, x+1:]
        to_fold_inverted = np.fliplr(to_fold)
        grid_remain = grid[:, :x]

    fold_y, fold_x = to_fold_inverted.shape
    remain_y, remain_x = grid_remain.shape
    
    if fold_x == remain_x:
        start_y = remain_y - fold_y
        grid_remain[start_y:, :] += to_fold_inverted
    else:
        start_x = remain_x - fold_x
        grid_remain[:, start_x:] += to_fold_inverted

    return grid_remain


print(read_file_and_count_visible_dots("Dec13_data.txt",1))
print(read_file_and_count_visible_dots("Dec13_data.txt"))