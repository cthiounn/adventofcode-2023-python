import re
from collections import deque
with open('data/my_input/10.in') as f:
    lines = f.read().split("\n")

DICT = {"|": "NS", "-": "WE", "L": "NE", "J": "NW", "7": "SW", "F": "SE", ".": "", "S": "NSWE"}

def get_neighbors(current, data):
    neighbors = []
    check_east = (current[0], current[1]+1)
    check_west = (current[0], current[1]-1)
    check_north = (current[0]-1, current[1])
    check_south = (current[0]+1, current[1])
    symbol = DICT[data[current]]
    if "N" in symbol and check_north in data and data[check_north] != "." and "S" in DICT[data[check_north]]:
        neighbors.append(check_north)
    if "S" in symbol and check_south in data and data[check_south] != "." and "N" in DICT[data[check_south]]:
        neighbors.append(check_south)
    if "W" in symbol and check_west in data and data[check_west] != "." and "E" in DICT[data[check_west]]:
        neighbors.append(check_west)
    if "E" in symbol and check_east in data and data[check_east] != "." and "W" in DICT[data[check_east]]:
        neighbors.append(check_east)
    return neighbors

def part1(lines):
    # parse lines to dict
    data = {(i,j): lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}
    starting_point = [(i,j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == "S"][0]
    seen = set()
    seen.add(starting_point)
    queue = deque()
    queue.append(starting_point)
    dict_distance = {starting_point: 0}
    while queue:
        current = queue.popleft()
        for neighbor in get_neighbors(current, data):
            if neighbor not in seen:
                queue.append(neighbor)
                seen.add(neighbor)
            dict_distance[neighbor] = dict_distance[current] + 1 if neighbor not in dict_distance else min(dict_distance[current] + 1, dict_distance[neighbor])
            
    return max(dict_distance.values())
    
def get_point_neighbors(current, data):
    neighbors = []
    check_east = (current[0], current[1]+1)
    check_west = (current[0], current[1]-1)
    check_north = (current[0]-1, current[1])
    check_south = (current[0]+1, current[1])
    if check_north in data and data[check_north] == ".":
        neighbors.append(check_north)
    if check_south in data and data[check_south] == ".":
        neighbors.append(check_south)
    if check_west in data and data[check_west] == ".":
        neighbors.append(check_west)
    if check_east in data and data[check_east] == ".":
        neighbors.append(check_east)
    return neighbors

def parity(i,j,data):
    increment = 1
    string=""
    while (i,j-increment) in data :
        string = data[(i,j-increment)]+string
        increment += 1
    counter =(re.sub("(L-*J|F-*7)","||",re.sub("(L-*7|F-*J)","|",string)).count("|"))
    return counter % 2

def part2(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
           print(lines[i][j], end="")
        print()
    # parse lines to dict
    data = {(i,j): lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}
    starting_point = [(i,j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == "S"][0]
    seen = set()
    seen.add(starting_point)
    queue = deque()
    queue.append(starting_point)
    dict_distance = {starting_point: 0}
    while queue:
        current = queue.popleft()
        for neighbor in get_neighbors(current, data):
            if neighbor not in seen:
                queue.append(neighbor)
                seen.add(neighbor)
            dict_distance[neighbor] = dict_distance[current] + 1 if neighbor not in dict_distance else min(dict_distance[current] + 1, dict_distance[neighbor])
    
    # Specific data input
    data[starting_point] = "|"

    new_data = { (i,j): data[(i,j)] for i in range(len(lines)) for j in range(len(lines[i])) if (i,j) in seen}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
           if (i,j) not in seen:
               new_data[(i,j)] = "."
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            
            if new_data[(i,j)] == "." and  parity(i,j,new_data) == 1:
                print("@", end="")
            else:
                print(new_data[(i,j)], end="")
        print()

    return sum([1 for i in range(len(lines)) for j in range(len(lines[i])) if new_data[(i,j)] == "." and parity(i,j,new_data) == 1 ])



print(part1(lines))
print(part2(lines))