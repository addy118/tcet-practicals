pid = [1, 2, 3, 4]
at = [0, 1, 2, 3]
bt = [8, 4, 9, 5]


def get_ct(at, bt):
    ct = []

    for i in range(len(pid)):
        if i == 0:
            ct.append(at[i] + bt[i])
        else:
            ct.append(ct[i-1] + bt[i])
    
    return ct


def get_tat(ct, at):
    tat = []

    for i in range(len(pid)):
        tat.append(ct[i] - at[i])

    return tat


def get_wt(tat, bt):
    wt = []

    for i in range(len(pid)):
        wt.append(tat[i] - bt[i])

    return wt


ct = get_ct(at, bt)

tat = get_tat(ct, at)

wt = get_wt(tat, bt)

answer = [pid, at, bt, ct, tat, wt]
headers = ['PID', 'AT', 'BT', 'CT', 'TAT', 'WT']

# for header in headers:
#     print(f"{header:4}", end="\t|")
# print()
#
# for row in answer:
#     for val in row:
#         print(f"{val:4}", end="\t|")
#     print()

# Print headers
header_line = " | ".join(f"{header:3}" for header in headers)
print(f"{header_line} |")

# Print values
for row in zip(*answer):
    print(" | ".join(f"{val:3}" for val in row) + " |")

# print(ct, tat, wt, sep='\n')
print(f"Average Waiting Time = {sum(wt)/len(wt)}")
print(f"Average Turn Around Time = {sum(tat)/len(tat)}")
        