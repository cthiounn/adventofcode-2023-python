import re
from copy import deepcopy

with open('data/my_input/13.in') as f:
    lines = f.read().split("\n\n")



def transpose_input(lines):
    return list(map(list, zip(*lines)))

def split_lines_into_two_part_from_indice(lines,indice):
    return lines[:indice+1][::-1],lines[indice+1:]


def find_symetric(lines):
    for i in range(0,len(lines)-1):
        if lines[i] == lines[i+1]:
            a,b = split_lines_into_two_part_from_indice(lines,i)
            size_a,size_b = len(a),len(b)
            min_size = min(size_a,size_b)
            if a[0:min_size] == b[0:min_size]:
                return i
            
    else:
        return -1

def find_all_symetric(lines):
    list_symetric=[]
    for i in range(0,len(lines)-1):
        if lines[i] == lines[i+1]:
            a,b = split_lines_into_two_part_from_indice(lines,i)
            size_a,size_b = len(a),len(b)
            min_size = min(size_a,size_b)
            if a[0:min_size] == b[0:min_size]:
                list_symetric.append(i)
    return list_symetric

def part1(lines):
    counter=0
    for puzzle in lines:
        
        lines_puzzle = puzzle.strip("\n").split("\n")
        
        counter += (find_symetric(lines_puzzle)+1 )*100
        counter += (find_symetric(transpose_input(lines_puzzle))+1)

    return counter

def part2(lines):
    counter=0
    for puzzle in lines:
        
        lines_puzzle = puzzle.strip("\n").split("\n")
        found=False

        num_rows_old,num_cols_old=find_symetric(lines_puzzle)+1,find_symetric(transpose_input(lines_puzzle))+1
        for i in range(0,len(lines_puzzle)):
            for j in range(0,len(lines_puzzle[i])):
                if not found:
                    newlinespuzzle = deepcopy(lines_puzzle)
                    if lines_puzzle[i][j]==".":
                        newlinespuzzle[i]=newlinespuzzle[i][:j] + "#" + newlinespuzzle[i][j+1:]
                    else:
                        newlinespuzzle[i]=newlinespuzzle[i][:j] + "." + newlinespuzzle[i][j+1:]
            
                    num_rows=find_all_symetric(newlinespuzzle)
                    num_cols=find_all_symetric(transpose_input(newlinespuzzle))
                    if (num_rows_old-1) in num_rows:
                        num_rows.remove(num_rows_old-1)
                    if (num_cols_old-1) in num_cols:
                        num_cols.remove(num_cols_old-1)

                    if not num_rows and not num_cols:
                        pass
                    elif num_rows:
                        counter += (num_rows[0]+1)*100
                        found=True
                    elif num_cols:
                        counter += (num_cols[0]+1)
                        found=True
    return counter

print(part1(lines))
print(part2(lines))