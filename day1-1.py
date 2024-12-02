import pandas as pd

# Convert txt to DataFrame for easy manipulation
groups = pd.read_csv('day1_input.txt', delim_whitespace=True, usecols=[0,1],names=['g1', 'g2'])

# Sort each columns and reset index for similarity score calculation
g1 = groups.g1.sort_values().reset_index(drop = True)
g2 = groups.g2.sort_values().reset_index(drop = True)

# Print the result
print(sum(abs(g2-g1)))
