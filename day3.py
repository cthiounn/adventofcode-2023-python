with open('data/my_input/3.in') as f:
    lines = f.read().split("\n")

def leftest_number(pos,d):
    i,j=pos
    inc=0
    while (i,j+inc) in d:
        inc-=1
        if (i,j+inc) not in d:
            j=j+inc+1
            break
    return (i,j)

def read_number(pos,d):
    i,j=leftest_number(pos,d)
    number=d[(i,j)]
    incr=1
    while (i,j+incr) in d:
        number+=d[(i,j+incr)]
        incr+=1
    return int(number)

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
    all_numbers=set(map(lambda x: leftest_number(x,datadicnum),set_of_touche))
    return sum(map(lambda x : read_number(x,datadicnum),all_numbers))



def read_numbers_and_multiply(gear,datadicnum):
    pos1,pos2=gear
    return read_number(pos1,datadicnum)*read_number(pos2,datadicnum)

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