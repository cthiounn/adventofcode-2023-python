import re
from math import gcd
from functools import reduce
with open('data/my_input/8.in') as f:
    lines = f.read().split("\n")


def move(starting_point, instruction, directions):
    left, right = directions[starting_point]
    if instruction == "L":
        return left
    elif instruction == "R":
        return right
    else:
        return starting_point

def part1(vlines):
    instructions= vlines[0]

    directions={}
    for line in vlines[2:]:
        start, left, right = (re.findall(r"\w+",line))
        directions[start]= (left, right)
    
    starting_point = "AAA"
    loop=0
    while starting_point != "ZZZ":
        for i,instruction in enumerate(instructions):
            starting_point= move(starting_point, instruction, directions)
            if starting_point == "ZZZ":
                return loop*len(instructions) + (i+1)
        loop+=1
    return 0


def all_ending_with_Z(starting_point):
    for point in starting_point:
        if not point.endswith("Z"):
            return False
    return True


def first_Z(starting_point,instructions,directions):
    loop=0
    while not starting_point.endswith("Z"):
        for i,instruction in enumerate(instructions):
            starting_point= move(starting_point, instruction, directions)
            if starting_point.endswith("Z"):
                return loop*len(instructions) + (i+1)
        loop+=1
    return 0


def part2(vlines):
    instructions= vlines[0]
    directions={}
    for line in vlines[2:]:
        start, left, right = (re.findall(r"\w+",line))
        directions[start]= (left, right)

    starting_point = set(map(lambda x : x if x.endswith("A") else None,directions.keys()))
    starting_point.remove(None)
    starting_point = list(starting_point)

    index_cycle=list()
    for start in starting_point:
        index_cycle.append(first_Z(start,instructions,directions))
    # calculate the LCM of the index_cycle
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    return reduce(lcm, index_cycle)



print(part1(lines))
print(part2(lines))