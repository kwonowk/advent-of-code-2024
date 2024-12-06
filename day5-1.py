import re

# Open the text and save page ordering rules and update page numbers separately
f = open('day5_input.txt', 'r')

rules = []
for x in f:
    if x != '\n':
        pattern = r'(\d+)\|(\d+)'
        matches = re.findall(pattern,x)
        rule = [int(n) for n in matches[0]]
        rules.append(rule)
    else:
        break

updates = []
for x in f:
    update = [int(i) for i in x.replace('\n','').split(',')]
    updates.append(update)

# Cross check each update page number list with every ordering rules to identify
# updates that are in right order
correct_middlepage = []
for u in updates:
    correct_middlepage.append(u[(len(u)//2)])
    for r in rules:
        if ((r[0] in u) and (r[1] in u)) and (u.index(r[0]) > u.index(r[1])):
            correct_middlepage.pop()
            break

print(sum(correct_middlepage))
