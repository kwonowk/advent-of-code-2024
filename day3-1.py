# Open file
f = open('day3_input.txt', 'r')

# Read and store instruction
instructions = ""
for x in f:
    instructions += x

# Extract numbers from "mul(*,*)"" format
import re
muls = r'mul\((\d+),(\d+)\)'
matches = re.findall(muls,instructions)

# Multiply the extracted results
results = sum([int(a) * int(b) for a, b in matches])
print(results)
