f = open("input4.txt", "r")
res = 0
for line in f:
    curr_line = line.split()
    s = set()
    for i in curr_line:
        s.add(''.join(sorted(i)))
    if len(s) == len(curr_line):
        res += 1
print(res)
