# --- Day 5: Hydrothermal Venture ---
# You come across a field of hydrothermal vents on the ocean floor!
# These vents constantly produce large, opaque clouds, so it would be best to
# avoid them if possible.

# They tend to form in lines;
# the submarine helpfully produces a list of nearby lines of vents
# (your puzzle input) for you to review. For example:

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
# where x1,y1 are the coordinates of one end the line segment and 
# x2,y2 are the coordinates of the other end. 
# These line segments include the points at both ends. 
# 
# In other words:

# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines:
# lines where either x1 = x2 or y1 = y2.

# So, the horizontal and vertical lines from the above list would produce the
# following diagram:

# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9.
# Each position is shown as the number of lines which cover that point or .
# if no line covers that point. The top-left pair of 1s, for example, comes
# from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 
# 0,9 -> 5,9 and 0,9 -> 2,9.

# To avoid the most dangerous areas, you need to determine the number of points
# where at least two lines overlap. In the above example, this is anywhere in
# the diagram with a 2 or larger - a total of 5 points.

# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

# --- Part Two ---
# Unfortunately, considering only horizontal and vertical lines doesn't give
# you the full picture; you need to also consider diagonal lines.

# Because of the limits of the hydrothermal vent mapping system, the lines in
# your list will only ever be horizontal, vertical, or a diagonal line at
# exactly 45 degrees. In other words:

# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Considering all lines from the above example would now produce the following 
# diagram:

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....

# You still need to determine the number of points where at least two lines overlap.
# In the above example, this is still anywhere in the diagram with a 2 or larger
# - now a total of 12 points.

# Consider all of the lines. At how many points do at least two lines overlap?

import numpy as np

with open ("Dec5_data.txt") as f:
    data = f.readlines()

pairings = []
input_max = 0
for row in data:
    cleaned = row.strip().split(" ")
    pair1 = tuple(map(int,cleaned[0].split(",")))
    # Cleaned[1] is arrow character
    pair2 = tuple(map(int,cleaned[2].split(",")))
    pairings.append((pair1, pair2))
    pair_max = max(max(pair1), max(pair2))
    input_max = max(input_max, pair_max)

input_max += 1 # Index to 0

tracker = np.zeros(input_max * input_max).reshape(input_max, input_max)

def part1(tracker, pairings):
    """
    Finds the number of tiles of concer for horizontal and vertical lines only

    Inputs:
        tracker(np.array): blank tracker
        pairings(list of tuples): pairings to check
    
    Returns (int): number of troubling spots (index > 2)
    """
    tracker = np.copy(tracker)
    for (x1,y1), (x2, y2) in pairings:
        # Note that x gives col num and y gives row num
        if x1 != x2 and y1 == y2:
            local_min = min(x1, x2)
            local_max = max(x1, x2) + 1
            tracker[y1, local_min:local_max] +=1
        elif y1 != y2 and x1 == x2:
            local_min = min(y1, y2)
            local_max = max(y1, y2) + 1
            tracker[local_min:local_max, x1] +=1

    locations_of_conern = np.where(tracker >= 2)
    return len(locations_of_conern[0])

def part2(tracker, pairings):
    """
    Finds the number of tiles of concer for hor, vert, diagonal lines

    Inputs:
        tracker(np.array): blank tracker
        pairings(list of tuples): pairings to check
    
    Returns (int): number of troubling spots (index > 2)
    """
    tracker = np.copy(tracker)
    for (x1,y1), (x2, y2) in pairings:
        # Note that x gives col num and y gives row num
        if x1 != x2 and y1 == y2:
            local_min = min(x1, x2)
            local_max = max(x1, x2) + 1
            tracker[y1, local_min:local_max] +=1
        elif y1 != y2 and x1 == x2:
            local_min = min(y1, y2)
            local_max = max(y1, y2) + 1
            tracker[local_min:local_max, x1] +=1
        else:
            x,y = x1, y1
            while x != x2 and y != y2:
                tracker[y,x] +=1
                x = x + 1 if x < x2 else x - 1
                y = y + 1 if y < y2 else y - 1
            tracker[y,x] += 1

    locations_of_conern = np.where(tracker >= 2)
    return len(locations_of_conern[0])

print(part1(tracker, pairings))
print(part2(tracker, pairings))