import re

with open('data/my_input/4.in') as f:
    lines = f.read().split("\n")

def part1(vlines):
    counter=0
    for line in vlines:
        winning,has=line.split("|")
        winning=set(re.findall(r"(\d+)",winning)[1:])
        has=set(re.findall(r"(\d+)",has))
        print(winning&has)
        if len(winning&has)>=1:
            counter+=2**(len(winning&has)-1)
    return counter


def part2(vlines):
    counter=0
    return counter

print(part1(lines))
print(part2(lines))