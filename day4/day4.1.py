f = open("input4.py", "r")
res = 0
for line in f:
    s = dict()
    curr_line = line.split()
    for i in curr_line:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
    if all(value == 1 for value in s.values()):
        res += 1
print(res)
