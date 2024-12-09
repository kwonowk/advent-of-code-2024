# Read the input
with open ('day7_input.txt', 'r') as f:
    lines = [list(map(int, line.replace(':','').split())) for line in f]

true_vals = []  # To store true values

for line in lines:
    numbers = line[1:]
    loop_vals = [line[0]]   # To store results of reverse calculation
    print(line)
    # Reversee calculation, from right to left to check whether one of the last remaining value is the same as the first value of the list
    for num in reversed(line[2:]):
        temp = []
        for l in loop_vals:
            # If remainder is not 0, only subtraction is possible. If 0, two possiblities still stand
            if l % num == 0:
                temp.append(l / num)
                temp.append(l - num)
            else:
                temp.append(l - num)
        loop_vals = temp
    for v in loop_vals:
        if v == line[1]:
            print(line)
            true_vals.append(line[0])
            break

print(sum(true_vals))
