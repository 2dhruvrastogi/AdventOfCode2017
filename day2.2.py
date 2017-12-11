f = open('input2.txt', "r")
res = 0
for line in f:
    curr_line = line.split("\t")
    int_arr = [int(i) for i in curr_line]
    int_arr.sort(reverse=True)
    for i in range(len(int_arr)):
        for j in range(1, len(int_arr)):
            if int_arr[i] % int_arr[j] == 0 and i != j:
                res += (int_arr[i]/int_arr[j])
print(res)
