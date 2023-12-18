import re
from copy import deepcopy

with open('data/my_input/14.in') as f:
    lines = f.read().split("\n")

def move_possible_north(i,j,dictmap):
    if (i-1,j) in dictmap:
        if dictmap[(i-1,j)]=="#" or dictmap[(i-1,j)]=="O":
            return False
    elif (i-1,j) not in dictmap:
        return False
    return True

def move_north(i,j,dictmap):
    if dictmap[(i,j)]=="O":
        if move_possible_north(i,j,dictmap):
            dictmap[(i-1,j)]="O"
            dictmap[(i,j)]="."
            if (i-1,j) in dictmap :
                move_north(i-1,j,dictmap)

def count(dictmap):
    counter=0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if dictmap[(i,j)]=="O":
                counter+=(len(lines)-i)
    return counter

def print_map(dictmap):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            print(dictmap[(i,j)],end="")
        print()

def part1(lines):
    dictmap={(i,j):lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if dictmap[(i,j)]=="O":
                move_north(i,j,dictmap)
    return count(dictmap)


def dictmap_to_string(dictmap):
    return "".join([dictmap[(i,j)] for i in range(len(lines)) for j in range(len(lines[i]))])


def rotate_map_90_anticlockwise(dictmap):
    new_dictmap={}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            new_dictmap[(j,len(lines)-1-i)]=dictmap[(i,j)]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            dictmap[(i,j)]=new_dictmap[(i,j)]

def do_a_cycle(dictmap):
    for _ in range(4):
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if dictmap[(i,j)]=="O":
                    move_north(i,j,dictmap)
        rotate_map_90_anticlockwise(dictmap)
                
            

def part2(lines):
    dictmap={(i,j):lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}

    seen=set()
    dict_hash={}
    repeated=set()
    start_indice_cycle=None
    for cycle in range(1000):
        do_a_cycle(dictmap)

        hash_dictmap=dictmap_to_string(dictmap)
        if hash_dictmap not in seen:
            seen.add(hash_dictmap)
            dict_hash[hash_dictmap]=cycle
        else:
            if start_indice_cycle is None:
                start_indice_cycle=cycle
            if dict_hash[hash_dictmap] not in repeated:
                repeated.add(dict_hash[hash_dictmap])
            else:
                end_indice_cycle=dict_hash[hash_dictmap]
    #print(repeated)
    #print(start_indice_cycle,end_indice_cycle)

    cycle_to_go=1000000000-1000
    cycle_to_go=cycle_to_go%(len(repeated))

    for _ in range(cycle_to_go):
        do_a_cycle(dictmap)
    return count(dictmap)

print(part1(lines))
print(part2(lines))