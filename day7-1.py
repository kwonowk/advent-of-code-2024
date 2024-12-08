with open ('day7_input.txt', 'r') as f:
    lines = [list(map(int, line.replace(':','').split())) for line in f]

true_vals = []

for line in lines:
    test_val = line[0]
    print(test_val)
    line.pop(0)
    add_vals = line.copy()
    multiple_vals = []
    for num in line:
        if test_val%num== 0:
            multiple_vals.append(num)
            add_vals.remove(num)

    addition = sum(add_vals)
    multiplication = 1
    for n in multiple_vals:
        multiplication = multiplication * n

    if (test_val - addition)/ multiplication == 1:
        true_vals.append(test_val)

print(sum(true_vals))
