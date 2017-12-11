f = open("input5.py", "r")
inp = []
steps = 0
for line in f:
    inp.append(int(line))
idx = 0
x = True
while x:
    steps += 1
    curr = inp[idx]
    if curr < 3:
        inp[idx] += 1
    else:
        inp[idx] -= 1
    idx += curr
    if idx < 0 or idx > len(inp)-1:
        x = False
print(steps)
