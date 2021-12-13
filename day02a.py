#DecafMegalodon
#Advent of code day 02a submission

def read_input(filename="./inputs/day02.txt"):
    file = open(filename, "r")
    instructions = []
    for line in file.readlines():
        splitline = line.split()
        instructions.append({"direction": splitline[0], "magnitude": splitline[1]})
    
    file.close()
    return instructions
    
if __name__ == "__main__":
    read_input()