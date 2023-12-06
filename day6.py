import re
with open('data/my_input/6.in') as f:
    lines = f.read().split("\n")

def num_ways_of_win(distance,time):
    counter=0
    for i in range(1,time):
        range_travelled=i*(time-i)
        if range_travelled>distance:
            counter+=1
    return counter

def part1(vlines):
    times=list(map(int,re.findall(r"(\d+)", vlines[0])))
    distances=list(map(int,re.findall(r"(\d+)", vlines[1])))
    dict_times_distances={times[i]:distances[i] for i in range(len(times))}
    counter=1
    for time,distance in dict_times_distances.items():
        counter*=num_ways_of_win(distance,time)
    return counter


def part2(vlines):
    time=int("".join(re.findall(r"(\d+)", vlines[0])))
    distance=int("".join(re.findall(r"(\d+)", vlines[1])))
    return num_ways_of_win(distance,time)

print(part1(lines))
print(part2(lines))