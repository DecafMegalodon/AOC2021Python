#DecafMegalodon
#Advent of code day 01 a submission

def read_input(filename="./inputs/day01.txt"):
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [i.strip() for i in input]
    return input

read_input()