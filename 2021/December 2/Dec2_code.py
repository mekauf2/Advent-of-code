# --- Day 2: Dive! ---
# Now, you need to figure out how to pilot this thing.

# It seems like the submarine can take a series of commands like 
# forward 1, down 2, or up 3:

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
# Note that since you're on a submarine, down and up affect your depth,
# and so they have the opposite result of what you might expect.

# The submarine seems to already have a planned course (your puzzle input). 
# You should probably figure out where it's going. 
# 
# For example:

# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
# 
# Your horizontal position and depth both start at 0. 
# 
# The steps above would then modify them as follows:

# forward 5 adds 5 to your horizontal position, a total of 5.
# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.
# down 8 adds 8 to your depth, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.
# After following these instructions, you would have a horizontal position of
# 15 and a depth of 10. (Multiplying these together produces 150.)

# Calculate the horizontal position and depth you would have after following
# the planned course. 

# What do you get if you multiply your final horizontal position
# by your final depth?

directions = []
with open("Dec2_data.txt") as f:
    for row in f:
        intial = tuple(row.strip().split(" "))
        adder = (intial[0], int(intial[1]))
        directions.append(adder)

def task_1(directions):
    """
    Multiplies final horizontal and depth position given 0,0 start

    Input (list of tuples): A list of tuples containing
        i: direciton to move;
        ii: how far to move
    
    Retunrs (int): Final horizontal * final depth
    """

    horizontal = 0
    depth = 0
    for direction, distance in directions:
        assert direction in ["forward", "down", "up"], print(direction, " not recognized")
        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        else:
            depth -= distance
    return horizontal * depth

print(task_1(directions))

# Based on your calculations, the planned course doesn't seem to make any sense.
# You find the submarine manual and discover that the process is actually
# slightly more complicated.

# In addition to horizontal position and depth, you'll also need to track a
# third value, aim, which also starts at 0. The commands also mean something
# entirely different than you first thought:

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#   It increases your horizontal position by X units.
#   It increases your depth by your aim multiplied by X.

# Again note that since you're on a submarine, down and up do the opposite of
# what you might expect: "down" means aiming in the positive direction.

# Now, the above example does something different:

# forward 5 adds 5 to your horizontal position, a total of 5.
#   Because your aim is 0, your depth does not change.
# down 5 adds 5 to your aim, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13. 
#   Because your aim is 5, your depth increases by 8*5=40.
# up 3 decreases your aim by 3, resulting in a value of 2.
# down 8 adds 8 to your aim, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.
# Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
# After following these new instructions, you would have a horizontal position of 15
# and a depth of 60. (Multiplying these produces 900.)

# Using this new interpretation of the commands, calculate the horizontal
# position and depth you would have after following the planned course. 
# What do you get if you multiply your final horizontal position by your final depth?

def task_2(directions):
    """
    Multiplies final horizontal and depth position given 0,0 start

    Input (list of tuples): A list of tuples containing
        i: direciton to move;
        ii: how far to move
    
    Retunrs (int): Final horizontal * final depth
    """

    horizontal = 0
    aim = 0
    depth = 0
    for direction, distance in directions:
        assert direction in ["forward", "down", "up"], print(direction, " not recognized")
        if direction == "forward":
            horizontal += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
        else:
            aim -= distance
    return horizontal * depth

print(task_2(directions))


##### Alternative that does not iterate through list 3x ########

def task_1_alt(move, position):
    """
    Calculates next horizontal and depth position

    Input:
        i: (tuple): a tuple containing direction to move and how far to move
        ii: (tuple): a tuple containing current position
    
    Retunrs (tuple): Ints representing horizontal and depth positions
    """

    horizontal, depth = position
    direction, distance = move
    assert direction in ["forward", "down", "up"], print(direction, " not recognized")
    if direction == "forward":
        horizontal += distance
    elif direction == "down":
        depth += distance
    else:
        depth -= distance
    return (horizontal, depth)


def task_2_alt(move, position):
    """
    Calculates next horizontal, depth, and aim positions

    Input:
        i: (tuple): a tuple containing direction to move and how far to move
        ii: (tuple): a tuple containing current position
    
    Retunrs (tuple): Ints representing horizontal, depth, and aim positions
    """

    horizontal, depth, aim = position
    direction, distance = move
    assert direction in ["forward", "down", "up"], print(direction, " not recognized")
    if direction == "forward":
        horizontal += distance
        depth += aim * distance
    elif direction == "down":
        aim += distance
    else:
        aim -= distance
    return (horizontal, depth, aim)

with open("Dec2_data.txt") as f:
    hor, depth = 0,0
    hor2, depth2, aim = 0,0,0
    for row in f:
        intial = tuple(row.strip().split(" "))
        direction = (intial[0], int(intial[1]))
        hor, depth = task_1_alt(direction, (hor, depth))
        hor2, depth2, aim = task_2_alt(direction, (hor2, depth2, aim))
    print("task 1:", hor * depth, ", task 2:", hor2 * depth2)

