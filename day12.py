import re
from functools import cache

with open('data/my_input/12.in') as f:
    lines = f.read().split("\n")


def check_valid_springs_config(springs, numbers):
    if "?" in springs:
        return False
    numbers_checked=(list(map(lambda x: x.count("#"),springs.split("."))))
    new_numbers_checked=list()
    for number in numbers_checked:
        if number !=0:
            new_numbers_checked.append(number)
    return new_numbers_checked==numbers


def generate_all_springs_config(springs):
    list_of_springs=list()
    for i in range(len(springs)):
        if springs[i]=="?":
            return generate_all_springs_config(springs[:i]+"#"+springs[i+1:])+generate_all_springs_config(springs[:i]+"."+springs[i+1:])
    list_of_springs.append(springs)
    return list_of_springs

def part1(lines):
    counter=0
    for line in lines:
        numbers = list(map(int,re.findall(r"-?\d+", line)))
        springs=line.split(" ")[0]
        counter+=sum([1 for config in generate_all_springs_config(springs) if check_valid_springs_config(config,numbers)])
    return counter

@cache
def num_valid(springs, numbers):
    if "#" not in numbers:
        regex="(\?|#){numbers}".replace("numbers",numbers)
        if re.search(regex, springs) :
            return 1
    else:
        number,*others=numbers.split("#")
        others="#".join(others)
        regex="(\?|#){number}(\.|\?)".replace("number",number)
        match=re.search(regex, springs)
        if match:
            start, end =match.span()
            if "#" in springs[:start] :
                return 0
            else: 
                return num_valid(springs[end:],others) + num_valid(springs[start+1:],numbers)
    return 0


def part2(lines):
    counter=0
    for i,line in enumerate(lines):
        if i !=20:
            numbers = "#".join(5*re.findall(r"-?\d+", line))
            spring=line.split(" ")[0]
            springs=spring+4*("?"+spring)
            #counter+=num_valid(springs,numbers)
            print(num_valid(springs,numbers),springs,numbers)
    return counter

#print(part1(lines))
print(part2(lines))