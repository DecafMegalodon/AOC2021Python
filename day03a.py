#DecafMegalodon
#Advent of code day 03a submission
#Our goal today is find the most common bit in each column of the input,
#As well as the complement of the most common bits

def read_input(filename="./inputs/day01.txt"):
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    return input