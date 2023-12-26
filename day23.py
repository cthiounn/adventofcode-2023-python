import re
from collections import deque

with open('data/my_input/23.in') as f:
    lines = f.read().split("\n")
    dictmap={(i,j):lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}


def can_move(start, end, dictmap):
    x,y=start
    xx,yy=end
    movable=False
    if end not in dictmap:
        pass
    elif dictmap[end] == '#':
        pass
    elif dictmap[end] == 'v' and x-xx==1:
        pass
    elif dictmap[end] == '^' and xx-x==1:
        pass
    elif dictmap[end] == '>' and y-yy==1:
        pass
    elif dictmap[end] == '<' and yy-y==1:
        pass
    else:
        movable=True
    return movable

def return_a_list_of_possible_moves(start, dictmap):
    x,y=start
    possible_moves=[]
    if can_move(start, (x+1,y), dictmap):
        possible_moves.append((x+1,y))
    if can_move(start, (x-1,y), dictmap):
        possible_moves.append((x-1,y))
    if can_move(start, (x,y+1), dictmap):
        possible_moves.append((x,y+1))
    if can_move(start, (x,y-1), dictmap):
        possible_moves.append((x,y-1))
    return possible_moves

def part1(dictmap):
    start = (0,1)
    q = deque()
    q.append((start, set()))
    all_distances = []
    max_distance = 0
    while q:
        current,  visited = q.popleft()
        distance = len(visited)
        if distance > max_distance:
            max_distance = distance
        if current in visited:
            continue
        next_moves = return_a_list_of_possible_moves(current, dictmap)
        if next_moves:
            for next_pos in next_moves:
                new_visited = set()
                new_visited=new_visited.union(visited)
                new_visited.add(current)
                if next_pos not in new_visited:
                    q.append((next_pos,new_visited))
    return max_distance

def part2():
    with open('data/my_input/23.in') as f:
        lines = f.read().replace('^', '.').replace('v', '.').replace('<', '.').replace('>', '.').split("\n")
    dictmap={(i,j):lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}
    return part1(dictmap)

print(part1(dictmap))
#print(part2())