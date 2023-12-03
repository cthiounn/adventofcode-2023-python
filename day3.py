import re
from collections import deque

with open('data/my_input/3.in') as f:
    lines = f.read().split("\n")

def return_list_numbers_from_dict(d):
    list_numbers=[]
    for (i,j) in d.keys():
        if (i,j-1) in d:
            continue
        else:
            number=d[(i,j)]
            incr=1
            while (i,j+incr) in d:
                number+=d[(i,j+incr)]
                incr+=1
            list_numbers.append(int(number))
    return list_numbers

def part1(vlines):
    datadicnum={(i,j):s for i,line in enumerate(vlines) for j,s in enumerate(line) if s!="." and s.isdigit()}
    datadicchar={(i,j):s for i,line in enumerate(vlines) for j,s in enumerate(line) if s!="." and not s.isdigit()}
    
    list_starting_position= list(datadicchar.keys())
    set_of_touche=set()
    for (x,y)  in list_starting_position:
        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx==dy==0:
                    continue
                if (x+dx,y+dy) in datadicnum:
                    set_of_touche.add((x+dx,y+dy))
    new_set_of_touche=set()
    touche_size=len(set_of_touche)
    new_touche_size=len(new_set_of_touche)
    while touche_size!=new_touche_size:
        new_set_of_touche=set()
        for (x,y)  in set_of_touche:
            for dy in range(-1,2):
                if (x,y+dy) in datadicnum:
                    new_set_of_touche.add((x,y+dy))

        
        touche_size=len(set_of_touche)
        new_touche_size=len(new_set_of_touche)
        set_of_touche=new_set_of_touche
            
    
    datadicvalidnum={(i,j):s for i,line in enumerate(vlines) for j,s in enumerate(line) if s!="." and s.isdigit() and (i,j) in set_of_touche}
    
    
    
    return sum(return_list_numbers_from_dict(datadicvalidnum))

def read_number(pos,d):
    i,j=pos
    inc=0
    while (i,j+inc) in d:
        inc-=1
        if (i,j+inc) not in d:
            j=j+inc+1
            break
    number=d[(i,j)]
    incr=1
    while (i,j+incr) in d:
        number+=d[(i,j+incr)]
        incr+=1
    return int(number)

def read_numbers_and_multiply(gear,datadicnum):
    pos1,pos2=gear
    return read_number(pos1,datadicnum)*read_number(pos2,datadicnum)

def leftest_number(pos,d):
    i,j=pos
    inc=0
    while (i,j+inc) in d:
        inc-=1
        if (i,j+inc) not in d:
            j=j+inc+1
            break
    return (i,j)

def part2(vlines):
    datadicnum={(i,j):s for i,line in enumerate(vlines) for j,s in enumerate(line) if s!="." and s.isdigit()}
    datadicchar={(i,j):s for i,line in enumerate(vlines) for j,s in enumerate(line) if s=="*"}
    counter=0
    list_starting_position= list(datadicchar.keys())
    set_of_touche=set()
    for (x,y)  in list_starting_position:
        gear=[]
        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx==dy==0:
                    continue
                if (x+dx,y+dy) in datadicnum:
                    gear.append((x+dx,y+dy))
        gear=list(set(list(map(lambda x : leftest_number(x,datadicnum),gear))))             
        if len(gear)==2:
            counter+=read_numbers_and_multiply(gear,datadicnum)
    return counter

print(part1(lines))
print(part2(lines))