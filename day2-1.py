level_result = [] # Store results

def level_checker(row):
    # Difference between the first and the last value to identify increase/decrease
    if row[0]-row[-1] > 0: # Decrease
        for i, j in zip(row[:-1], row[1:]):
            if (i-j <= 0) or (i-j > 3):
                return level_result.append(0)
        return level_result.append(1)
    else: # Increase or constant
        for i, j in zip(row[:-1],row[1:]):
            if (i-j >= 0) or (i-j < -3):
                return level_result.append(0)
        return level_result.append(1)

f = open("day2_input.txt", "r")
for x in f:
   line = list(map(int, x.split())) # Convert each row as a list with integer values
   level_checker(line)

print(sum(level_result))
