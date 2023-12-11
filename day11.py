import re
from collections import Counter
from itertools import combinations
from collections import deque

with open('data/my_input/11.in') as f:
    lines = f.read().split("\n")

def detected_empty_lines(lines):
    list_of_empty_lines=[]
    for i in range(len(lines)):
        if  "." in lines[i] and len(Counter(lines[i]))==1:
            list_of_empty_lines.append(i)
    return list_of_empty_lines

def detected_empty_columns(dict_map_galaxy):
    list_of_empty_columns=[]
    for i in range(len(lines[0])):
        if "." in [dict_map_galaxy[(j,i)] for j in range(len(lines))] and len(Counter([dict_map_galaxy[(j,i)] for j in range(len(lines))]))==1:
            list_of_empty_columns.append(i)
    return list_of_empty_columns

def distance_between_galaxies(galaxy_item1, galaxy_item2, dict_map_galaxy_dist):
    # A star algorithm
    
    starting_point=galaxy_item1
    ending_point=galaxy_item2
    deque_of_points=deque()
    deque_of_points.append(starting_point)
    visited_points=[]
    dict_of_points={}
    dict_of_points[starting_point]=0
    while len(deque_of_points)>0:
        current_point=deque_of_points.popleft()
        if current_point==ending_point:
            return dict_of_points[current_point]
        visited_points.append(current_point)
        for i in range(-1,2):
            for j in range(-1,2):
                if i==0 and j==0:
                    continue
                if abs(i)+abs(j)>1:
                    continue
                new_point=(current_point[0]+i, current_point[1]+j)
                if new_point[0] in range(len(lines)) and new_point[1] in range(len(lines[0])) and new_point not in visited_points and dict_map_galaxy_dist[new_point]>0:
                    if new_point not in dict_of_points.keys():
                        dict_of_points[new_point]=dict_of_points[current_point]+dict_map_galaxy_dist[new_point]
                    else:
                        dict_of_points[new_point]=min(dict_of_points[new_point], dict_of_points[current_point]+dict_map_galaxy_dist[new_point])
                    deque_of_points.append(new_point)
                    if new_point==ending_point:
                        return dict_of_points[new_point]

def taxy_cab_distance(galaxy_item1, galaxy_item2):
    return abs(galaxy_item1[0]-galaxy_item2[0])+abs(galaxy_item1[1]-galaxy_item2[1])

def part1(lines):
    dict_map_galaxy = {(i,j):lines[i][j] for i in range(len(lines)) for j in range(len(lines[0]))}
    list_of_empty_lines=detected_empty_lines(lines)
    list_of_empty_columns=detected_empty_columns(dict_map_galaxy)
    
    all_lines=[]
    for i in range(len(lines)):
        string=""
        for j in range(len(lines[0])):
            if j in list_of_empty_columns:
                string+="."
            string+=lines[i][j]
        if i in list_of_empty_lines:
            all_lines.append(string)
        all_lines.append(string)
    
    dict_map_galaxy_item = {(i,j):all_lines[i][j] for i in range(len(all_lines)) for j in range(len(all_lines[0])) if all_lines[i][j]=="#"}
    dist=0
    for galaxy_item1, galaxy_item2 in combinations(dict_map_galaxy_item.keys(),2):
        dist+=taxy_cab_distance(galaxy_item1, galaxy_item2)
        
    

    return dist

def num_empty_lines_in_between(galaxy_item1, galaxy_item2, list_of_empty_lines):
    if galaxy_item1>galaxy_item2:
        galaxy_item1, galaxy_item2=galaxy_item2, galaxy_item1
    if galaxy_item1==galaxy_item2:
        return 0
    num_empty_lines=0
    for i in range(galaxy_item1+1, galaxy_item2):
        if i in list_of_empty_lines:
            num_empty_lines+=1
    return num_empty_lines

def taxy_cab_distance2(galaxy_item1, galaxy_item2, list_of_empty_lines, list_of_empty_columns):
    normal_distance = taxy_cab_distance(galaxy_item1, galaxy_item2)
    x,y=galaxy_item1
    x2,y2=galaxy_item2
    num_empty= num_empty_lines_in_between(x, x2, list_of_empty_lines) + num_empty_lines_in_between(y, y2, list_of_empty_columns) 
    return normal_distance + (1000000-1)*num_empty 

def part2(lines):
    dict_map_galaxy = {(i,j):lines[i][j] for i in range(len(lines)) for j in range(len(lines[0]))}
    list_of_empty_lines=detected_empty_lines(lines)
    list_of_empty_columns=detected_empty_columns(dict_map_galaxy)
    
    
    dict_map_galaxy_item = {(i,j):lines[i][j] for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j]=="#"}
    dist=0
    for galaxy_item1, galaxy_item2 in combinations(dict_map_galaxy_item.keys(),2):
        dist+=taxy_cab_distance2(galaxy_item1, galaxy_item2,list_of_empty_lines, list_of_empty_columns)
    return dist

print(part1(lines))
print(part2(lines))