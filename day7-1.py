with open ('day7_input.txt', 'r') as f:
    lines = [list(map(int, line.replace(':','').split())) for line in f]

true_vals = []

for line in lines:
    test_val = line[0]
    for num in reversed(line[1:]):
        if test_val % num == 0:
            test_val = test_val // num
        else:
            test_val -= num

    if test_val :

        print(line)
        print('yes')
        true_vals.append(line[0])

print(sum(true_vals))
