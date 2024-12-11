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
mid_points = {}
for signal in frequencies:
    print(frequencies[signal])
    for i in range(len(frequencies[signal])-1):
        for j in range(i+1,len(frequencies[signal])):
            print(i,j)
            print(frequencies[signal][i][0])
            print(frequencies[signal][j][0])
            print(frequencies[signal][i][1])
            print(frequencies[signal][j][1])
            mid_points[signal].append([(frequencies[signal][i][0]+frequencies[signal][j][0])//2,(frequencies[signal][i][1]+frequencies[signal][j][1])//2])
