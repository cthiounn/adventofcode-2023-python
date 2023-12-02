import re
with open('data/my_input/2.in') as f:
    lines = f.read().split("\n")


def impossible(line):
    data=(line.split(":")[1].split(";"))

    for d in data :

        list_green= re.findall(r"(\d+) green",d)
        list_red= re.findall(r"(\d+) red",d)
        list_blue= re.findall(r"(\d+) blue",d)
        num_green = int(list_green[0]) if list_green else 0
        num_red = int(list_red[0]) if list_red else 0
        num_blue = int(list_blue[0]) if list_blue else 0

        if num_green > 13 or num_red > 12 or num_blue > 14:
            return True
    return False



def power(line):
    data=(line.split(":")[1].split(";"))
    max_green,max_red,max_blue=0,0,0
    for d in data :

        list_green= re.findall(r"(\d+) green",d)
        list_red= re.findall(r"(\d+) red",d)
        list_blue= re.findall(r"(\d+) blue",d)
        num_green = int(list_green[0]) if list_green else 0
        num_red = int(list_red[0]) if list_red else 0
        num_blue = int(list_blue[0]) if list_blue else 0
        max_green=max(num_green,max_green)
        max_red=max(num_red,max_red)
        max_blue=max(num_blue,max_blue)

    return max_green*max_red*max_blue

def part1(vlines):
    counter=0
    for line in vlines:
        game_id=re.findall(r"\d+",line)[0]
        if not impossible(line):
            counter+=int(game_id)
    
    return counter


def part2(vlines):
    counter=0
    for line in vlines:
        game_id=re.findall(r"\d+",line)[0]
        counter+=power(line)
    
    return counter

print(part1(lines))
print(part2(lines))