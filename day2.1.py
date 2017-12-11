f = open('input2.1.txt', "r")
res = 0
for line in f:
    curr_line = line.split("\t")
    int_arr = [int(i) for i in curr_line]
    res += (max(int_arr) - min(int_arr))
f.close()
print(res)
