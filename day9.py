import re

with open('data/my_input/9.in') as f:
    lines = f.read().split("\n")

def compute_diff_numbers(numbers):
    # we compute value minue the previous one in a new list
    diff_numbers = []
    for i in range(1, len(numbers)):
        diff_numbers.append(int(numbers[i])-int(numbers[i-1]))
    return diff_numbers

        

def predict(line):
    # parse all numbers
    numbers = list(map(int,re.findall(r'-?\d+', line)))
    step_numbers = numbers
    list_numbers = [numbers[-1]]
    while any(step_numbers):
        step_numbers =compute_diff_numbers(step_numbers)
        if step_numbers:
            list_numbers.append(step_numbers[-1])
    return (sum(list_numbers))

def predict2(line):
    # parse all numbers
    numbers = list(map(int,re.findall(r'-?\d+', line)))
    step_numbers = numbers[::-1]
    list_numbers = [numbers[0]]
    while any(step_numbers):
        step_numbers =compute_diff_numbers(step_numbers)
        if step_numbers:
            list_numbers.append(step_numbers[-1])
    return (sum(list_numbers))



def part1(lines):
    counter = 0
    for line in lines:
        counter+=predict(line)
    return counter

def part2(lines):
    counter = 0
    for line in lines:
        counter+=predict2(line)
    return counter



print(part1(lines))
print(part2(lines))