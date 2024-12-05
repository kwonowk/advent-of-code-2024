# Load the text and save lines as a list
f = open('day4_input.txt', 'r')

lines = []
for x in f:
    lines.append(x)
lines = [line.replace('\n','')for line in lines] # Remove line break at the end of lists

y = len(lines)      # 140 lines
x = len(lines[0])   # each with 140 characters

count = 0

# Horizontal & Backward combination
for line in lines:
    for e in range(x-3):
        if line[e]+line[e+1]+line[e+2]+line[e+3] in ("XMAS","SAMX"):
            count+=1

# Vertical top-down & bottom-up
for l in range(y-3):
    for i in range(x):
        if lines[l][i] + lines[l+1][i] + lines[l+2][i] + lines[l+3][i] in ("XMAS", "SAMX"):
            count += 1

# Diagonal left-right
for l in range(y-3):
    for e in range(x-3):
        if lines[l][e]+lines[l+1][e+1]+lines[l+2][e+2]+lines[l+3][e+3] in ("XMAS", "SAMX"):
            count +=1

# Diagonal right-left
for l in range(y-3):
    for e in range(3,x):
        if lines[l][e]+lines[l+1][e-1]+lines[l+2][e-2]+lines[l+3][e-3] in ("XMAS", "SAMX"):
            count +=1

print(count)
