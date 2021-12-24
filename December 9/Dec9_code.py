# --- Day 9: Smoke Basin ---
# These caves seem to be lava tubes.
# Parts are even still volcanically active; small hydrothermal vents release
# smoke into the caves that slowly settles like rain.

# If you can model how the smoke flows through the caves, you might be able to
# avoid it and be that much safer. 
# The submarine generates a heightmap of the floor of the nearby caves for you
# (your puzzle input).

# Smoke flows to the lowest point of the area it's in. 
# For example, consider the following heightmap:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# Each number corresponds to the height of a particular location, where 9 is
# the highest and 0 is the lowest a location can be.

# Your first goal is to find the low points - the locations that are lower than
# any of its adjacent locations. Most locations have four adjacent locations
# (up, down, left, and right); locations on the edge or corner of the map have
# three or two adjacent locations, respectively.
# (Diagonal locations do not count as adjacent.)

# In the above example, there are four low points, all highlighted: two are in
# the first row (a 1 and a 0), one is in the third row (a 5), and one is in the
# bottom row (also a 5). All other locations on the heightmap have some lower
# adjacent location, and so are not low points.

# The risk level of a low point is 1 plus its height. 
# In the above example, the risk levels of the low points are 2, 1, 6, and 6. 
# The sum of the risk levels of all low points in the heightmap is therefore 15.

# Find all of the low points on your heightmap. 
# What is the sum of the risk levels of all low points on your heightmap?

import numpy as np

with open("Dec9_sample.txt") as f:
    data = f.readlines()

cleaned = []
for row in data:
    all_nums = row.strip()
    indiv_num = []
    for num in all_nums:
        indiv_num.append(int(num))
    cleaned.append(indiv_num)

df = np.array(cleaned)

def task1(df):
    """
    Returns sum of risk levels associated with low points; 
        risk level = low point value + 1
    
    Input:
        df (np.array of ints): array of heights
    
    Returns (int): sum of risk levels associated with low points
    """
    landscape = np.ones(df.shape)
    rows, cols = df.shape
    for r in range(rows):
        row = df[r, :]
        for j, val in enumerate(row):
            if (j != 0 and val > row[j-1]) or (j != cols - 1 and val > row[j + 1]):
                landscape[r,j] = 0
    
    # print(df)
    # print(landscape)
    potential_lows = np.where(landscape == 1)
    # print(potential_lows[0])
    for i, x in enumerate(potential_lows[0]):
        y = potential_lows[1][i]
        val = df[x,y]
        # print(x,y,val)
        if (x != 0 and val > df[x-1, y]) or (x != rows - 1 and val > df[x+1, y]):
            landscape[x,y] = 0

    # for c in range(cols):
    #     col = df[:, c]
    #     print(col)
    #     for i, val in enumerate(col):
    #         if (i != 0 and val > col[i-1]) or (i != rows - 1 and val > col[i + 1]):
    #             landscape[i, c] = 0
    # print(landscape)

    num_low_points = len(np.where(landscape == 1)[0])

    return np.sum(landscape * df) + num_low_points

print(task1(df))
