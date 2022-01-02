# --- Day 12: Passage Pathing ---
# With your submarine's subterranean subsystems subsisting suboptimally,
# the only way you're getting out of this cave anytime soon is by finding a
# path yourself.
# Not just a path - the only way to know if you've found the best path is to find all of them.

# Fortunately, the sensors are still mostly working, 
# and so you build a rough map of the remaining caves (your puzzle input).
# 
# For example:

# start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end
# This is a list of how all of the caves are connected.
# You start in the cave named start, and your destination is the cave named end.
# An entry like b-d means that cave b is connected to cave d -
# that is, you can move between them.

# So, the above cave system looks roughly like this:

#     start
#     /   \
# c--A-----b--d
#     \   /
#      end

# Your goal is to find the number of distinct paths that start at start,
# end at end, and don't visit small caves more than once.
# There are two types of caves: big caves (written in uppercase, like A) and
# small caves (written in lowercase, like b).
# It would be a waste of time to visit any small cave more than once,
# but big caves are large enough that it might be worth visiting them multiple
# times.
# So, all paths you find should visit small caves at most once,
# and can visit big caves any number of times.

# Given these rules, there are 10 paths through this example cave system:

# start,A,b,A,c,A,end
# start,A,b,A,end
# start,A,b,end
# start,A,c,A,b,A,end
# start,A,c,A,b,end
# start,A,c,A,end
# start,A,end
# start,b,A,c,A,end
# start,b,A,end
# start,b,end
# (Each line in the above list corresponds to a single path;
# the caves visited by that path are listed in the order they are visited and
# separated by commas.)

# Note that in this cave system, cave d is never visited by any path:
# to do so, cave b would need to be visited twice
# (once on the way to cave d and a second time when returning from cave d),
# and since cave b is small, this is not allowed.

# Here is a slightly larger example:

# dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc

# The 19 paths through it are as follows:

# start,HN,dc,HN,end
# start,HN,dc,HN,kj,HN,end
# start,HN,dc,end
# start,HN,dc,kj,HN,end
# start,HN,end
# start,HN,kj,HN,dc,HN,end
# start,HN,kj,HN,dc,end
# start,HN,kj,HN,end
# start,HN,kj,dc,HN,end
# start,HN,kj,dc,end
# start,dc,HN,end
# start,dc,HN,kj,HN,end
# start,dc,end
# start,dc,kj,HN,end
# start,kj,HN,dc,HN,end
# start,kj,HN,dc,end
# start,kj,HN,end
# start,kj,dc,HN,end
# start,kj,dc,end

# Finally, this even larger example has 226 paths through it:

# fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW
# How many paths through this cave system are there that visit small caves at most once?

def read_data(file_path):
    """
    Reads in data for possible paths

    Input:
        file_path (filepath): location of data
    
    Returns:
        paths_dict (dict): dictionary of all path combos
        big_caves (set): set of all big caves
    """
    with open(file_path) as f:
        data = f.readlines()
    
    pairs_dict = {}
    big_caves = set()

    for row in data:
        row = row.strip()
        values = row.split("-")
        start, stop = values
        if start in pairs_dict:
            pairs_dict[start].append(stop)
        else:
            pairs_dict[start] = [stop]
        if stop in pairs_dict:
            pairs_dict[stop].append(start)
        else:
            pairs_dict[stop] = [start]
        if start.isupper():
            big_caves.add(start)
        if stop.isupper():
            big_caves.add(stop)
    
    return pairs_dict, big_caves

def find_paths(file_path, num_revisits=0, time_reivist=0,
                             smalls_cannot_revisit = set(["start", "end"])):
    """
    Finds all potential paths given constraint that you cannot enter a small
        cave more than 1x

    Input:
        file_path (filepath): location of data
        num_revisits (int): number of small caves can revisit
        times_revisit (int): number of times can revisit same small cave
        smalls_cannot_revisit (set): small caves you cannot revisit
    
    Returns (int): number of paths
    """
    pairs_dict, big_caves = read_data(file_path)
    small_caves_visited = set(["start"])
    small_caves_revisited = {}
    possible_paths = compute_next_step("start", pairs_dict, 
                                       big_caves, small_caves_visited,
                                       small_caves_revisited, num_revisits,
                                       time_reivist, smalls_cannot_revisit)
    final_paths = []
    for potential_path in possible_paths:
        potential_path.insert(0, "start")
        final_paths.append(potential_path)

    return len(final_paths)

def update_revisit_dictionary(step, big_caves, small_caves_revisited,
                        num_revisits, time_revisit, smalls_cannot_revisit):
    """
    Updates small caves revisit dictionary

    Input:
        step (str): current cave sub is in
        big_caves (set): set of all big caves
        small_caves_revisited (dict): dictionary of smalls revisited and times
            revisited
        num_revisits (int): number of small caves can revisit
        times_revisit (int): number of times can revisit same small cave
        smalls_cannot_revisit (set): small caves you cannot revisit
    
    Returns (dict): small_caves_revisted (updated if need be)
    """   

    if len(small_caves_revisited) < num_revisits:
        if step not in smalls_cannot_revisit and step not in big_caves:
            if num_revisits > 0 and time_revisit > 0:
                if small_caves_revisited.get(step,-1) < time_revisit:
                    small_caves_revisited2 = small_caves_revisited.copy()
                    small_caves_revisited2[step] = small_caves_revisited2.get(
                                                                    step, -1) \
                                                                    + 1
                    return small_caves_revisited2
    return small_caves_revisited       

def determine_if_can_revisit(step, big_caves, small_caves_revisited,
                             num_revisits, time_revisit, smalls_cannot_revisit):
    """
    Determines if can revisit the small cave

    Input:
        step (str): current cave sub is in
        big_caves (set): set of all big caves
        small_caves_revisited (dict): dictionary of smalls revisited and times
            revisited
        num_revisits (int): number of small caves can revisit
        times_revisit (int): number of times can revisit same small cave
        smalls_cannot_revisit (set): small caves you cannot revisit
    
    Returns (bool): T/F if can revisit or not
    """ 

    if time_revisit > 0 and num_revisits > 0:
        if len(small_caves_revisited) < num_revisits:
            if step in small_caves_revisited:
                if small_caves_revisited[step] < time_revisit:
                    return True
            elif step not in smalls_cannot_revisit and step not in big_caves:
                return True
    return False

def compute_next_step(current_step, paths_dict, big_caves,
                      small_caves_visited, small_caves_revisited, num_revisits,
                      time_revisit, smalls_cannot_revisit):
    """
    Finds the next potential step of a path

    Input:
        current_step (str): current cave sub is in
        paths_dict (dict): dictionary of all path combos
        big_caves (set): set of all big caves
        small_caves_visited (set): set of small caves visited (cannot revisit)
        small_caves_revisited (dict): dictionary of smalls revisited and times
            revisited
        num_revisits (int): number of small caves can revisit
        times_revisit (int): number of times can revisit same small cave
        smalls_cannot_revisit (set): small caves you cannot revisit
    
    Returns (list): output of potential paths
    """
    if current_step == "end":
        return [[]]
    else:
        output = []
        potential_next_steps = paths_dict[current_step]
        for step in potential_next_steps:
            small_caves_visited2 = small_caves_visited.copy()
            small_caves_revisited2 = small_caves_revisited.copy()
            if step not in small_caves_visited:
                if step not in big_caves:
                    small_caves_visited2.add(step)
                options = compute_next_step(step, paths_dict, big_caves,
                                            small_caves_visited2,
                                            small_caves_revisited2,
                                            num_revisits, time_revisit,
                                            smalls_cannot_revisit)
                for path in options:
                    output.append([step] + path)
            elif determine_if_can_revisit(step, big_caves,
                                          small_caves_revisited, num_revisits,
                                          time_revisit, smalls_cannot_revisit):
                small_caves_revisited2 = update_revisit_dictionary(step, big_caves,
                                                               small_caves_revisited2,
                                                               num_revisits, 
                                                               time_revisit, 
                                                               smalls_cannot_revisit)
                options = compute_next_step(step, paths_dict, big_caves,
                                            small_caves_visited2,
                                            small_caves_revisited2,
                                            num_revisits, time_revisit,
                                            smalls_cannot_revisit)
                for path in options:
                    output.append([step] + path)
        return output


print(find_paths("Dec12_data.txt"))
print(find_paths("Dec12_data.txt",1,1))