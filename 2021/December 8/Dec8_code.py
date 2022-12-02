# --- Day 8: Seven Segment Search ---
# You barely reach the safety of the cave when the whale smashes into the cave
# mouth, collapsing it. Sensors indicate another exit to this cave at a much
# greater depth, so you have no choice but to press on.

# As your submarine slowly makes its way through the cave system, you notice
# that the four-digit seven-segment displays in your submarine are
# malfunctioning; they must have been damaged during the escape. You'll be in a
# lot of trouble without them, so you'd better figure out what's wrong.

# Each digit of a seven-segment display is rendered by turning on or off any of
# seven segments named a through g:

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# So, to render a 1, only segments c and f would be turned on; the rest would
# be off. To render a 7, only segments a, c, and f would be turned on.

# The problem is that the signals which control the segments have been mixed up
# on each display. The submarine is still trying to display numbers by
# producing output on signal wires a through g, but those wires are connected
# to segments randomly. Worse, the wire/segment connections are mixed up
# separately for each four-digit display!
# (All of the digits within a display use the same connections, though.)

# So, you might know that only signal wires b and g are turned on, but that
# doesn't mean segments b and g are turned on: the only digit that uses two
# segments is 1, so it must mean segments c and f are meant to be on. 
# With just that information, you still can't tell which wire (b/g) goes to
# which segment (c/f). For that, you'll need to collect more information.

# For each display, you watch the changing signals for a while, make a note of
# all ten unique signal patterns you see, and then write down a single four
# digit output value (your puzzle input). Using the signal patterns, you should
# be able to work out which pattern corresponds to which digit.

# For example, here is what you might see in a single entry in your notes:

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf
# (The entry is wrapped here to two lines so it fits; in your notes, it will
# all be on a single line.)

# Each entry consists of ten unique signal patterns, a | delimiter, and finally
# the four digit output value. Within an entry, the same wire/segment
# connections are used (but you don't know what the connections actually are).
# The unique signal patterns correspond to the ten different ways the submarine
# tries to render a digit using the current wire/segment connections. 
# Because 7 is the only digit that uses three segments, dab in the above
# example means that to render a 7, signal lines d, a, and b are on. Because 4
# is the only digit that uses four segments, eafb means that to render a 4,
# signal lines e, a, f, and b are on.

# Using this information, you should be able to work out which combination of
# signal wires corresponds to each of the ten digits.
# Then, you can decode the four digit output value. 
# Unfortunately, in the above example, all of the digits in the output value
# (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

# For now, focus on the easy digits. Consider this larger example:

# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
# fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
# fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
# cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
# efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
# gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
# gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
# cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
# ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
# gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
# fgae cfgab fg bagce

# Because the digits 1, 4, 7, and 8 each use a unique number of segments, you
# should be able to tell which combinations of signals correspond to those digits.
# Counting only digits in the output values (the part after | on each line), in
# the above example, there are 26 instances of digits that use a unique number
# of segments (highlighted above).

# In the output values, how many times do digits 1, 4, 7, or 8 appear?

# --- Part Two ---
# Through a little deduction, you should now be able to determine the remaining
# digits. Consider again the first example above:

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf
# After some careful analysis, the mapping between signal wires and segments
# only make sense in the following configuration:

#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc
# So, the unique signal patterns would correspond to the following digits:

# acedgfb: 8
# cdfbe: 5
# gcdfa: 2
# fbcad: 3
# dab: 7
# cefabd: 9
# cdfgeb: 6
# eafb: 4
# cagedb: 0
# ab: 1
# Then, the four digits of the output value can be decoded:

# cdfeb: 5
# fcadb: 3
# cdfeb: 5
# cdbaf: 3
# Therefore, the output value for this entry is 5353.

# Following this same process for each entry in the second, larger example
# above, the output value of each entry can be determined:

# fdgacbe cefdb cefbgd gcbe: 8394
# fcgedb cgb dgebacf gc: 9781
# cg cg fdcagb cbg: 1197
# efabcd cedba gadfec cb: 9361
# gecf egdcabf bgf bfgea: 4873
# gebdcfa ecba ca fadegcb: 8418
# cefg dcbef fcge gbcadfe: 4548
# ed bcgafe cdgba cbgef: 1625
# gbdfcae bgc cg cgb: 8717
# fgae cfgab fg bagce: 4315
# Adding all of the output values in this larger example produces 61229.

# For each entry, determine all of the wire/segment connections and decode the
# four-digit output values. What do you get if you add up all of the output values?

from numpy import number
from numpy.core.numeric import full


with open("Dec8_data.txt") as f:
    data = f.readlines()

observations = []
outputs = []
obs_and_outs = []
for row in data:
    obs, outs = row.strip().split("|")
    obs_clean = obs.rstrip().split(" ")
    observations.append(obs_clean)
    outs_clean = outs.strip().split(" ")
    outputs.append(outs_clean)
    obs_and_outs.append(obs_clean + outs_clean)

# Define how many segments are lit up for which numbers
# E.g. 6 segments is 0, 6, and 9

numbers_segs_dict = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}

# Create a dict of which segments are lit up for each number

segs_lit_dict_by_num = {0: [0,1,2,4,5,6], 1: [2,5], 2: [0,2,3,4,6],
                         3: [0,2,3,5,6], 4: [1,2,3,5], 5: [0,1,3,5,6],
                         6: [0,1,3,4,5,6], 7: [0,2,5], 8: [0,1,2,3,4,5,6],
                         9: [0,1,2,3,5,6]}

# Count total segments lit up when a given segment is lit
# E.g. when segment 0 (top) is lit up, there are a total of 43 segs lit
# from numbers 0, 2, 3, 5, 6, 7, 8, 9

total_segs_lit_by_seg = {k:(0,0) for k in range(0,10)}

for _, segs_lit in segs_lit_dict_by_num.items():
    lit = len(segs_lit)
    for seg in segs_lit:
        num_occur, total_segs = total_segs_lit_by_seg[seg]
        total_segs_lit_by_seg[seg] = (num_occur + 1, total_segs + lit)

# To make easier to look up in task2
total_segs_lit_by_seg_inverted = {v:k for k, v in total_segs_lit_by_seg.items()}


def task1(outputs, target_nums, numbers_dict):
    """
    Returns the number of times the target number appears in the output
        Note: must target all numbers in a given segment slot for this to work
    
    Inputs:
        outputs (list of list of str): A list of string outputs
        target_nums (list of ints): A list of target nums to find
        numbers_dict (dict of lists): Dictionary for how many lit up segments
            correspond to which number 
    
    Returns (int): Count of times number occurs
    """
    nd2 = numbers_dict.copy()
    segment_lengths_to_check = []
    for segments, numbers in numbers_dict.items():
        for target in target_nums:
            if target in numbers and target in nd2[segments]:
                nd2[segments].remove(target)
            if segments not in segment_lengths_to_check and not nd2[segments]:
                segment_lengths_to_check.append(segments)
    
    count = 0

    for output in outputs:
        for digit in output:
            if len(digit) in segment_lengths_to_check:
                count += 1

    return count


def task2(outputs, observations, segs_lit_by_num, segs_lit_by_seg):
    """
    Returns the sum of the output digits (each output is one set of digits)
    
    Inputs:
        outputs (list of list of str): A list of string outputs
        obs_and_outs (list of list of str): A list of combined observations
            and outputs
        segs_lit_by_num (dictionary): A dictionary containing the segments lit
            for each number
        segs_lit_by_seg (dictionary): A dictionary containing the total lit up
            segments across all numbers given a certain segement is lit
    
    Returns (int): sum of the outputs
    """
    output_nums = []
    for row, obs_set in enumerate(observations):
        obs_tuples = {"a": (0,0), "b": (0,0), "c": (0,0), "d": (0,0),
                      "e": (0,0), "f": (0,0), "g": (0,0)}
        obs_position_mapping = {"a": "", "b": "", "c": "", "d": "",
                      "e": "", "f": "", "g": ""}
        for obs in obs_set:
            segs_lit = len(obs)
            for letter in obs:
                num_occur, total_segs = obs_tuples[letter]
                obs_tuples[letter] = (num_occur + 1, total_segs + segs_lit)
        for letter, obs_pairing in obs_tuples.items():
            obs_position_mapping[letter] = segs_lit_by_seg[obs_pairing]
        
        full_num_for_a_row = ""
        for output in outputs[row]:
            output_segs = []
            for letter in output:
                output_segs.append(obs_position_mapping[letter])
            output_segs = sorted(output_segs)
            for num, segs_lit in segs_lit_by_num.items():
                if output_segs == segs_lit:
                    full_num_for_a_row += str(num)
                    break            
        output_nums.append(int(full_num_for_a_row))

    return sum(output_nums)

print(task1(outputs, [1,4,7,8], numbers_segs_dict))
print(task2(outputs, observations, segs_lit_dict_by_num, total_segs_lit_by_seg_inverted))

# Task 2 done with logic-game style code below (for fun)

# def task2_logical(outputs, obs_and_outs, segs_lit_by_num):
#     """
#     Returns the sum of the output digits (each output is one set of digits)
    
#     Inputs:
#         outputs (list of list of str): A list of string outputs
#         obs_and_outs (list of list of str): A list of combined observations
#             and outputs
#         segs_lit_by_num (dictionary): A dictionary containing the segments lit
#             for each number
    
#     Returns (int): sum of the outputs
#     """
#     output_nums = []
#     for row, set_nums in enumerate(obs_and_outs):
#         string_by_segs = {k:[] for k in range(0,10)}
#         letter_to_seg = {"a": "", "b": "", "c": "", "d":"", "e": "", "f": "",
#                          "g": ""}
#         for string in set_nums:
#             length = len(string)
#             string_by_segs[length].append(string)

#         potential_middle = []
#         potential_right = []

#         # Delta between one and seven is top, also gives RHS items
#         if string_by_segs[2] and string_by_segs[3]:
#             for letter in string_by_segs[3][0]:
#                 if letter not in string_by_segs[2][0]:
#                     letter_to_seg[letter] = 0
#                 else:
#                     potential_right.append(letter)

#         # If have not determined top, have seven and four (also gives RHS)
#         if string_by_segs[3] and string_by_segs[4] and not string_by_segs[2]:
#             for letter in string_by_segs[3][0]:
#                 if letter not in string_by_segs[4][0]:
#                     letter_to_seg[letter] = 0
#                 else:
#                     potential_right.append(letter)

#         # Determine RHS
#         if potential_right and string_by_segs[6]:
#             for letter in potential_right:
#                 if not potential_right:
#                     break
#                 for string_set in string_by_segs[6]:
#                     if letter not in string_set:    
#                         letter_to_seg[letter] = 2
#                         potential_right.remove(letter)

#                         remain_letter = potential_right[0]
#                         letter_to_seg[remain_letter] = 5
#                         potential_right.remove(remain_letter)
#                         break
      
#         # Determine potential middle bar
#         if string_by_segs[3] and string_by_segs[4]:
#             for letter in string_by_segs[4][0]:
#                 if letter not in string_by_segs[3][0]:
#                     potential_middle.append(letter)

#         if string_by_segs[2] and string_by_segs[4] and not potential_middle:
#             for letter in string_by_segs[4][0]:
#                 if letter not in string_by_segs[3][0]:
#                     potential_middle.append(letter)


#         # Determine middle bar and top LHS item once we have middle
#         if string_by_segs[5] and potential_middle:
#             for letter in potential_middle:
#                 if not potential_middle:
#                     break
#                 for set_strings in string_by_segs[5]:
#                     if letter not in set_strings:
#                         letter_to_seg[letter] = 1
#                         potential_middle.remove(letter)
                            
#                         remain_letter = potential_middle[0]
#                         letter_to_seg[remain_letter] = 3
#                         potential_middle.remove(remain_letter)
#                         break
            
#         if string_by_segs[6] and potential_middle:
#             for letter in potential_middle:
#                 if not potential_middle:
#                     break
#                 for set_strings in string_by_segs[6]:
#                     if letter not in set_strings:
#                         letter_to_seg[letter] = 3
#                         potential_middle.remove(letter)
                            
#                         remain_letter = potential_middle[0]
#                         letter_to_seg[remain_letter] = 1
#                         potential_middle.remove(remain_letter)
#                         break
            
#         # Time to determine bottom LHS and bottom row
#         potential_bottom_left_and_bottom = []
#         for letter, pos in letter_to_seg.items():
#             if pos == "":
#                 potential_bottom_left_and_bottom.append(letter)

#         # Of 5 segment items, 3 and 5 are missing 1 letter that we don't have
#         # Of 6 segment items, only 9 is missing 1 letter we don't have
#         # All of above with only 1 missing are missing bottom LHS

#         for string_set in string_by_segs[5]:
#             if not potential_bottom_left_and_bottom:
#                 break
#             pot_bottom_left_5 = []
#             for letter in string_set:
#                 if letter in potential_bottom_left_and_bottom:
#                     pot_bottom_left_5.append(letter)
#             if len(pot_bottom_left_5) == 1:
#                 letter = pot_bottom_left_5[0]
#                 letter_to_seg[letter] = 6
#                 potential_bottom_left_and_bottom.remove(letter)

#                 remain_letter = potential_bottom_left_and_bottom[0]
#                 letter_to_seg[remain_letter] = 4
#                 potential_bottom_left_and_bottom.remove(remain_letter)
#                 break

        
#         # If using the 5 segments failed, then try with 6 seg
#         for string_set in string_by_segs[6]:
#             if not potential_bottom_left_and_bottom:
#                 break
#             pot_bottom_left_6 = []
#             for letter in string_set:
#                 if letter in potential_bottom_left_and_bottom:
#                     pot_bottom_left_6.append(letter)
#             if len(pot_bottom_left_6) == 1:
#                 letter = pot_bottom_left_6[0]
#                 letter_to_seg[letter] = 6
#                 potential_bottom_left_and_bottom.remove(letter)
                
#                 remain_letter = potential_bottom_left_and_bottom[0]
#                 letter_to_seg[remain_letter] = 4
#                 potential_bottom_left_and_bottom.remove(remain_letter)
#                 break

#         # Can now find the output numbers for the set

#         full_num_for_a_row = ""
#         for output in outputs[row]:
#             output_segs = []
#             for letter in output:
#                 output_segs.append(letter_to_seg[letter])
#             output_segs = sorted(output_segs)
#             for num, segs_lit in segs_lit_by_num.items():
#                 if output_segs == segs_lit:
#                     full_num_for_a_row += str(num)
#                     break            
#         output_nums.append(int(full_num_for_a_row))

#     return sum(output_nums)

# print(task2_logical(outputs, obs_and_outs, segs_lit_dict_by_num))
