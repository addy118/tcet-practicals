def findWaitingTime(processes, n, wt):
	rt = [0] * n
	
	for i in range(n):
		rt[i] = processes[i][1]
	complete = 0
	t = 0
	minm = 999999999
	short = 0
	check = False

	while complete != n:
		for j in range(n):
			if ((processes[j][2] <= t) and
					(rt[j] < minm) and rt[j] > 0):
				minm = rt[j]
				short = j
				check = True
		if check == False:
			t += 1
			continue

		rt[short] -= 1

		minm = rt[short]
		if minm == 0:
			minm = 999999999

		if rt[short] == 0:

			complete += 1
			check = False

			fint = t + 1

			wt[short] = (fint - proc[short][1] - proc[short][2])

			if wt[short] < 0:
				wt[short] = 0

		t += 1


def findTurnAroundTime(processes, n, wt, tat):
	for i in range(n):
		tat[i] = processes[i][1] + wt[i]


def findavgTime(processes, n):
	wt = [0] * n
	tat = [0] * n

	findWaitingTime(processes, n, wt)

	findTurnAroundTime(processes, n, wt, tat)

	print("Processes    Burst Time     Waiting", "Time     Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", processes[i][0], "\t\t", processes[i][1], "\t\t", wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f " % (total_wt / n))
	print("Average turn around time = ", total_tat / n)


proc = [[1, 6, 1], [2, 8, 1], [3, 7, 2], [4, 3, 3]]
n = 4
findavgTime(proc, n)
