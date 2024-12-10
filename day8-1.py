with open ('day8_input.txt', 'r') as f:
    lines = [line.replace('\n','') for line in f]

frequencies = {}
for row in range(len(lines)):
    for char in range(len(lines[row])):
        if lines[row][char] == '.':
            continue
        if lines[row][char] in frequencies:
            frequencies[lines[row][char]].append([row,char])
        else:
            frequencies[lines[row][char]] = [[row,char]]

frequencies
