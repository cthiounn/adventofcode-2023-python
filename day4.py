import re
from collections import defaultdict
with open('data/my_input/4.in') as f:
    lines = f.read().split("\n")

def part1(vlines):
    counter=0
    for line in vlines:
        winning,has=line.split("|")
        winning=set(re.findall(r"(\d+)",winning)[1:])
        has=set(re.findall(r"(\d+)",has))
        if len(winning&has)>=1:
            counter+=2**(len(winning&has)-1)
    return counter


def part2(vlines):
    dic=defaultdict(int)
    for line in vlines:
        winning,has=line.split("|")
        num_card=re.findall(r"(\d+)",winning)[0]
        dic[num_card]+=1
        winning=set(re.findall(r"(\d+)",winning)[1:])
        has=set(re.findall(r"(\d+)",has))
        if len(winning&has)>=1:
            for i in range(1,len(winning&has)+1):
                dic[str(int(num_card)+i)]+=dic[num_card]
    return sum(dic.values())

print(part1(lines))
print(part2(lines))