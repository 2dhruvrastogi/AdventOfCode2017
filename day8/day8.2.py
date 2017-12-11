f = open("input8.py", "r")
dict = {}

def change_val(reg, op, val):
    if op == "inc":
        dict[reg] += val
    else:
        dict[reg] -= val
highest = 0
for line in f:
    curr_line = line.split(" ")
    if curr_line[0] not in dict:
        dict[curr_line[0]] = 0
    if curr_line[-3] not in dict:
        dict[curr_line[-3]] = 0
    if curr_line[-2] == ">":
        if dict[curr_line[-3]] > int(curr_line[-1]):
            change_val(curr_line[0], curr_line[1], int(curr_line[2]))
    elif curr_line[-2] == ">=":
        if dict[curr_line[-3]] >= int(curr_line[-1]):
            change_val(curr_line[0], curr_line[1], int(curr_line[2]))
    elif curr_line[-2] == "<":
        if dict[curr_line[-3]] < int(curr_line[-1]):
            change_val(curr_line[0], curr_line[1], int(curr_line[2]))
    elif curr_line[-2] == "<=":
        if dict[curr_line[-3]] <= int(curr_line[-1]):
            change_val(curr_line[0], curr_line[1], int(curr_line[2]))
    elif curr_line[-2] == "==":
        if dict[curr_line[-3]] == int(curr_line[-1]):
            change_val(curr_line[0], curr_line[1], int(curr_line[2]))
    elif curr_line[-2] == "!=":
        if dict[curr_line[-3]] != int(curr_line[-1]):
            change_val(curr_line[0], curr_line[1], int(curr_line[2]))
    else:
        continue
    if max(dict.values()) > highest:
        highest = max(dict.values())
print(highest)
