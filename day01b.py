#DecafMegalodon
#Advent of code day 01b submission

def read_input(filename="./inputs/day01.txt"):
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [int(i) for i in input]
    return input

def calc_sliding_sum(raw_input):
    pooled_input = [raw_input[index] + 
        raw_input[index + 1] + 
        raw_input[index + 2] 
        for index in range(len(raw_input) - 2)]
    return pooled_input

def count_deeper(input):
    current_depth = float('inf')  # set our initial depth to infinity so the first measurement is always less
    deeper_count = 0
    for new_depth in input:
        if new_depth > current_depth:
            deeper_count += 1
        current_depth = new_depth
    return deeper_count
    
if __name__ == "__main__":
    input = read_input()
    pooled_input = calc_sliding_sum(input)
    print(count_deeper(pooled_input))