import numpy as np
np.set_printoptions(edgeitems=30, linewidth = 1000000)

# Read file and save the map as an array
with open ('day6_input.txt', 'r') as f:
    lines = [list(line.strip()) for line in f]
map = np.array(lines)

# Define map boundary and inital location
boundary = map.shape[0]
init_loc = np.where(map == '^')
y, x = init_loc[0][0], init_loc[1][0]

# Gruard route
while (0 <= x < boundary) and (0 <= y < boundary):
    if np.isin(map, '^').any(): # Go upward
        y = np.where(map == '^')[0][0]
        x = np.where(map == '^')[1][0]
        if (y-1)>=0:
            if map[y-1, x] != '#':
                map[y-1, x] = '^'
                map[y, x] = 'X'
                y, x = y-1, x
            else :
                map[y, x] = '>' # Right turn
        elif (y-1) < 0:
            map[y, x] = 'X'
            break


    elif np.isin(map, '>').any(): # Go rightward
        y = np.where(map == '>')[0][0]
        x = np.where(map == '>')[1][0]
        if (x+1) < boundary:
            if map[y, x+1] != '#':
                map[y, x+1] = '>'
                map[y, x] = 'X'
                y, x = y, x+1
            else :
                map[y, x] = 'v' # Right turn
        elif (x+1) == boundary:
            map[y, x] = 'X'
            break


    elif np.isin(map, 'v').any(): # Go down
        y = np.where(map == 'v')[0][0]
        x = np.where(map == 'v')[1][0]
        if (y+1) < boundary :
            if map[y+1, x] != '#':
                map[y+1, x] = 'v'
                map[y, x] = 'X'
                y, x = y+1, x
            else :
                map[y, x] = '<' # Right turn
        elif (y+1) == boundary:
            map[y,x] = 'X'
            break


    elif np.isin(map, '<').any(): # Go leftward
        y = np.where(map == '<')[0][0]
        x = np.where(map == '<')[1][0]
        if (x-1) >= 0 :
            if map[y, x-1] != '#':
                map[y, x-1] = '<'
                map[y, x] = 'X'
                y, x = y, x-1
            else :
                map[y, x] = '^' # Right turn
        elif (x-1) < 0:
            map[y,x] = 'X'
            break

print(map)
print(sum(sum(map == 'X')))
