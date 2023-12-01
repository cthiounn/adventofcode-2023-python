import re
with open('data/my_input/1.in') as f:
    lines = f.read().split("\n")

def concat(l):
    return l[0]+l[-1]

DIGITS={"one":"1e","two":"2o","three":"3e","four":"4r", "five":"5e", "six":"6x", "seven":"7n", "eight":"8t", "nine":"9e"}

def string_to_digits(s):
    for word, digit in DIGITS.items():
        s = s.replace(word, digit)
    return s

def replace_digits(s):
    ss=""
    for char in s:
        ss=string_to_digits(ss+char)
    return string_to_digits(ss)

def part1(vlines):
    return sum(map(lambda x : int(concat(re.findall(r"\d",x))),vlines))


def part2(vlines):
    vlines2=list(map(replace_digits,vlines))
    return sum(map(lambda x : int(concat(re.findall(r"\d",x))),vlines2))

print(part1(lines))
print(part2(lines))