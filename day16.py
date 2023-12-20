import re
from collections import deque

with open('data/my_input/16.in') as f:
    lines = f.read().split("\n")

LRUD={"L":(0,-1),"R":(0,1),"U":(-1,0),"D":(1,0)}

def append_to_queue_if_not_seen(queue,seen,position):
    if position not in seen:
        queue.append(position)
        seen.add(position)
    return queue,seen

def printmap(dictmap):
    max_x=max(map(lambda x:x[0],dictmap.keys()))
    max_y=max(map(lambda x:x[1],dictmap.keys()))
    for i in range(max_x+1):
        for j in range(max_y+1):
            print(dictmap[(i,j)],end="")
        print()

def calculate_light(lines,start,starting_direction):
    dictmap={(i,j):lines[i][j] for i in range(len(lines)) for j in range(len(lines[i]))}
    
    queue=deque()
    queue.append((start,starting_direction))
    seen=set()
    while queue:
        current=queue.popleft()
        pos,direction=current
        x,y=pos
        next_pos=(x+LRUD[direction][0],y+LRUD[direction][1])
        other_direction=None
        if next_pos in dictmap:
            if dictmap[next_pos]==".":
                new_direction=direction
            elif dictmap[next_pos]=="|":
                if direction=="R" or direction=="L":
                    new_direction="D"
                    other_direction="U"
                else:
                    new_direction=direction
            elif dictmap[next_pos]=="-":
                if direction=="R" or direction=="L":
                    new_direction=direction
                else:
                    new_direction="R"
                    other_direction="L"
            elif dictmap[next_pos]=="\\":
                if direction=="R":
                    new_direction="D"
                elif direction=="L":
                    new_direction="U"
                elif direction=="U":
                    new_direction="L"
                elif direction=="D":
                    new_direction="R"
            elif dictmap[next_pos]=="/":
                if direction=="R":
                    new_direction="U"
                elif direction=="L":
                    new_direction="D"
                elif direction=="U":
                    new_direction="R"
                elif direction=="D":
                    new_direction="L"
            queue,seen=append_to_queue_if_not_seen(queue,seen,(next_pos,new_direction))
            if other_direction:
                queue,seen=append_to_queue_if_not_seen(queue,seen,(next_pos,other_direction))
    list_of_seen=set(map(lambda x:x[0],seen))
    new_dict={k:('#' if k in list_of_seen else ".") for k,v in dictmap.items()}
    #printmap(new_dict)
    return len(list_of_seen)


def part1(lines):
    start=(0,-1)
    starting_direction="R"
    return calculate_light(lines,start,starting_direction)

def part2(lines):
    list_of_starting_positions=[]
    for i in range(len(lines)):
        list_of_starting_positions.append(((i,-1),"R"))
        list_of_starting_positions.append(((i,len(lines[0])),"L"))
    for j in range(len(lines[0])):
        list_of_starting_positions.append(((-1,j),"D"))
        list_of_starting_positions.append(((len(lines),j),"U"))
    return max(map(lambda x:calculate_light(lines,x[0],x[1]),list_of_starting_positions))

print(part1(lines))
print(part2(lines))