import re

with open('data/my_input/15.in') as f:
    lines = f.read().split("\n")

# Compute Hash from a string
def hash(s):
    current_hash=0
    for i in range(len(s)):
        current_hash+=ord(s[i])
        current_hash*=17
        current_hash%=256
    return current_hash


def part1(lines):
    return sum([hash(line) for line in lines[0].split(",")])


def part2(lines):
    counter=0
    return counter

print(part1(lines))
print(part2(lines))