pid = ['p1', 'p2', 'p3', 'p4']
at = [0, 1, 2, 3]
bt = [8, 4, 9, 5]

length = int(input('Enter the total number '))

while length != 0:
    pid

# ct = [8, 12, 21, 26]
# tat = [8, 11, 19, 23]
# wt = [0, 7, 10, 18]

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
print(ct)

tat = get_tat(ct, at)
print(tat)

wt = get_wt(tat, bt)
print(wt)
        