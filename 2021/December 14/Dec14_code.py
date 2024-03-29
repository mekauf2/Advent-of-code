# --- Day 14: Extended Polymerization ---
# The incredible pressures at this depth are starting to put a strain on your
# submarine. The submarine has polymerization equipment that would produce
# suitable materials to reinforce the submarine, and the nearby
# volcanically-active caves should even have the necessary input elements in
# sufficient quantities.

# The submarine manual contains instructions for finding the optimal polymer
# formula; specifically, it offers a polymer template and a list of pair
# insertion rules (your puzzle input).
# You just need to work out what polymer would result after repeating the pair
# insertion process a few times.

# For example:

# NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C

# The first line is the polymer template - this is the starting point of the
# process.

# The following section defines the pair insertion rules.
# A rule like AB -> C means that when elements A and B are immediately adjacent,
# element C should be inserted between them.
# These insertions all happen simultaneously.

# So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

# The first pair (NN) matches the rule NN -> C, so element C is inserted
# between the first N and the second N.
# The second pair (NC) matches the rule NC -> B, so element B is inserted
# between the N and the C.
# The third pair (CB) matches the rule CB -> H, so element H is inserted
# between the C and the B.
# Note that these pairs overlap: the second element of one pair is the first
# element of the next pair. Also, because all pairs are considered
# simultaneously, inserted elements are not considered to be part of a pair
# until the next step.

# After the first step of this process, the polymer becomes NCNBCHB.

# Here are the results of a few steps using the above rules:

# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

# This polymer grows quickly. After step 5, it has length 97;
# After step 10, it has length 3073.
# After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times,
# and N occurs 865 times; taking the quantity of the most common element
# (B, 1749) and subtracting the quantity of the least common element (H, 161)
# produces 1749 - 161 = 1588.

# Apply 10 steps of pair insertion to the polymer template and find the most
# and least common elements in the result.
# What do you get if you take the quantity of the most common element and
# subtract the quantity of the least common element?

# --- Part Two ---
# The resulting polymer isn't nearly strong enough to reinforce the submarine.
# You'll need to run more steps of the pair insertion process;
# a total of 40 steps should do it.

# In the above example, the most common element is B
# (occurring 2192039569602 times) and the least common element
# is H (occurring 3849876073 times); subtracting these produces 2188189693529.

# Apply 40 steps of pair insertion to the polymer template
# and find the most and least common elements in the result.
# What do you get if you take the quantity of the most common element and
# subtract the quantity of the least common element?

def read_data(filepath):
    """
    Reads starter polymer and gets rules
    
    Input: filepath (filepath)
    
    Returns:
        polymer (str): starter polymer
        rules (dict): rules dictionary
    """
    with open(filepath) as f:
        data = f.readlines()
    
    polymer = data[0].strip()

    rules = {}
    for row in data[2:]:
        row = row.strip()
        pair, insert = row.split(" -> ")
        rules[pair] = insert
    
    return polymer, rules

def recursion_pairs_starter(filepath, steps):
    """
    Finds most and least common polymer frequencies and subtracts them
    
    Inputs:
        filepath (filepath)
        steps (int): number of steps to advance
    
    Returns (int): Delta in polymer frequency
    """
    polymer, rules = read_data(filepath)
    polymer_chars = len(polymer)
    counter = {}
    for i in range(polymer_chars - 1):
        pair = polymer[i:i+2]
        start, end = pair
        counter[start] = counter.get(start,0) + 1
        counter = recursion_pairs(pair, rules, steps, counter)
    counter[end] = counter.get(end,0) + 1
    print(counter)
    return max(counter.values()) - min(counter.values())

def recursion_pairs(pair, rules, steps, counter):
    """
    Builds up polymer frequencies dictionary

    Inputs:
        pair (str): polymer pair
        rules (dict): rules dictionary
        steps (int): number of steps to advance
        counter (dict): dictionary tracking pair frequency

    Returns:
        counter (dict): modified dictionary of pairs occuring
    """
    start, end = pair
    to_insert = rules[pair]
    if steps == 1:
        counter[to_insert] = counter.get(to_insert,0) + 1
        return counter
    else:
        new_pair = start + to_insert
        other_pair = to_insert + end
        counter[to_insert] = counter.get(to_insert,0) + 1
        counter = recursion_pairs(new_pair, rules, steps - 1, counter)
        counter = recursion_pairs(other_pair, rules, steps -1, counter)
    return counter

print(recursion_pairs_starter("Dec14_data.txt",40))