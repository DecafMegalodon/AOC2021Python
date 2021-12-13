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
    aim = 0
    
    submarine_movements={
        "forward": lambda instr_mag, cur_d, cur_h, cur_a: (cur_d + instr_mag * cur_a, cur_h + instr_mag, cur_a),
        "back": lambda instr_mag, cur_d, cur_h, cur_a:  (cur_d - instr_mag * cur_a, cur_h - instr_mag, cur_a),
        "up": lambda instr_mag, cur_d, cur_h, cur_a:  (cur_d, cur_h, cur_a - instr_mag),
        "down": lambda instr_mag, cur_d, cur_h, cur_a: (cur_d, cur_h, cur_a + instr_mag)
    }
    
    for instruction in instructions:
        direction, magnitude = instruction["direction"], instruction["magnitude"]
        depth, horizontal, aim = submarine_movements[direction](magnitude, depth, horizontal, aim)

    return depth * horizontal
    
if __name__ == "__main__":
    input = read_input()
    print(simulate_submarine(input))