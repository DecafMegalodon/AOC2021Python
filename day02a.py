#DecafMegalodon
#Advent of code day 02a submission

def read_input(filename="./inputs/day02.txt"):
    file = open(filename, "r")
    instructions = []
    for line in file.readlines():
        splitline = line.split()
        instructions.append({"direction": splitline[0], "magnitude": int(splitline[1])})
    
    file.close()
    return instructions

def simulate_submarine(instructions):
    depth = 0
    horizontal = 0
    
    submarine_movements={
        "forward": lambda instr_mag, cur_d, cur_h: (cur_d, cur_h + instr_mag),
        "back": lambda instr_mag, cur_d, cur_h:  (cur_d, cur_h - instr_mag),
        "up": lambda instr_mag, cur_d, cur_h:  (cur_d - instr_mag, cur_h),
        "down": lambda instr_mag, cur_d, cur_h: (cur_d + instr_mag, cur_h)
    }
    
    for instruction in instructions:
        direction, magnitude = instruction["direction"], instruction["magnitude"]
        depth, horizontal = submarine_movements[direction](magnitude, depth, horizontal)

    return depth * horizontal
    
if __name__ == "__main__":
    input = read_input()
    print(simulate_submarine(input))